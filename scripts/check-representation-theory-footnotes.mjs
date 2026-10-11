import assert from 'node:assert/strict'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { load } from 'cheerio'
import { createMarkdownRenderer, disposeMdItInstance } from 'vitepress'
import { installMathRenderer } from './algebra-math-renderer.mjs'
import { installRepresentationTheoryFootnotes } from './representation-theory-footnotes.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
disposeMdItInstance()
const md = await createMarkdownRenderer(path.join(root, 'docs'), {
  math: true,
  config(markdown) { installMathRenderer(markdown, { mode: 'inline' }) }
})
const input = '正文 $A$[^rt-195-1]，再次引用[^rt-195-1]。\n\n[^rt-195-1]: 原注的条件是 $n>0$。'
const outsideEnvs = [{}, { relativePath: 'library/volume-87/chapter-001.md' },
  { relativePath: 'library/volume-880/chapter-001.md' },
  { relativePath: 'library/volume-85/chapter-001.md', frontmatter: { pageClass: 'representation-theory-reading' } }]
const baselines = outsideEnvs.map((env) => md.render(input, { ...env }))
installRepresentationTheoryFootnotes(md)
installRepresentationTheoryFootnotes(md)
for (const [index, env] of outsideEnvs.entries()) assert.equal(md.render(input, { ...env }), baselines[index])
for (const env of [{ relativePath: 'library/volume-88/chapter-007.md' }, { frontmatter: { pageClass: 'algebra-reading representation-theory-reading' } }]) {
  const html = md.render(input, { ...env })
  const $ = load(html)
  assert.equal($('.footnote-ref').length, 2)
  assert.equal($('.footnote-item').length, 1)
  assert.equal($('.footnote-backref').length, 2)
  assert.equal($('mjx-container').length, 2)
  assert.match($('.footnote-item').text(), /原注的条件是/u)
  const ids = $('[id]').toArray().map((element) => $(element).attr('id'))
  assert.equal(new Set(ids).size, ids.length)
  for (const element of $('a[href^="#"]').toArray()) {
    const target = $(element).attr('href').slice(1)
    assert.ok(ids.includes(target), target)
  }
}
const inlineHtml = md.render('文字^[含 $V$ 的原注]。', { relativePath: 'library/volume-88/chapter-002.md' })
assert.equal(load(inlineHtml)('.footnote-item').length, 1)
assert.equal(load(inlineHtml)('mjx-container').length, 1)
console.log('Verified scoped native footnotes, repeated references and backlinks, all original note math, unique targets, outside-volume equality, and idempotent installation.')
