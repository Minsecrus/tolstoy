/** Read-only comparison of every index entry with its rendered HTML parent. */
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { load } from 'cheerio'
import { createMarkdownRenderer } from 'vitepress'
import { installMathRenderer } from './algebra-math-renderer.mjs'
import { buildContinuousReadingSections, continuousReadingMarkdown } from './category-theory-continuous-reading.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const work = path.join(root, 'tmp/pdfs/category-theory-index-qa')
fs.mkdirSync(work, { recursive: true })
const renderer = await createMarkdownRenderer(path.join(root, 'docs'), {
  math: true, config(md) { installMathRenderer(md, { mode: 'external', assetDir: path.join(work,'math-svg') }) }
})
const compact = (value) => value.replace(/\s+/gu, '')
const reports = []
for (const language of ['zh', 'en']) {
  const section = (await buildContinuousReadingSections({language})).find(section => section.key === 'book-index')
  const expected = [], stack = []
  for (const page of section.pages) {
    const source = fs.readFileSync(path.join(root, 'source/category-theory', language, `pdf-${String(page.pdfPage).padStart(4, '0')}.md`), 'utf8')
    for (const line of source.split(/\r?\n/u)) {
      const bullet = line.match(/^([ \t]*)[-+*][ \t]+(.*)$/u)
      if (!bullet) continue
      const depth = bullet[1].replaceAll('\t', '    ').length / 2
      if (!Number.isInteger(depth) || (depth && stack[depth - 1] === undefined)) throw new Error(`${language}/${page.pdfPage}: source child has no explicit parent`)
      const parent = depth ? stack[depth - 1] : null
      expected.push({sourcePdfPage:page.pdfPage, depth, parent, text:bullet[2]})
      stack[depth] = expected.length - 1
      stack.length = depth + 1
    }
  }
  const html = renderer.render(continuousReadingMarkdown(section.pages, {pageAnchors:true}))
  fs.writeFileSync(path.join(work, `index-${language}.html`), html)
  fs.writeFileSync(path.join(work, `reading-index-${language}.json`), JSON.stringify(section))
  const $ = load(html), elements = $('li').toArray()
  const ownText = (element) => {
    const own = $(element).clone()
    own.find('ul,ol').remove()
    own.find('img.math-svg').each((_,math) => {
      const tex = $(math).attr('alt')
      if (tex === undefined) throw new Error('Rendered mathematics has no source label')
      $(math).replaceWith(`$${tex}$`)
    })
    return own.text().trim()
  }
  if (elements.length !== expected.length || expected.length !== 567) throw new Error(`${language}: expected 567 entries, found ${expected.length} source / ${elements.length} HTML`)
  for (const [index,element] of elements.entries()) {
    const parents = $(element).parents('li')
    const parent = parents.length ? elements.indexOf(parents[0]) : null
    const actual = {depth:parents.length,parent,text:ownText(element)}
    const source = expected[index]
    if (actual.depth !== source.depth || actual.parent !== source.parent || compact(actual.text) !== compact(source.text)) {
      throw new Error(JSON.stringify({language,index,actual,source}))
    }
  }
  const boundaries = []
  for (const page of section.pages) {
    const anchor = $(`#pdf-page-${page.pdfPage}`)
    const item = anchor.closest('li')[0], index = elements.indexOf(item)
    if (anchor.length !== 1 || index !== expected.findIndex(entry => entry.sourcePdfPage === page.pdfPage)) throw new Error(`${language}/${page.pdfPage}: source anchor left its first actual index item`)
    boundaries.push({sourcePdfPage:page.pdfPage,firstItem:index,depth:expected[index].depth,
      parent:expected[index].parent===null?null:expected[expected[index].parent].text})
  }
  reports.push({language,entryCount:elements.length,allDepthsParentsAndTextsVerified:true,boundaries})
}
fs.writeFileSync(path.join(work,'html-validation.json'),JSON.stringify(reports,null,2))
console.log(JSON.stringify(reports))
