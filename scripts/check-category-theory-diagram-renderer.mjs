import assert from 'node:assert/strict'
import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer, disposeMdItInstance } from 'vitepress'
import { load } from 'cheerio'
import siteConfig from '../docs/.vitepress/config.mts'
import { installMathRenderer } from './algebra-math-renderer.mjs'
import { installMathematicalBookTypography } from './mathematical-book-typography.mjs'
import { installCategoryTheoryDiagramRenderer } from './category-theory-diagram-renderer.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const mapping = JSON.parse(fs.readFileSync(new URL('./category-theory-diagram-widths.json', import.meta.url), 'utf8'))
const mainCrop = '/library/volume-87/diagrams/pdf-0019-associativity.png'
const base = '/tolstoy/'
let checks = 0
function check(name, run) {
  run()
  checks++
  console.log(`PASS ${name}`)
}
async function create(scaled) {
  // VitePress retains one module-level markdown instance; create distinct
  // original/scaled instances so this comparison tests the wrapper itself.
  disposeMdItInstance()
  return createMarkdownRenderer(path.join(root, 'docs'), {
    ...siteConfig.markdown,
    image: { lazyLoading: true },
    highlight: (source) => source,
    config(md) {
      if (scaled) {
        const previousBase = process.env.VITEPRESS_BASE
        process.env.VITEPRESS_BASE = base
        try { siteConfig.markdown.config(md) }
        finally {
          if (previousBase === undefined) delete process.env.VITEPRESS_BASE
          else process.env.VITEPRESS_BASE = previousBase
        }
      }
      else {
        // The pre-crop-rule configuration is the comparison baseline, even
        // after the shared site config has integrated the new installer.
        installMathRenderer(md, { base })
        installMathematicalBookTypography(md)
      }
      // The site's math output is kept in memory for this focused rendering test.
      installMathRenderer(md, { mode: 'inline', base })
      if (scaled) installCategoryTheoryDiagramRenderer(md, { base })
    }
  }, base)
}
const original = await create(false)
const scaled = await create(true)
const env = { relativePath: 'library/volume-87/chapter-001.md' }
const imageAttrs = (html) => ({ ...load(html)('img').first().attr() })

check('all 191 mapped crop widths and asset hashes match current page reviews', () => {
  assert.equal(mapping.diagramCount, 191)
  assert.equal(Object.keys(mapping.diagrams).length, 191)
  let count = 0
  for (const name of fs.readdirSync(path.join(root, 'source/category-theory/review')).filter((name) => /^pdf-\d+\.json$/.test(name))) {
    const review = JSON.parse(fs.readFileSync(path.join(root, 'source/category-theory/review', name), 'utf8'))
    for (const diagram of review.diagrams || []) {
      const entry = mapping.diagrams[diagram.path]
      assert.ok(entry, diagram.path)
      assert.equal(entry.widthPt, diagram.widthPt)
      assert.equal(entry.sourcePdfPage, review.pdfPage)
      assert.deepEqual(entry.clipPt, diagram.clipPt)
      assert.equal(entry.sha256, diagram.sha256)
      assert.equal(entry.bodyFontPt, mapping.bodyFontPt)
      assert.ok(Math.abs(entry.widthEm - entry.widthPt / entry.bodyFontPt) < 0.00000051)
      const asset = path.join(root, 'docs/public', diagram.path)
      assert.equal(crypto.createHash('sha256').update(fs.readFileSync(asset)).digest('hex'), entry.sha256)
      count++
    }
  }
  assert.equal(count, mapping.diagramCount)
})

check('every English and Chinese crop is scaled; existing image attributes remain', () => {
  const seen = new Set()
  let count = 0
  for (const language of ['en', 'zh']) {
    const sourceDir = path.join(root, 'source/category-theory', language)
    for (const filename of fs.readdirSync(sourceDir).filter((name) => name.endsWith('.md'))) {
      const tokens = scaled.parse(fs.readFileSync(path.join(sourceDir, filename), 'utf8'), { ...env })
      for (const inline of tokens.filter((token) => token.type === 'inline')) {
        for (const token of inline.children.filter((token) => token.type === 'image')) {
          const src = token.attrGet('src')
          if (!mapping.diagrams[src]) continue
          const source = `![${token.content}](${src} "crop title")`
          const oldAttrs = imageAttrs(original.render(source, { ...env }))
          const newAttrs = imageAttrs(scaled.render(source, { ...env }))
          const style = newAttrs.style
          delete newAttrs.style
          assert.deepEqual(newAttrs, oldAttrs, src)
          assert.equal(newAttrs.loading, 'lazy')
          assert.ok(style.includes(`width:${mapping.diagrams[src].widthEm}em;`), src)
          assert.ok(style.includes('max-width:100%;height:auto;display:inline-block;vertical-align:middle;'))
          seen.add(src)
          count++
        }
      }
    }
  }
  assert.equal(count, 382)
  assert.equal(seen.size, 191)
})

check('the reported crop scales to 199.646674px at the actual 17px body font', () => {
  const entry = mapping.diagrams[mainCrop]
  assert.equal(entry.widthPt, 117)
  assert.equal(entry.widthEm, 11.743922)
  assert.ok(Math.abs(entry.widthEm * 17 - 199.646674) < 0.000001)
})

