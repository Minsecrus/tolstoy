import assert from 'node:assert/strict'
import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer, disposeMdItInstance } from 'vitepress'
import { load } from 'cheerio'
import { installMathRenderer } from './algebra-math-renderer.mjs'
import { installMathematicalBookTypography } from './mathematical-book-typography.mjs'
import { installRepresentationTheoryDiagramRenderer } from './representation-theory-diagram-renderer.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const mapping = JSON.parse(fs.readFileSync(new URL('./representation-theory-diagram-widths.json', import.meta.url), 'utf8'))
const base = '/tolstoy/'
const prefix = '/library/volume-88/diagrams/'
const inlineClass = 'representation-theory-inline-diagram'
const allowPending = process.argv.includes('--allow-pending')
let checks = 0
function check(name, run) {
  run()
  checks++
  console.log(`PASS ${name}`)
}
async function create(scaled) {
  disposeMdItInstance()
  return createMarkdownRenderer(path.join(root, 'docs'), {
    image: { lazyLoading: true },
    highlight: (source) => source,
    config(md) {
      installMathRenderer(md, { mode: 'inline', base })
      installMathematicalBookTypography(md)
      if (scaled) installRepresentationTheoryDiagramRenderer(md, { base })
    }
  }, base)
}
const original = await create(false)
const scaled = await create(true)
const env = { relativePath: 'library/volume-88/chapter-001.md' }
const imageAttrs = (html) => ({ ...load(html)('img').first().attr() })
const mainCrop = Object.keys(mapping.diagrams)[0]
const reviewDir = path.join(root, 'source/representation-theory/review')
const reviewFiles = fs.existsSync(reviewDir)
  ? fs.readdirSync(reviewDir).filter((name) => /^pdf-\d+\.json$/.test(name)) : []
const hasProseSibling = (tokens) => tokens.some((token) => token.type === 'math_inline' ||
  (token.type === 'text' && /[^\p{P}\p{Z}\s]/u.test(token.content)))

check('current review inventory and native-font calibration are explicitly recorded', () => {
  assert.equal(mapping.bodyFontEvidence.nativeFont, 'CMR10')
  assert.ok(Math.abs(mapping.bodyFontPt - 10 * 72 / 72.27) < 0.00001)
  assert.equal(mapping.reviewRecordCount, reviewFiles.length)
  assert.equal(mapping.completeReviewInventory, mapping.pendingReviewPages.length === 0)
  const source = JSON.parse(fs.readFileSync(path.join(root, 'scripts/representation-theory-source-manifest.json'), 'utf8'))
  assert.equal(mapping.sourceSha256, source.sourceSha256)
  assert.equal(mapping.sourcePdfPageCount, source.pdfPageCount)
  if (!allowPending) assert.equal(mapping.pendingReviewPages.length, 0, 'Missing reviews require an explicit --allow-pending preparation run')
})

check('every mapped physical width, scan-page scale and crop hash matches current reviews', () => {
  assert.equal(Object.keys(mapping.diagrams).length, mapping.diagramCount)
  let count = 0
  for (const name of reviewFiles) {
    const review = JSON.parse(fs.readFileSync(path.join(reviewDir, name), 'utf8'))
    for (const diagram of review.diagrams || []) {
      const entry = mapping.diagrams[diagram.path]
      assert.ok(entry, diagram.path)
      assert.equal(entry.widthPt, diagram.widthPt)
      assert.equal(entry.sourcePdfPage, review.pdfPage)
      assert.deepEqual(entry.clipPt, diagram.clipPt)
      assert.ok(Math.abs(entry.widthPt - (entry.clipPt[2] - entry.clipPt[0])) <= 0.02)
      assert.equal(entry.sha256, diagram.sha256)
      const calibration = mapping.pageCalibrations[String(review.pdfPage)]
      assert.ok(calibration, diagram.path)
      assert.equal(entry.scanScaleX, calibration.scanScaleX)
      assert.equal(entry.bodyFontPt, calibration.effectiveHorizontalBodyFontPt)
      assert.ok(Math.abs(entry.bodyFontPt - mapping.bodyFontPt * entry.scanScaleX) < 0.00000001)
      assert.ok(Math.abs(entry.widthEm - entry.widthPt / entry.bodyFontPt) < 0.00000051)
      assert.equal(entry.pixelVerification.sourcePixelMatch, true)
      assert.ok(entry.pixelVerification.dpi >= 250)
      assert.ok(entry.pixelVerification.widthPx > 0 && entry.pixelVerification.heightPx > 0)
      const asset = path.join(root, 'docs/public', diagram.path)
      assert.equal(crypto.createHash('sha256').update(fs.readFileSync(asset)).digest('hex'), entry.sha256)
      count++
    }
  }
  assert.equal(count, mapping.diagramCount)
})

const references = []
const pendingAssets = new Set()
for (const language of ['en', 'zh']) {
  const directory = path.join(root, 'source/representation-theory', language)
  if (!fs.existsSync(directory)) continue
  for (const filename of fs.readdirSync(directory).filter((name) => /^pdf-\d+\.md$/.test(name))) {
    const tokens = scaled.parse(fs.readFileSync(path.join(directory, filename), 'utf8'), { ...env })
    for (const inline of tokens.filter((token) => token.type === 'inline')) {
      for (let index = 0; index < inline.children.length; index++) {
        const token = inline.children[index]
        if (token.type !== 'image' || !token.attrGet('src')?.startsWith(prefix)) continue
        const src = token.attrGet('src')
        if (!mapping.diagrams[src]) { pendingAssets.add(src); continue }
        references.push({ language, filename, token, siblings: inline.children, index, src })
      }
    }
  }
}

