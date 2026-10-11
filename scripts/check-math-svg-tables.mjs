import assert from 'node:assert/strict'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { load } from 'cheerio'
import { getMathRendererStats, normalizeStandaloneMathSvg, renderMath, upgradeMathSvgCache } from './algebra-math-renderer.mjs'

// Load the wrapper after the complete SVG output has initialized its CJS graph.
const { SVGmtable } = await import('mathjax-full/js/output/svg/Wrappers/mtable.js')

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const temporaryRoot = path.join(root, 'tmp')
fs.mkdirSync(temporaryRoot, { recursive: true })
const temporary = fs.mkdtempSync(path.join(temporaryRoot, 'math-svg-tables-'))
const rules = 'g[data-mml-node="mtable"] > line[data-line], svg[data-table] > g > line[data-line], ' +
  'g[data-mml-node="mtable"] > rect[data-frame], svg[data-table] > g > rect[data-frame]'
let checks = 0
function check(name, run) {
  run()
  checks++
  console.log(`PASS ${name}`)
}
function xml(svg) { return load(svg, { xmlMode: true }) }
function assertVisibleRules(svg, expectedCount) {
  const $ = xml(svg)
  const lines = $(rules)
  assert.equal(lines.length, expectedCount)
  for (const element of lines.toArray()) {
    assert.equal($(element).attr('stroke-width'), '70px')
    assert.equal($(element).attr('fill'), 'none')
  }
}
function structuralSnapshot(svg) {
  const $ = xml(svg)
  const styleNames = new Set(['stroke-width', 'fill', 'stroke-dasharray', 'stroke-linecap', 'overflow'])
  return $('*').toArray().map((element) => ({
    name: element.name,
    attributes: Object.fromEntries(Object.entries(element.attribs).filter(([name]) => !styleNames.has(name))),
    text: $(element).children().length ? undefined : $(element).text()
  }))
}
function fileFromHtml(html, assetDir) {
  const src = load(html)('img.math-svg').attr('src')
  assert.ok(src)
  return path.join(assetDir, path.basename(src))
}
const tableFixture = `<svg xmlns="http://www.w3.org/2000/svg" width="10ex" height="4ex" viewBox="0 -1000 4000 2000">
<g stroke="currentColor" fill="currentColor" stroke-width="0"><g data-mml-node="mtable">
<line data-line="v" class="mjx-solid" x1="100" y1="-200" x2="100" y2="800"/>
<line data-line="h" class="mjx-dashed" x1="0" y1="100" x2="500" y2="100"></line>
<line data-line="h" class="mjx-dotted" x1="0" y1="200" x2="500" y2="200"/>
<rect data-frame="true" class="mjx-dotted" x="0" y="-200" width="500" height="1000"/>
<g><svg data-table="true" x="-25" width="100%"><g>
<line data-line="h" class="mjx-dashed" x1="0" y1="300" x2="500" y2="300"/>
<rect data-frame="true" class="mjx-solid" x="0" y="0" width="500" height="500"/>
</g></svg></g>
<g><line data-line="h" class="mjx-dotted" x1="0" y1="400" x2="500" y2="400"/></g>
</g><line data-line="v" class="mjx-solid" x1="200" y1="-200" x2="200" y2="800"/></g></svg>`

