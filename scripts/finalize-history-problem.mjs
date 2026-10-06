import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { fileURLToPath } from 'node:url'
import { rebuildLibraryIndex } from './rebuild-library-index.mjs'

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const volumeDir = path.join(rootDir, 'docs', 'library', 'volume-85')
const modulePath = path.join(rootDir, 'docs', '.vitepress', 'library.history-problem.mjs')
const pdfPath = path.join(rootDir, 'docs', 'public', 'library', 'volume-85', 'the-history-problem.pdf')
const bookTitle = '历史问题：东亚战争纪念的政治'
const fullTitle = 'The History Problem: The Politics of War Commemoration in East Asia'
const sourceHash = 'f2e7d9fb63cbbe45382333d16fe889514d6d22e47eaa3a2314361b306d8f8e00'
const numberedKeys = ['intro', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'conclusion']
const sourceManifestPath = path.join(rootDir, 'scripts', 'history-problem-source-manifest.json')

function fail(message) {
  throw new Error(message)
}

function chapterFile(number) {
  return `chapter-${String(number).padStart(3, '0')}.md`
}

function chapterRoute(number) {
  return `/library/volume-85/chapter-${String(number).padStart(3, '0')}`
}

function readRequired(file) {
  if (!fs.existsSync(file)) fail(`缺少文件：${file}`)
  return fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n')
}

function sameSequence(actual, expected, label) {
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    const position = actual.findIndex((item, i) => item !== expected[i])
    const mismatch = position < 0 ? Math.min(actual.length, expected.length) : position
    fail(`${label} 与原文不一致：应有 ${expected.length} 项，实际 ${actual.length} 项；第 ${mismatch + 1} 项应为 ${expected[mismatch] ?? '结束'}，实际为 ${actual[mismatch] ?? '结束'}`)
  }
}

function rawPages(source) {
  return [...source.matchAll(/\[\[P:([0-9]+|[ivxlcdm]+)\]\]/g)].map((m) => m[1])
}

function pageMarkers(markdown) {
  return [...markdown.matchAll(/\[\[P:([0-9]+|[ivxlcdm]+)\]\]|<span class="original-page-marker" id="page-([0-9]+|[ivxlcdm]+)"[^>]*>/g)]
    .map((m) => m[1] ?? m[2])
}

function referenceMarkers(markdown) {
  return [...markdown.matchAll(/\[\[N:([a-z0-9]+):(\d+)\]\]|<sup class="footnote-ref" id="note-ref-([a-z0-9]+)-(\d+)"[^>]*>/g)]
    .map((m) => `${m[1] ?? m[3]}:${Number(m[2] ?? m[4])}`)
}

function definitionMarkers(markdown) {
  return [...markdown.matchAll(/\[\[D:([a-z0-9]+):(\d+)\]\]|<span class="footnote-definition footnote-source" id="note-([a-z0-9]+)-(\d+)"[^>]*>/g)]
    .map((m) => `${m[1] ?? m[3]}:${Number(m[2] ?? m[4])}`)
}

