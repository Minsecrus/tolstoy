import assert from 'node:assert/strict'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import siteConfig from '../docs/.vitepress/config.mts'
import { installMathRenderer } from './algebra-math-renderer.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const markdown = await createMarkdownRenderer(path.join(root, 'docs'), {
  ...siteConfig.markdown,
  highlight: (source) => source,
  config(md) {
    // Exercise the site's actual plugin configuration; keep test formulas in memory.
    siteConfig.markdown.config(md)
    installMathRenderer(md, { mode: 'inline' })
  }
})
assert.equal(markdown.options.typographer, true)

let checks = 0
function check(name, run) {
  run()
  checks++
  console.log(`PASS ${name}`)
}
function render(source, relativePath, frontmatter = {}) {
  return markdown.render(source, { relativePath, frontmatter })
}

const labels = [...'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
  .map((letter) => `(${letter})`).join(' ') + ' (tm) (TM) ©'
for (const volume of [86, 87, 88]) {
  check(`volume ${volume}: every letter label, trademark-like label and actual ©`, () => {
    assert.ok(render(labels, `library/volume-${volume}/chapter-001.md`).includes(labels))
  })
}

check('mathematical frontmatter when a content loader supplies no relative path', () => {
  for (const pageClass of ['algebra-reading', 'algebra-reading category-theory-reading', 'representation-theory-reading']) {
    const source = `---\npageClass: ${pageClass}\n---\n\n(c) (C) (r) (R) (tm) (TM) ©`
    assert.ok(render(source).includes('(c) (C) (r) (R) (tm) (TM) ©'))
  }
})

check('volume 85, other literature and similar volume numbers keep replacements', () => {
  for (const relativePath of [
    'library/volume-85/chapter-001.md', 'library/volume-1/chapter-001.md',
    'library/volume-870/chapter-001.md', 'library/volume-880/chapter-001.md', 'index.md', undefined
  ]) {
    assert.ok(render('(c) (C) (r) (R) (tm) (TM) © ... -- ---', relativePath)
      .includes('© © ® ® ™ ™ © … – —'))
  }
  // A real nonmathematical path wins over stale or inherited class metadata.
  assert.ok(render('(c)', 'library/volume-85/chapter-001.md', {
    pageClass: 'algebra-reading'
  }).includes('<p>©</p>'))
})

check('other mathematical-page typography, entities, emphasis and links still render', () => {
  const html = render('(c) ... -- --- "quoted" **(C)** [(r)](#item) &copy; © `(tm)`',
    'library/volume-87/chapter-001.md')
  assert.ok(html.includes('(c) … – — “quoted”'))
  assert.ok(html.includes('<strong>(C)</strong>'))
  assert.ok(html.includes('href="#item">(r)</a>'))
  assert.ok(html.includes('&copy; ©'))
  assert.ok(html.includes('<code>(tm)</code>'))
  assert.ok(!html.includes('®') && !html.includes('™'))
})

check('inline and display math token contents are unchanged and MathJax succeeds', () => {
  const inline = String.raw`f(c) = \text{(c), (r), (tm)}`
  const display = String.raw`\text{(C), (R), (TM)} \quad f(c) = c`
  const source = `(c) $${inline}$\n\n$$\n${display}\n$$\n`
  const env = { relativePath: 'library/volume-87/chapter-001.md' }
  const tokens = markdown.parse(source, env)
  const formulas = tokens.flatMap((token) => token.type === 'inline'
    ? token.children.filter((child) => child.type === 'math_inline')
    : token.type === 'math_block' ? [token] : [])
  assert.deepEqual(formulas.map((token) => token.content.trim()), [inline, display])
  const html = markdown.render(source, { ...env })
  assert.equal((html.match(/<mjx-container\b/g) || []).length, 2)
  assert.ok(!/data-mjx-error|<mjx-merror\b|<merror\b|data-mml-node="merror"/.test(html))
  assert.ok(!html.includes('©') && !html.includes('®') && !html.includes('™'))
})

check('original category theory note and example labels remain (c)', () => {
  const original = fs.readFileSync(path.join(root, 'docs/library/volume-87/chapter-001.md'), 'utf8')
  for (const label of ['**注 1.1.2**', '**例 1.1.3', '**例 1.1.8']) {
    const start = original.indexOf(label)
    assert.ok(start >= 0, `Missing source label: ${label}`)
    const item = original.slice(start).split('\n').find((line) => line.startsWith('(c)'))
    assert.ok(item, `Missing (c) item under ${label}`)
    const html = render(`${label.replaceAll('**', '')}\n\n${item}`,
      'library/volume-87/chapter-001.md')
    assert.ok(html.includes('<p>(c) '), label)
    assert.ok(!html.includes('©'), label)
  }
})

check('a shared renderer can alternate mathematical and literary pages', () => {
  for (let i = 0; i < 3; i++) {
    assert.ok(render('(c)', 'library/volume-87/chapter-001.md').includes('<p>(c)</p>'))
    assert.ok(render('(c)', 'library/volume-85/chapter-001.md').includes('<p>©</p>'))
    assert.equal(markdown.options.typographer, true)
  }
})

console.log(`Verified ${checks} typography checks with VitePress and the shared site configuration.`)
