/** Verify presentation joins without editing the independently reviewed pages. */
import assert from 'node:assert/strict'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import { buildContinuousReadingSections, continuousReadingMarkdown, readingBody } from './representation-theory-continuous-reading.mjs'
import { installRepresentationTheoryFootnotes } from './representation-theory-footnotes.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const section = { key: 'chapter-002', title: '基本概念', englishTitle: 'Basic notions', firstPdfPage: 1, lastPdfPage: 2 }
let checks = 0
async function check(name, run) {
  await run()
  checks += 1
  console.log(`PASS ${name}`)
}
async function prepare(bodies, language = 'zh', spec = section) {
  return (await buildContinuousReadingSections({
    sections: [spec], language, rootDir: root,
    states: bodies.map((body) => ({ [language]: body }))
  }))[0]
}

await check('a source-page boundary does not interrupt a sentence with a native footnote', async () => {
  const source = ['# 2 基本概念\n\n称 $A$[^rt-1] 的上同调为\n\n[^rt-1]: 原书的完整注释。', '$H^i(A)$。\n\n下一段。']
  const result = await prepare(source)
  assert.equal(result.pages[1].joinsPrevious, true)
  assert.deepEqual(result.pages[0].footnoteDefinitions, ['[^rt-1]: 原书的完整注释。'])
  const reading = continuousReadingMarkdown(result.pages, { pageAnchors: true })
  assert.match(reading, /的上同调为<span[^>]+pdf-page-2[^>]+><\/span>\$H\^i\(A\)\$。/u)
  assert.equal((reading.match(/\[\^rt-1\]:/gu) ?? []).length, 1)
  assert.ok(reading.endsWith('[^rt-1]: 原书的完整注释。'))
  const renderer = await createMarkdownRenderer(path.join(root, 'docs'), { math: true })
  installRepresentationTheoryFootnotes(renderer)
  const html = renderer.render(reading, { relativePath: 'library/volume-88/chapter-002.md' })
  assert.match(html, /class="footnote-ref"/u)
  assert.match(html, /原书的完整注释/u)
  assert.equal(source[0].includes('[^rt-1]: 原书的完整注释。'), true)
})

await check('completed paragraphs and newly numbered mathematical statements remain separate', async () => {
  for (const [left, right] of [['前一段已经结束。', '后一段。'], ['一个尚未结束的片段', '**定理 2.1.3.** 完整条件。']]) {
    const result = await prepare([left, right])
    assert.equal(result.pages[1].joinsPrevious, false)
    assert.match(continuousReadingMarkdown(result.pages), /\n\n/u)
  }
  for (const right of ['**Definition 2.1.3.** Complete hypotheses.', '[56] The next complete bibliography entry.']) {
    const result = await prepare(['An unfinished previous fragment', right], 'en')
    assert.equal(result.pages[1].joinsPrevious, false)
  }
})

await check('English words remain separated when an unfinished sentence continues', async () => {
  const result = await prepare(['This algebra has a', 'unit element.'], 'en')
  assert.equal(continuousReadingMarkdown(result.pages), 'This algebra has a unit element.')
})

await check('only a duplicate opening chapter title is removed, preserving numbered subsections', async () => {
  assert.equal(readingBody(section, 'en', '# 2 Basic notions\n\n## 2.1 Associative algebras\n\nText.'), '## 2.1 Associative algebras\n\nText.')
  assert.equal(readingBody(section, 'en', '# Chapter 2. Basic notions\n\n## 2.1 Associative algebras\n\nText.'), '## 2.1 Associative algebras\n\nText.')
  assert.equal(readingBody(section, 'zh', '# 第 2 章 基本概念\n\n## 2.1 结合代数\n\n正文。'), '## 2.1 结合代数\n\n正文。')
  assert.equal(readingBody(section, 'zh', '# 2. 基本概念\n\n正文。'), '正文。')
  assert.equal(readingBody(section, 'en', '## 2.1 Associative algebras\n\nText.'), '## 2.1 Associative algebras\n\nText.')
})

await check('prose star references survive Markdown while mathematical stars remain TeX', async () => {
  const actual = readingBody(section, 'en', 'Use (*) and (**), with $A^*$ and $(*)$.')
  assert.equal(actual, 'Use (\\*) and (\\*\\*), with $A^*$ and $(*)$.')
})

await check('index children retain their explicit parent across source-page boundaries', async () => {
  const spec = { ...section, key: 'book-index' }
  const result = await prepare(['- 父条目 1\n  - 子条目甲 2', '  - 子条目乙 3\n- 后一个父条目 4'], 'zh', spec)
  const actual = continuousReadingMarkdown(result.pages, { pageAnchors: true })
  assert.match(actual, /\n  - <span[^>]+pdf-page-2/u)
  assert.equal(result.pages[1].body.startsWith('  - '), true)
  const renderer = await createMarkdownRenderer(path.join(root, 'docs'), { math: true })
  const tokens = renderer.parse(actual, {})
  assert.equal(tokens.filter((token) => token.type === 'bullet_list_open').length, 2)
})

console.log(`Verified ${checks} meaningful continuous-reading regressions; canonical files and PDF were not changed.`)

if (process.argv.includes('--require-complete')) {
  const plan = JSON.parse(fs.readFileSync(path.join(root, 'scripts/representation-theory-reading-plan.json'), 'utf8'))
  const expectedHeadings = plan.sections.flatMap((part) => part.subsections ?? [])
    .map((part) => ({ number: part.number, pdfPage: part.firstPdfPage }))
  for (const language of ['zh', 'en']) {
    const sections = await buildContinuousReadingSections({ language, rootDir: root })
    assert.deepEqual(sections.flatMap((part) => part.pages.map((page) => page.pdfPage)), plan.retainedPdfPages)
    const headings = []
    let noteCount = 0
    for (const part of sections) {
      const firstLine = part.pages[0].body.split('\n')[0]
      assert.ok(!/^#{1,2}\s+(?:Chapter\s+\d|第\s*[一二三四五六七八九十\d]+\s*章|\d+[.]?\s+[^\d])/iu.test(firstLine), `${language}/${part.key}: duplicated opening chapter heading`)
      const definitions = part.pages.flatMap((page) => page.footnoteDefinitions)
      const labels = definitions.map((definition) => definition.match(/^\[\^([^\]]+)\]:/u)[1])
      assert.equal(new Set(labels).size, labels.length, `${language}/${part.key}: duplicate footnote definition`)
      const prose = part.pages.map((page) => page.body).join('\n')
      const references = [...prose.matchAll(/\[\^([^\]]+)\]/gu)].map((match) => match[1])
      assert.deepEqual(new Set(references), new Set(labels), `${language}/${part.key}: unresolved or unreferenced original footnote`)
      noteCount += labels.length
      for (const page of part.pages) {
        for (const line of page.body.split('\n')) {
          const heading = line.match(/^##\s+(\d+\.\d+)\.?\s+/u)
          if (heading) headings.push({ number: heading[1], pdfPage: page.pdfPage })
        }
      }
    }
    assert.deepEqual(headings, expectedHeadings, `${language}: original mathematical subsections or their source pages differ from the verified plan`)
    console.log(`Verified ${language}: ${sections.length} parts, ${plan.retainedPdfPages.length} source pages, ${headings.length} mathematical subsections, ${noteCount} complete native original footnotes.`)
  }
}