function metadataTitle(markdown, file) {
  const title = markdown.match(/^---\n[\s\S]*?^title:\s*(.+)$/m)?.[1]?.trim()
  if (!title) fail(`${file} 缺少 title 元数据`)
  let parsed = title
  if (title.startsWith('"')) parsed = JSON.parse(title)
  else if (title.startsWith("'")) parsed = title.slice(1, -1)
  const heading = markdown.match(/^# (.+)$/m)?.[1]?.trim()
  if (!heading || heading !== parsed) fail(`${file} 的标题元数据与一级标题不一致`)
  if (!markdown.includes('class="reading-meta"')) fail(`${file} 缺少阅读页元数据`)
  return parsed
}

function validateMarkers(markdown, page, label) {
  sameSequence(pageMarkers(markdown), page.pages, `${label} 页码`)
  sameSequence(referenceMarkers(markdown), page.references, `${label} 正文注释引用`)
  sameSequence(definitionMarkers(markdown), page.definitions, `${label} 原注释定义`)
  const ids = [...markdown.matchAll(/\sid="([^"\s]+)"/g)].map((m) => m[1])
  if (new Set(ids).size !== ids.length) fail(`${label} 存在重复 HTML 锚点`)
  const unknownMarkers = markdown.replace(/\[\[(?:P:(?:[0-9]+|[ivxlcdm]+)|[ND]:[a-z0-9]+:\d+)\]\]/g, '').match(/\[\[[^\n]*?\]\]/g)
  if (unknownMarkers) fail(`${label} 存在未知标记：${unknownMarkers.join(', ')}`)
  if (/\bTODO\b|待翻译|待补充|此处省略|后续翻译/i.test(markdown)) fail(`${label} 存在未完成占位文字`)
}

function pageMarker(page, inline = false) {
  const label = page === '280' ? '书后作者简介（PDF 第 293 页）' : `原书第 ${page} 页`
  const style = inline
    ? 'display:inline;font-size:0;width:0;scroll-margin-top:96px;'
    : 'display:block;margin:1.5em 0 .5em;color:var(--vp-c-text-3);font-size:12px;scroll-margin-top:96px;'
  return `<span class="original-page-marker" id="page-${page}" style="${style}"${inline ? ` aria-label="${label}" title="${label}"` : ''}>${label}</span>`
}

function normalizeCrossPageParagraphs(markdown) {
  let result = markdown
  // 仅处理由原始页码标记及空行打断的无句末标点段落；保留章节、列表和完整段落边界。
  const boundary = /([^\n]+)\n[ \t]*\n(?:[ \t]*\n)*\[\[P:([0-9]+|[ivxlcdm]+)\]\]\n[ \t]*\n(?:[ \t]*\n)*([^\n]+)/g
  let joined
  do {
    joined = false
    result = result.replace(boundary, (match, previous, page, next) => {
      if (/^\s*(?:[#<>]|[-*+]\s|\d+[.)]\s|---\s*$)/.test(previous) || /^\s*(?:[#<>]|[-*+]\s|\d+[.)]\s|\[\[P:)/.test(next)) return match
      const plainPrevious = previous
        .replace(/\[\[N:[a-z0-9]+:\d+\]\]/g, '')
        .replace(/<sup class="footnote-ref"[\s\S]*?<\/sup>/g, '')
        .replace(/<span class="original-page-marker"[\s\S]*?<\/span>/g, '')
        .trimEnd()
      if (!plainPrevious || /[。！？.!?;；：:”’）》)\]\}]$/.test(plainPrevious)) return match
      if (/^(?:序言|导论|结论|参考文献|索引|关于作者|Preface|Introduction|Conclusion|Bibliography|Index|About the Author|第[一二三四五六]章)(?:\s|$)/.test(next.trim())) return match
      const space = /[\x21-\x7e]$/.test(plainPrevious) && /^[\x21-\x7e]/.test(next.trimStart()) ? ' ' : ''
      joined = true
      return previous.trimEnd() + pageMarker(page, true) + space + next.trimStart()
    })
  } while (joined)
  return result
}

function finalizeMarkers(markdown) {
  let result = normalizeCrossPageParagraphs(markdown).replace(/\[\[P:([0-9]+|[ivxlcdm]+)\]\]/g, (_, page) => pageMarker(page))
  // 作者简介没有印刷页码；内部 page-280 锚点仅用于来源清单核对。
  result = result.replace(/(<span class="original-page-marker" id="page-280"[^>]*>)[\s\S]*?(<\/span>)/g, '$1书后作者简介（PDF 第 293 页）$2')
  result = result.replace(/\[\[N:([a-z0-9]+):(\d+)\]\]/g, (_, key, number) => {
    if (!numberedKeys.includes(key)) fail(`未知正文注释分组 ${key}`)
    return `<sup class="footnote-ref" id="note-ref-${key}-${number}"><a href="#note-${key}-${number}" aria-label="查看原书注释 ${number}">[${number}]</a></sup>`
  })
  result = result.replace(/\[\[D:([a-z0-9]+):(\d+)\]\]([\s\S]*?)(?=\[\[D:|\s*$)/g, (_, key, number, body) => {
    if (!numberedKeys.includes(key)) fail(`未知原注释分组 ${key}`)
    if (!body.trim()) fail(`原注释 ${key}:${number} 没有正文`)
    if (body.includes('class="footnote-backref"')) fail(`原注释 ${key}:${number} 已有返回链接但尚未转换定义标记`)
    return `<span class="footnote-definition footnote-source" id="note-${key}-${number}" style="display:block;scroll-margin-top:96px;"><span class="footnote-number">[${number}]</span></span>\n\n${body.trim()}\n\n<span class="footnote-backrefs"><a class="footnote-backref" href="#note-ref-${key}-${number}" aria-label="返回正文注释 ${number}">↩</a></span>\n\n`
  })
  return result.trimEnd() + '\n'
}

function validateFinalLinks(rendered, pages) {
  for (const page of pages) {
    const file = chapterFile(page.chapter)
    const markdown = rendered.get(file)
    if (/\[\[(?:P|N|D):/.test(markdown)) fail(`${file} 仍有未转换标记`)
    sameSequence([...markdown.matchAll(/class="footnote-backref" href="#note-ref-([a-z0-9]+)-(\d+)"/g)]
      .map((m) => `${m[1]}:${Number(m[2])}`), page.definitions, `${file} 注释返回链接`)
    for (const item of page.references) {
      const [key, number] = item.split(':')
      const expected = `<a href="#note-${key}-${number}" aria-label="查看原书注释 ${number}">[${number}]</a>`
      if (!markdown.includes(expected)) fail(`${file} 正文注释 ${item} 的链接不正确`)
    }
    for (const item of page.definitions) {
      const [key, number] = item.split(':')
      if (!markdown.includes(`href="#note-ref-${key}-${number}"`)) fail(`${file} 原注释 ${item} 的返回链接不正确`)
    }
    if (/href="[^"#]+#(?:note|note-ref)-/.test(markdown)) fail(`${file} 存在跨页注释链接，注释应位于本章末尾`)
    for (const match of markdown.matchAll(/href="#((?:note|note-ref)-[^"\s]+)"/g)) {
      if (!markdown.includes(`id="${match[1]}"`)) fail(`${file} 指向不存在的同页注释锚点 ${match[1]}`)
    }
    if (page.definitions.length) {
      const notesStart = markdown.indexOf('\n## 注释\n')
      if (notesStart < 0) fail(`${file} 缺少章末注释标题`)
      if (referenceMarkers(markdown.slice(notesStart)).length || definitionMarkers(markdown.slice(0, notesStart)).length) {
        fail(`${file} 注释未完整放在正文末尾`)
      }
    }
  }
}

function countCharacters(markdown) {
  const body = markdown.slice(markdown.indexOf('\n# ') + 1)
  const text = body
    .replace(/<span class="original-page-marker"[\s\S]*?<\/span>/g, '')
    .replace(/<[^>]+>/g, '')
    .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
    .replace(/&(?:[a-z]+|#\d+|#x[0-9a-f]+);/gi, '')
    .replace(/[\s#*_`>|]/g, '')
  return [...text].length
}

function makeLibraryModule(pages, rendered, manifest) {
  const item = (page) => ({ text: page.title, link: chapterRoute(page.chapter) })
  const sidebar = [{ text: bookTitle, collapsed: true, items: [
    { text: '本卷首页', link: '/library/volume-85/' },
    { text: '中文译本', collapsed: false, items: pages.filter((p) => p.chapter <= 9).map(item) },
    { text: '文献、索引与作者', collapsed: true, items: pages.filter((p) => p.chapter >= 18).map(item) },
    { text: '英文原书 PDF', link: '/library/volume-85/original' }
  ] }]
  const catalog = [{ title: bookTitle, fullTitle, volumeLabel: '新增卷', author: 'Hiro Saito', translator: '本站 AI 辅助中文译本',
    isbn: '978-0-8248-5674-8 / 978-0-8248-7439-1', publicationDate: '2016-12', copyrightYear: 2017,
    source: manifest.source, sourceSha256: manifest.sha256, link: '/library/volume-85/', firstPage: chapterRoute(1), pageCount: pages.length }]
  const stats = { volumeCount: 1, pageCount: pages.length, characterCount: [...rendered.values()].reduce((sum, text) => sum + countCharacters(text), 0) }
  return '// 此文件由 scripts/finalize-history-problem.mjs 生成。\n' +
    `export const historyProblemLibrarySidebar = ${JSON.stringify(sidebar, null, 2)}\n\n` +
    `export const historyProblemLibraryCatalog = ${JSON.stringify(catalog, null, 2)}\n\n` +
    `export const historyProblemLibraryStats = ${JSON.stringify(stats, null, 2)}\n`
}

async function main() {
  const args = process.argv.slice(2)
  const defaultSourceDir = path.join(rootDir, 'tmp', 'pdfs', 'history-problem')
  let sourceDir = fs.existsSync(path.join(defaultSourceDir, 'manifest.json')) ? defaultSourceDir : null
  let checkOnly = false
  for (let i = 0; i < args.length; i += 1) {
    if (args[i] === '--check') checkOnly = true
    else if (args[i] === '--source-dir' && args[i + 1]) sourceDir = path.resolve(args[++i])
    else fail(`未知参数 ${args[i]}；用法：node scripts/finalize-history-problem.mjs [--source-dir 路径] [--check]`)
  }
  const manifest = JSON.parse(readRequired(sourceManifestPath))
  if (manifest.sha256 !== sourceHash || manifest.pdfPages !== 293 || manifest.source !== 'https://www.loc.gov/item/2019666840/') fail('来源清单与指定的英文开放获取版本不一致')
  if (!fs.existsSync(pdfPath)) fail(`缺少未经修改的英文原书：${pdfPath}`)
  const actualHash = crypto.createHash('sha256').update(fs.readFileSync(pdfPath)).digest('hex')
  if (actualHash !== manifest.sha256) fail('网站英文 PDF 的 SHA-256 与原书清单不一致')
  sameSequence(manifest.sections.map((s) => s.key), ['preface', ...numberedKeys], '正文清单分组')
  sameSequence(manifest.sections.map((s) => s.chapter), [1, 2, 3, 4, 5, 6, 7, 8, 9], '正文清单章号')
  if (manifest.sections.reduce((sum, s) => sum + (s.noteCount || 0), 0) !== 815) fail('原书注释总数应为 815')
  sameSequence(manifest.supplementalPages.map((p) => p.key), ['bibliography', 'index', 'author'], '附录清单分组')
  sameSequence(manifest.supplementalPages.map((p) => p.chapter), [18, 19, 20], '附录清单章号')
  if (sourceDir) {
    const extracted = JSON.parse(readRequired(path.join(sourceDir, 'manifest.json')))
    if (extracted.sha256 !== manifest.sha256 || extracted.pdfPages !== manifest.pdfPages) fail('抽取源文件清单与已保存清单不一致')
    sameSequence(extracted.sections.map((s) => s.key), manifest.sections.map((s) => s.key), '抽取源文件分组')
  }
  const pages = manifest.sections.map((section) => {
    const references = section.referenceNumbers.map((n) => `${section.key}:${n}`)
    if (sourceDir) {
      const source = readRequired(path.join(sourceDir, `${section.key}.txt`))
      sameSequence([...source.matchAll(/\[\[N:([a-z0-9]+):(\d+)\]\]/g)].map((m) => `${m[1]}:${Number(m[2])}`), references, `${section.key} 原文引用清单`)
      sameSequence(rawPages(source), section.pages, `${section.key} 原文页码清单`)
    }
    if (section.key !== 'preface' && references.length !== section.noteCount) fail(`${section.key} 的原文引用数与注释数不一致`)
    return { ...section, references, definitions: section.key === 'preface' ? [] : references }
  })
  for (const key of numberedKeys) {
    const section = manifest.sections.find((s) => s.key === key)
    const definitions = Array.from({ length: section.noteCount }, (_, n) => `${key}:${n + 1}`)
    if (sourceDir) {
      const source = readRequired(path.join(sourceDir, `notes-${key}.txt`))
      sameSequence([...source.matchAll(/\[\[D:([a-z0-9]+):(\d+)\]\]/g)].map((m) => `${m[1]}:${Number(m[2])}`), definitions, `${key} 原文注释清单`)
      sameSequence(rawPages(source), [], `${key} 原文注释页码标记`)
    }
  }
  for (const page of manifest.supplementalPages) {
    if (sourceDir) sameSequence(rawPages(readRequired(path.join(sourceDir, `${page.key}.txt`))), page.pages, `${page.key} 原文页码清单`)
    pages.push({ ...page, references: [], definitions: [] })
  }
  pages.sort((a, b) => a.chapter - b.chapter)
  const actualFiles = fs.readdirSync(volumeDir).filter((file) => /^chapter-.*\.md$/.test(file)).sort()
  sameSequence(actualFiles, pages.map((p) => chapterFile(p.chapter)), '12 个中文阅读页面')
  const rendered = new Map()
  for (const page of pages) {
    const file = chapterFile(page.chapter)
    const markdown = readRequired(path.join(volumeDir, file))
    const title = metadataTitle(markdown, file)
    if (page.key === 'index' && title === '索引') page.title = title
    else if (title !== page.title) fail(`${file} 题名应为 ${page.title}，实际为 ${title}`)
    validateMarkers(markdown, page, file)
    const converted = checkOnly ? markdown : finalizeMarkers(markdown)
    validateMarkers(converted, page, file)
    rendered.set(file, converted)
  }
  validateFinalLinks(rendered, pages)
  const module = makeLibraryModule(pages, rendered, manifest)
  if (checkOnly) {
    if (readRequired(modulePath) !== module) fail('目录元数据或字数统计已过期，请重新运行 finalizer')
  } else {
    // 所有页面、标号及链接通过验证后，才写入译文和目录元数据。
    for (const [file, markdown] of rendered) {
      const target = path.join(volumeDir, file)
      if (readRequired(target) !== markdown) fs.writeFileSync(target, markdown)
    }
    if (!fs.existsSync(modulePath) || readRequired(modulePath) !== module) fs.writeFileSync(modulePath, module)
    await rebuildLibraryIndex()
  }
  const totalNotes = pages.reduce((sum, p) => sum + p.definitions.length, 0)
  const totalPages = pages.reduce((sum, p) => sum + p.pages.length, 0)
  console.log(`${checkOnly ? '验证' : '整合'}完成：${pages.length} 个中文阅读页面，${totalPages} 个来源页锚点（含无印刷页码的作者简介），${totalNotes} 条原注释及双向链接；英文 PDF SHA-256 一致。`)
}

main().catch((error) => {
  console.error(`《历史问题》整合失败：${error.message}`)
  process.exitCode = 1
})
