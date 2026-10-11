import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'

const defaultRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const separateEntries = new Set(['title-pages', 'contents', 'index', 'index-of-notation', 'notation-index', 'book-index', 'further-reading'])
const closingMarks = /[\s*_`"'\u201d\u2019\u300d\u300f\u00bb\u0029\u005d\u007d\uff09\uff3d\u3011\u3015]+$/u
const endPunctuation = /[\u3002\uff01\uff1f\uff1b\uff1a.!?;:]$/u
const referenceLabel = /^\s*\[[A-Za-z][^\]\n]+\]\s/u
const numberedEntry = /^\s*(?:\*{1,2})?(?:\(?[a-zA-Z]\)|\d+[.)\u3002]|(?:\u4f8b|\u5b9a\u7406|\u547d\u9898|\u5f15\u7406|\u63a8\u8bba|\u4e60\u9898|\u8bd1\u6821\u6ce8)[\s\u3002\uff1a:])/u

const chineseOpeningAliases = {
  preface: ['arXiv 版本前言'],
  'chapter-002': ['伴随'],
  'chapter-003': ['集合插曲'],
  'chapter-006': ['伴随、可表函子与极限'],
  'book-index': ['实体索引', '主题索引']
}

// Only the numbered chapter in the structure plan can lose a chapter prefix.
// Numbered mathematical subsection headings such as 2.1 remain untouched.
function normalizedHeading(text, section) {
  let heading = text.normalize('NFKC').trim()
  const chapter = section.key.match(/^chapter-0*(\d+)$/)?.[1]
  if (chapter) {
    heading = heading.replace(new RegExp(`^${Number(chapter)}\\s+`), '')
      .replace(/^第[一二三四五六七八九十]+章\s*/, '')
  }
  return heading.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '')
}

function escapeProseStarReferences(body) {
  let text = ''
  let mathDelimiter = null
  const escapedStarReferences = []
  for (let position = 0; position < body.length; position += 1) {
    const character = body[position]
    // Literal code is outside the book's mathematics and should retain its
    // original spelling. Its dollar signs do not open a math expression.
    if (!mathDelimiter && character === '`') {
      const ticks = body.slice(position).match(/^`+/)[0]
      const closing = body.indexOf(ticks, position + ticks.length)
      if (closing >= 0) {
        text += body.slice(position, closing + ticks.length)
        position = closing + ticks.length - 1
        continue
      }
    }
    if (character === '$') {
      let backslashes = 0
      for (let previous = position - 1; previous >= 0 && body[previous] === '\\'; previous -= 1) backslashes += 1
      if (backslashes % 2 === 0) {
        const delimiter = body[position + 1] === '$' ? '$$' : '$'
        mathDelimiter = mathDelimiter === delimiter ? null : mathDelimiter ?? delimiter
        text += delimiter
        position += delimiter.length - 1
        continue
      }
    }
    if (!mathDelimiter && character === '(') {
      const reference = body.slice(position).match(/^\((\*{1,3})\)/)
      if (reference) {
        text += `(${reference[1].replaceAll('*', '\\*')})`
        escapedStarReferences.push(reference[0])
        position += reference[0].length - 1
        continue
      }
    }
    text += character
  }
  return { body: text, escapedStarReferences }
}

function prepareReadingPage(section, language, source, pdfPage) {
  // The first line of an index page can be a two-space-indented child entry.
  // Remove blank padding, never the indentation that encodes its parent.
  let body = source.replace(/\r\n/g, '\n').replace(/^(?:[ \t]*\n)+/u, '').trimEnd()
  const removedHeadings = []
  if (section.key === 'contents') {
    const heading = body.match(/^#{1,2}\s+([^\n]+)(?:\n|$)/)
    const contentsTitle = language === 'zh' ? '\u76ee\u5f55' : 'Contents'
    if (heading && heading[1].trim().toLowerCase() === contentsTitle.toLowerCase()) {
      removedHeadings.push(heading[1])
      body = body.slice(heading[0].length).trimStart()
    }
  } else if (pdfPage === section.firstPdfPage) {
    const titles = [language === 'zh' ? section.title : section.englishTitle]
    if (language === 'zh') titles.push(...(chineseOpeningAliases[section.key] ?? []))
    if (language === 'en' && section.key === 'appendix') titles.push(`Appendix ${section.englishTitle}`)
    const expected = new Set(titles.map((title) => normalizedHeading(title, section, language)))
    const candidates = []
    let rest = body
    for (let count = 1; count <= 2; count += 1) {
      const heading = rest.match(/^#{1,2}\s+([^\n]+)(?:\n|$)/)
      if (!heading) break
      candidates.push(heading[1])
      rest = rest.slice(heading[0].length).trimStart()
      if (expected.has(normalizedHeading(candidates.join(' '), section, language))) {
        removedHeadings.push(...candidates)
        body = rest
        break
      }
    }
  }
  const publishingFooterRemoved = false
  const escaped = escapeProseStarReferences(body.replace(/^# /gm, '## '))
  return { ...escaped, removedHeadings, publishingFooterRemoved }
}

/** Normalize duplicated printed headings and footers only in presentation. */
export function readingBody(section, language, source, pdfPage = section.firstPdfPage) {
  return prepareReadingPage(section, language, source, pdfPage).body
}

function edgeParagraph(tokens, edge) {
  const group = edge === 'first' ? tokens.slice(0, 3) : tokens.slice(-3)
  if (group[0]?.type !== 'paragraph_open' || group[0].level !== 0 ||
      group[1]?.type !== 'inline' || group[2]?.type !== 'paragraph_close') return null
  if (group[1].children?.some((token) => token.type === 'image')) return null
  return group[1]
}

function isFinished(paragraph) {
  const proseEnd = paragraph.content.trimEnd().replace(closingMarks, '')
  if (endPunctuation.test(proseEnd)) return true
  // A sentence can put its final punctuation inside inline mathematics.
  const lastToken = paragraph.children?.filter((token) => token.type !== 'text' || token.content.trim()).at(-1)
  return lastToken?.type === 'math_inline' && /[.;:]\s*$/u.test(lastToken.content)
}

function joinDecision(section, previousTokens, currentTokens, language) {
  if (separateEntries.has(section.key)) return { joinsPrevious: false, joinSeparator: '' }
  const previous = edgeParagraph(previousTokens, 'last')
  const current = edgeParagraph(currentTokens, 'first')
  if (!previous || !current || isFinished(previous)) return { joinsPrevious: false, joinSeparator: '' }
  if (/\u00a9|Springer Science\+Business Media/u.test(previous.content) ||
      numberedEntry.test(current.content)) return { joinsPrevious: false, joinSeparator: '' }
  // Complete references are independent entries. A reference actually split in
  // its title can still continue across the source boundary.
  if (referenceLabel.test(current.content) ||
      (referenceLabel.test(previous.content) &&
       /(?:\d{3,4}|\u9875|pp?\.?|[\u3015\uff09)])\s*[*_]*$/u.test(previous.content))) {
    return { joinsPrevious: false, joinSeparator: '' }
  }
  const left = previous.content.trimEnd().at(-1)
  const right = current.content.trimStart().at(0)
  const delimiterCollision = (left === '$' && right === '$') ||
    (left === '*' && right === '*') || (left === '_' && right === '_')
  const wordCollision = /[A-Za-z0-9]/u.test(left) && /[A-Za-z0-9]/u.test(right)
  const englishSpace = language === 'en' && !/[-\u2010\u2011]/u.test(left)
  return { joinsPrevious: true, joinSeparator: delimiterCollision || wordCollision || englishSpace ? ' ' : '' }
}

/**
 * Output-only joins. Reviewed page files and their hashes are never changed.
 * Each page retains its source number even when its first paragraph continues
 * the preceding page. The optional states argument avoids rereading finalizer
 * inputs; the CLI reads the canonical source files directly.
 */
export async function buildContinuousReadingSections({
  sections, states, language = 'zh', rootDir = defaultRoot
} = {}) {
  if (!['zh', 'en'].includes(language)) throw new Error('language must be zh or en')
  const plan = sections ?? JSON.parse(fs.readFileSync(path.join(rootDir, 'scripts', 'category-theory-reading-plan.json'), 'utf8')).sections
  const markdown = await createMarkdownRenderer(path.join(rootDir, 'docs'), { math: true })
  const result = []
  for (const section of plan.filter((section) => section.excludeFromReading !== true)) {
    const pages = []
    let previousTokens = null
    for (let pdfPage = section.firstPdfPage; pdfPage <= section.lastPdfPage; pdfPage += 1) {
      const source = states ? states[pdfPage - 1][language] : fs.readFileSync(
        path.join(rootDir, 'source', 'category-theory', language, `pdf-${String(pdfPage).padStart(4, '0')}.md`), 'utf8')
      if (typeof source !== 'string' || !source.trim()) throw new Error(`Missing ${language} source PDF page ${pdfPage}`)
      const presentation = prepareReadingPage(section, language, source, pdfPage)
      const { body } = presentation
      const tokens = markdown.parse(body, {})
      const decision = previousTokens ? joinDecision(section, previousTokens, tokens, language) :
        { joinsPrevious: false, joinSeparator: '' }
      pages.push({ pdfPage, ...presentation, ...decision, indexList: section.key === 'book-index' })
      previousTokens = tokens
    }
    if (language === 'en') {
      // The source visibly breaks "example" across pages 34/35. Keep the
      // faithful page transcripts unchanged and rejoin this verified word only
      // in reading output; do not guess whether other hyphens are lexical.
      const previous = pages.find((page) => page.pdfPage === 34)
      const current = pages.find((page) => page.pdfPage === 35)
      if (previous && current?.joinsPrevious && /\bex-\s*$/u.test(previous.body) && /^ample\b/u.test(current.body)) {
        previous.body = previous.body.replace(/-\s*$/u, '')
        current.joinSeparator = ''
        current.dehyphenatedBoundary = { previousPdfPage: 34, word: 'example' }
      }
    }
    if (section.key === 'preface') {
      const attribution = language === 'zh'
        ? '原作 © Tom Leinster 2014, 2016；原作及本中文译本均采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可。'
        : 'Original © Tom Leinster 2014, 2016; the original and this Chinese translation are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).'
      pages.at(-1).body += `\n\n${attribution}`
      pages.at(-1).generatedAttribution = true
    }
    result.push({ ...section, pages })
  }
  return result
}

/** Plain Markdown for PDF; optional invisible inline anchors for the website. */
export function continuousReadingMarkdown(pages, { pageAnchors = false } = {}) {
  let text = ''
  for (const page of pages) {
    const anchor = pageAnchors ? `<span class="original-page-anchor" id="pdf-page-${page.pdfPage}" aria-hidden="true"></span>` : ''
    if (page.indexList) {
      if (!/^[ \t]*[-+*][ \t]+/u.test(page.body)) throw new Error(`Index PDF page ${page.pdfPage} does not begin with a list entry`)
      // Anchor a child within its actual entry. A separate HTML paragraph would
      // end its previous-page parent list before the child was parsed.
      const body = anchor ? page.body.replace(/^([ \t]*[-+*][ \t]+)/u, `$1${anchor}`) : page.body
      text += `${text ? '\n' : ''}${body}`
      continue
    }
    if (text && page.joinsPrevious) {
      text += `${page.joinSeparator}${anchor}${page.body}`
    } else {
      text += `${text ? '\n\n' : ''}${anchor ? `${anchor}\n\n` : ''}${page.body}`
    }
  }
  return text
}

async function main() {
  let language = 'zh'
  let json = false
  const args = process.argv.slice(2)
  for (let index = 0; index < args.length; index += 1) {
    if (args[index] === '--json') json = true
    else if (args[index] === '--language' && args[index + 1]) language = args[++index]
    else throw new Error('Usage: node scripts/category-theory-continuous-reading.mjs --json [--language zh|en]')
  }
  if (!json) throw new Error('Specify --json for the reusable section/page data')
  const sections = await buildContinuousReadingSections({ language })
  process.stdout.write(JSON.stringify({ version: 1, language, sections }))
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((error) => { console.error(error.message); process.exitCode = 1 })
}