check('base paths, query fragments, links, alt text and titles remain intact', () => {
  for (const src of [mainCrop, `${base.slice(0, -1)}${mainCrop}`, `${mainCrop}?v=1#crop`]) {
    const source = `[![A & B](${src} "source title")](https://example.org/page)`
    const oldHtml = original.render(source, { ...env })
    const newHtml = scaled.render(source, { ...env })
    const oldAttrs = imageAttrs(oldHtml)
    const newAttrs = imageAttrs(newHtml)
    assert.ok(newAttrs.style.includes('width:11.743922em'))
    delete newAttrs.style
    assert.deepEqual(newAttrs, oldAttrs)
    assert.equal(load(newHtml)('a').attr('href'), load(oldHtml)('a').attr('href'))
  }
})

check('other volumes, unknown assets, remote images and inline math retain exact output', () => {
  for (const source of [
    '![other book](/library/volume-86/diagrams/diagram.png)',
    '![other volume](/library/volume-870/diagrams/diagram.png)',
    '![not reviewed](/library/volume-87/diagrams/unknown.png)',
    `![remote](https://example.org${mainCrop})`,
    `![remote](//example.org${mainCrop})`,
    '$A_0 \\to A_4$'
  ]) assert.equal(scaled.render(source, { ...env }), original.render(source, { ...env }))
})

check('both actual inline diagrams stay in their prose paragraph without added block markup', () => {
  for (const language of ['en', 'zh']) {
    for (const pdfPage of [50, 160]) {
      const filename = `pdf-${String(pdfPage).padStart(4, '0')}.md`
      const body = fs.readFileSync(path.join(root, 'source/category-theory', language, filename), 'utf8')
      const paragraph = body.split('\n').find((line) => line.includes('!['))
      const html = scaled.render(paragraph, { ...env })
      const $ = load(html)
      assert.equal($('p').length, 1)
      assert.equal($('p > img').length, 1)
      assert.ok($('p').text().trim().length > 12)
      assert.ok($('img').attr('style').includes('display:inline-block'))
      assert.ok($('img').hasClass('category-theory-inline-diagram'))
      assert.equal($('div, figure').length, 0)
    }
  }
})

check('display crops and punctuation-only siblings retain display classification', () => {
  for (const source of [
    `![crop](${mainCrop})`,
    `![crop](${mainCrop}).`,
    `![crop](${mainCrop})。`
  ]) assert.ok(!load(scaled.render(source, { ...env }))('img').hasClass('category-theory-inline-diagram'))
  for (const source of [`prose ![crop](${mainCrop})`, `$A_0=$ ![crop](${mainCrop})`]) {
    assert.ok(load(scaled.render(source, { ...env }))('img').hasClass('category-theory-inline-diagram'))
  }
  for (const language of ['en', 'zh']) {
    for (const pdfPage of [70, 86]) {
      const filename = `pdf-${String(pdfPage).padStart(4, '0')}.md`
      const body = fs.readFileSync(path.join(root, 'source/category-theory', language, filename), 'utf8')
      const paragraph = body.split('\n').find((line) => line.includes('!['))
      assert.ok(!load(scaled.render(paragraph, { ...env }))('img').hasClass('category-theory-inline-diagram'))
    }
  }
})

check('only the two actual sentence-inline crops per language receive the new class', () => {
  const inlineCrops = new Set([
    '/library/volume-87/diagrams/pdf-0050-functor-pair.png',
    '/library/volume-87/diagrams/pdf-0160-two-object-category.png'
  ])
  let count = 0
  for (const language of ['en', 'zh']) {
    const sourceDir = path.join(root, 'source/category-theory', language)
    for (const filename of fs.readdirSync(sourceDir).filter((name) => name.endsWith('.md'))) {
      const tokens = scaled.parse(fs.readFileSync(path.join(sourceDir, filename), 'utf8'), { ...env })
      for (const inline of tokens.filter((token) => token.type === 'inline')) {
        for (let index = 0; index < inline.children.length; index++) {
          const token = inline.children[index]
          if (token.type !== 'image' || !mapping.diagrams[token.attrGet('src')]) continue
          const src = token.attrGet('src')
          const html = scaled.renderer.rules.image(inline.children, index, scaled.options, { ...env }, scaled.renderer)
          const isInline = load(html)('img').hasClass('category-theory-inline-diagram')
          assert.equal(isInline, inlineCrops.has(src), `${language}/${filename}: ${src}`)
          if (isInline) count++
        }
      }
    }
  }
  assert.equal(count, 4)
})

check('previous image-rule custom attributes and style survive, even repeated rendering', () => {
  const plain = new original.constructor()
  const previous = plain.renderer.rules.image
  let previousCalls = 0
  plain.renderer.rules.image = (...args) => {
    previousCalls++
    args[0][args[1]].attrSet('data-existing-renderer', 'retained')
    return previous(...args)
  }
  installCategoryTheoryDiagramRenderer(plain, { base })
  installCategoryTheoryDiagramRenderer(plain, { base })
  const tokens = plain.parse(`before ![crop](${mainCrop}) after`, {})
  const image = tokens.find((token) => token.type === 'inline').children.find((token) => token.type === 'image')
  image.attrSet('style', 'border:0')
  image.attrSet('width', '468')
  image.attrSet('class', 'existing-image-class')
  for (let i = 0; i < 2; i++) {
    const attrs = imageAttrs(plain.renderer.render(tokens, plain.options, {}))
    assert.equal(attrs['data-existing-renderer'], 'retained')
    assert.equal(attrs.width, '468')
    assert.equal(attrs.class, 'existing-image-class category-theory-inline-diagram')
    assert.ok(attrs.style.startsWith('border:0;'))
    assert.equal((attrs.style.match(/width:11\.743922em/g) || []).length, 1)
  }
  assert.equal(previousCalls, 2)
})

console.log(`Verified ${checks} focused crop-rendering checks without a site build or PDF export.`)