try {
  check('the restored table defaults match the installed MathJax stylesheet', () => {
    const styles = SVGmtable.styles
    assert.deepEqual(styles['g[data-mml-node="mtable"] > line[data-line], svg[data-table] > g > line[data-line]'],
      { 'stroke-width': '70px', fill: 'none' })
    assert.deepEqual(styles['g[data-mml-node="mtable"] > rect[data-frame], svg[data-table] > g > rect[data-frame]'],
      { 'stroke-width': '70px', fill: 'none' })
    assert.deepEqual(styles['g[data-mml-node="mtable"] > .mjx-dashed, svg[data-table] > g > .mjx-dashed'],
      { 'stroke-dasharray': '140' })
    assert.deepEqual(styles['g[data-mml-node="mtable"] > .mjx-dotted, svg[data-table] > g > .mjx-dotted'],
      { 'stroke-linecap': 'round', 'stroke-dasharray': '0,140' })
    assert.deepEqual(styles['g[data-mml-node="mtable"] > g > svg'], { overflow: 'visible' })
  })
  check('solid, dashed and dotted rules/frames remain visible below inherited stroke-width zero', () => {
    const normalized = normalizeStandaloneMathSvg(tableFixture)
    const $ = xml(normalized)
    assertVisibleRules(normalized, 6)
    assert.equal($('g[data-mml-node="mtable"] > .mjx-dashed').attr('stroke-dasharray'), '140')
    for (const element of $('g[data-mml-node="mtable"] > .mjx-dotted').toArray()) {
      assert.equal($(element).attr('stroke-dasharray'), '0,140')
      assert.equal($(element).attr('stroke-linecap'), 'round')
    }
    assert.equal($('svg[data-table] > g > .mjx-dashed').attr('stroke-dasharray'), '140')
    assert.equal($('g[data-mml-node="mtable"] > g > svg').attr('overflow'), 'visible')
    assert.equal($('g[data-mml-node="mtable"] > g > line').attr('stroke-width'), undefined)
    assert.equal($('svg').first().children('g').children('line').attr('stroke-width'), undefined)
    assert.deepEqual(structuralSnapshot(normalized), structuralSnapshot(tableFixture))
    assert.equal(normalizeStandaloneMathSvg(normalized), normalized)
  })
  check('explicit attributes/styles, quoted markup and unrelated shapes are preserved', () => {
    const original = `<svg aria-label="x &gt; y; &quot;quoted&quot;"><!-- <g data-mml-node="mtable"> -->
<g data-mml-node = 'mtable'><line data-line='h' class='mjx-dashed' stroke-width='25px' fill='red' style='stroke-dasharray: 50;'/>
<rect data-frame='true' style='stroke-width: 40px; fill: blue;'/><rect class='mjx-solid' width='200' height='100'/>
</g><path data-c="41" stroke-width="0" d="M 0 0 L 100 100"/></svg>`
    assert.equal(normalizeStandaloneMathSvg(original), original)
    const noTable = '<svg><g stroke-width="0"><line class="mjx-solid" data-line="h"/><rect data-frame="true"/><path data-c="41" d="M0 0"/></g></svg>'
    assert.equal(normalizeStandaloneMathSvg(noTable), noTable)
  })
  check('all three original tensor product tables use unchanged TeX in both rendering modes', () => {
    const source = fs.readFileSync(path.join(root, 'source', 'representation-theory', 'zh', 'pdf-0083.md'), 'utf8')
    const formulas = [...source.matchAll(/\$\$\r?\n([\s\S]*?)\r?\n\$\$/g)]
      .filter((match) => match[1].includes('\\begin{array}')).map((match) => `${match[1]}\n`)
    assert.equal(formulas.length, 3)
    const freshDir = path.join(temporary, 'fresh')
    for (const [index, tex] of formulas.entries()) {
      const html = renderMath(tex, { display: true, assetDir: freshDir })
      const svg = fs.readFileSync(fileFromHtml(html, freshDir), 'utf8')
      assert.equal(xml(svg)('svg').first().attr('aria-label'), tex)
      assertVisibleRules(svg, [6, 10, 10][index])
      assertVisibleRules(renderMath(tex, { display: true, mode: 'inline' }), [6, 10, 10][index])
    }
  })
  check('fresh bordered and dashed arrays, including equation-label layouts, retain their rules', () => {
    const solid = renderMath(String.raw`\begin{array}{|c|c|}\hline a&b\\\hline c&d\\\hline\end{array}`, { mode: 'inline' })
    const dashed = renderMath(String.raw`\begin{array}{:c:c:}\hdashline a&b\\\hdashline c&d\\\hdashline\end{array}`, { mode: 'inline' })
    for (const svg of [solid, dashed]) {
      const $ = xml(svg)
      assert.ok($(rules).length >= 3)
      assertVisibleRules(svg, $(rules).length)
      assert.ok($('rect[data-frame]').length)
    }
    const $ = xml(dashed)
    assert.ok($(rules).filter('.mjx-dashed').length)
    for (const element of $(rules).filter('.mjx-dashed').toArray()) {
      assert.equal($(element).attr('stroke-dasharray'), '140')
    }
    const tagged = renderMath(String.raw`\begin{array}{c|c}a&b\\\hline c&d\end{array}\tag{1}`, { mode: 'inline', display: true })
    const taggedXml = xml(tagged)
    const nested = taggedXml('g[data-mml-node="mtable"] > g > svg')
    assert.ok(nested.length)
    for (const element of nested.toArray()) assert.equal(taggedXml(element).attr('overflow'), 'visible')
    assertVisibleRules(tagged, 2)
  })
  check('cache reads repair the existing S3 URL without conversions or layout changes', () => {
    const hashName = '3453a42f1c05d26cc90402966061437f120d3025bc3435f6811e7160d5b2f343.svg'
    const original = fs.readFileSync(path.join(root, 'docs', 'public', 'math-svg', hashName), 'utf8')
    const $ = xml(original)
    const tex = $('svg').first().attr('aria-label')
    // Make this regression independent of whether the real cache was already upgraded.
    const legacy = original.replace(/ (?:stroke-width="70px"|fill="none"|stroke-dasharray="140"|stroke-dasharray="0,140"|stroke-linecap="round"|overflow="visible")/g, '')
    const cacheDir = path.join(temporary, 'cached')
    fs.mkdirSync(cacheDir)
    fs.writeFileSync(path.join(cacheDir, hashName), legacy)
    const conversions = getMathRendererStats().conversions
    const html = renderMath(tex, { display: true, assetDir: cacheDir })
    assert.equal(path.basename(fileFromHtml(html, cacheDir)), hashName)
    assert.equal(getMathRendererStats().conversions, conversions)
    const upgraded = fs.readFileSync(path.join(cacheDir, hashName), 'utf8')
    assertVisibleRules(upgraded, 6)
    assert.deepEqual(structuralSnapshot(upgraded), structuralSnapshot(legacy))
    assert.equal(renderMath(tex, { display: true, assetDir: cacheDir }), html)
    assert.equal(fs.readFileSync(path.join(cacheDir, hashName), 'utf8'), upgraded)
    assert.deepEqual(fs.readdirSync(cacheDir), [hashName])
  })
  check('whole-cache upgrades support dry runs, are idempotent, and preserve other files', () => {
    const cacheDir = path.join(temporary, 'migration')
    fs.mkdirSync(cacheDir)
    const tableName = `${'a'.repeat(64)}.svg`
    const otherName = `${'b'.repeat(64)}.svg`
    const unrelated = '<svg><path data-c="41" d="M0 0"/></svg>'
    fs.writeFileSync(path.join(cacheDir, tableName), tableFixture)
    fs.writeFileSync(path.join(cacheDir, otherName), unrelated)
    fs.writeFileSync(path.join(cacheDir, 'not-a-formula.svg'), tableFixture)
    fs.mkdirSync(path.join(cacheDir, `${'c'.repeat(64)}.svg`))
    assert.deepEqual(upgradeMathSvgCache({ assetDir: cacheDir, dryRun: true }), { scanned: 2, changed: 1, written: 0 })
    assert.equal(fs.readFileSync(path.join(cacheDir, tableName), 'utf8'), tableFixture)
    assert.deepEqual(upgradeMathSvgCache({ assetDir: cacheDir }), { scanned: 2, changed: 1, written: 1 })
    assertVisibleRules(fs.readFileSync(path.join(cacheDir, tableName), 'utf8'), 6)
    assert.deepEqual(upgradeMathSvgCache({ assetDir: cacheDir }), { scanned: 2, changed: 0, written: 0 })
    assert.equal(fs.readFileSync(path.join(cacheDir, otherName), 'utf8'), unrelated)
    assert.equal(fs.readFileSync(path.join(cacheDir, 'not-a-formula.svg'), 'utf8'), tableFixture)
    assert.throws(() => upgradeMathSvgCache({ assetDir: root }), /inside the workspace/)
    assert.throws(() => upgradeMathSvgCache({ assetDir: path.parse(root).root }), /inside the workspace/)
  })
  console.log(`Verified ${checks} focused standalone-SVG table regressions.`)
} finally {
  const target = path.resolve(temporary)
  assert.ok(target.startsWith(`${path.resolve(temporaryRoot)}${path.sep}`))
  fs.rmSync(target, { recursive: true, force: true })
}