check('actual English and Chinese image references use current reviewed crop records', () => {
  if (!allowPending) assert.deepEqual([...pendingAssets], [], 'Unmapped source crops remain')
  for (const language of ['en', 'zh']) {
    const seen = new Set(references.filter((item) => item.language === language).map((item) => item.src))
    if (!allowPending) assert.deepEqual([...seen].sort(), Object.keys(mapping.diagrams).sort(), `${language}: missing crop references`)
  }
  for (const item of references) {
    const { src, token } = item
    const source = `![${token.content}](${src} "crop title")`
    const oldAttrs = imageAttrs(original.render(source, { ...env }))
    const newAttrs = imageAttrs(scaled.render(source, { ...env }))
    const style = newAttrs.style
    delete newAttrs.style
    assert.deepEqual(newAttrs, oldAttrs, src)
    assert.equal(newAttrs.loading, 'lazy')
    assert.ok(style.includes(`width:${mapping.diagrams[src].widthEm}em;`), src)
    assert.ok(style.includes('max-width:100%;height:auto;display:inline-block;vertical-align:middle;'))
  }
})

check('actual sentence-inline and display crops are classified from their own prose/math siblings', () => {
  for (const { siblings, index, language, filename, src } of references) {
    const html = scaled.renderer.rules.image(siblings, index, scaled.options, { ...env }, scaled.renderer)
    const $ = load(html)
    assert.equal($('img').hasClass(inlineClass), hasProseSibling(siblings), `${language}/${filename}: ${src}`)
    assert.equal($('div, figure').length, 0)
  }
})

check('other volumes, unknown crops, remote images and native inline math retain exact output', () => {
  for (const source of [
    '![other book](/library/volume-86/diagrams/diagram.png)',
    '![other book](/library/volume-87/diagrams/diagram.png)',
    '![other volume](/library/volume-880/diagrams/diagram.png)',
    '![not reviewed](/library/volume-88/diagrams/unknown.png)',
    `![remote](https://example.org${mainCrop || prefix + 'unknown.png'})`,
    `![remote](//example.org${mainCrop || prefix + 'unknown.png'})`,
    '$A_0 \\to A_4$'
  ]) assert.equal(scaled.render(source, { ...env }), original.render(source, { ...env }))
})

if (mainCrop) {
  const widthEm = mapping.diagrams[mainCrop].widthEm
  check('base prefixes, query fragments, links, alt text and titles remain intact', () => {
    for (const src of [mainCrop, `${base.slice(0, -1)}${mainCrop}`, `${mainCrop}?v=1#crop`]) {
      const source = `[![A & B](${src} "source title")](https://example.org/page)`
      const oldHtml = original.render(source, { ...env })
      const newHtml = scaled.render(source, { ...env })
      const oldAttrs = imageAttrs(oldHtml)
      const newAttrs = imageAttrs(newHtml)
      assert.ok(newAttrs.style.includes(`width:${widthEm}em;`))
      delete newAttrs.style
      assert.deepEqual(newAttrs, oldAttrs)
      assert.equal(load(newHtml)('a').attr('href'), load(oldHtml)('a').attr('href'))
    }
  })

  check('punctuation-only siblings stay display; real prose and math remain sentence-inline', () => {
    for (const source of [`![crop](${mainCrop})`, `![crop](${mainCrop}).`, `![crop](${mainCrop})。`]) {
      assert.ok(!load(scaled.render(source, { ...env }))('img').hasClass(inlineClass))
    }
    for (const source of [`prose ![crop](${mainCrop})`, `$A_0=$ ![crop](${mainCrop})`]) {
      const $ = load(scaled.render(source, { ...env }))
      assert.ok($('img').hasClass(inlineClass))
      assert.equal($('p').length, 1)
      assert.equal($('div, figure').length, 0)
    }
  })

  check('previous image-rule attributes and styles survive repeated installation/rendering', () => {
    const plain = new original.constructor()
    const previous = plain.renderer.rules.image
    let previousCalls = 0
    plain.renderer.rules.image = (...args) => {
      previousCalls++
      args[0][args[1]].attrSet('data-existing-renderer', 'retained')
      return previous(...args)
    }
    installRepresentationTheoryDiagramRenderer(plain, { base })
    installRepresentationTheoryDiagramRenderer(plain, { base })
    const tokens = plain.parse(`before ![crop](${mainCrop}) after`, {})
    const token = tokens.find((item) => item.type === 'inline').children.find((item) => item.type === 'image')
    token.attrSet('style', 'border:0')
    token.attrSet('width', String(mapping.diagrams[mainCrop].pixelVerification.widthPx))
    token.attrSet('class', 'existing-image-class')
    for (let i = 0; i < 2; i++) {
      const attrs = imageAttrs(plain.renderer.render(tokens, plain.options, {}))
      assert.equal(attrs['data-existing-renderer'], 'retained')
      assert.equal(attrs.width, String(mapping.diagrams[mainCrop].pixelVerification.widthPx))
      assert.equal(attrs.class, `existing-image-class ${inlineClass}`)
      assert.ok(attrs.style.startsWith('border:0;'))
      assert.equal(attrs.style.split(`width:${widthEm}em;`).length - 1, 1)
    }
    assert.equal(previousCalls, 2)
  })
} else {
  assert.ok(allowPending, 'No actual reviewed crop is available for renderer sizing tests')
  console.log('PENDING crop-specific sizing/base/attribute tests: no actual reviewed crop exists yet')
}

const inlineCount = references.filter((item) => hasProseSibling(item.siblings)).length
console.log(`Verified ${checks} focused rendering checks; ${mapping.diagramCount} mapped assets; ${references.length} actual EN/ZH references, ${inlineCount} sentence-inline; ${mapping.pendingReviewPages.length} missing reviews and ${pendingAssets.size} unmapped source images.`)
