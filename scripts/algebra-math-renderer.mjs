import fs from 'node:fs'
import path from 'node:path'
import crypto from 'node:crypto'
import { createRequire } from 'node:module'
import { fileURLToPath } from 'node:url'
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js'
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js'
import { AssistiveMmlHandler } from 'mathjax-full/js/a11y/assistive-mml.js'
import { TeX } from 'mathjax-full/js/input/tex.js'
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js'
import { SVG } from 'mathjax-full/js/output/svg.js'

const require = createRequire(import.meta.url)
const mathjaxVersion = require('mathjax-full/package.json').version
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const defaultAssetDir = path.join(root, 'docs', 'public', 'math-svg')
// Increment when mathematical conversion or layout changes. Missing standalone
// table styles are repaired in the existing cache without changing formula URLs.
const rendererVersion = 4
const metrics = { em: 16, ex: 8, containerWidth: 640 }
const adaptor = liteAdaptor()
const handler = RegisterHTMLHandler(adaptor)
AssistiveMmlHandler(handler)
// Keep the complete formula/CD package set, except the two error-recovery
// packages. Both website rendering and validation must expose invalid TeX.
const packages = AllPackages.filter((name) => !['noerrors', 'noundefined'].includes(name))
// The source's \mapsfrom is U+21A4: MathJax's TeX font has its stretchy
// left-arrow/bar delimiter, although its TeX input has no named macro for it.
// The empty overset asks the SVG layout to use that horizontal delimiter's
// built-in arrow/line/bar paths, rather than a system-font Unicode text glyph.
const macros = { mapsfrom: '\\mathrel{\\overset{}{\\mmlToken{mo}[stretchy="true"]{↤}}}' }
const input = new TeX({ packages, macros })
const output = new SVG({ fontCache: 'local' })
const document = handler.create('', { InputJax: input, OutputJax: output })
const metadataCache = new Map()
const cacheLimit = 512
let conversions = 0

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (character) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[character])
}

function cacheMetadata(key, metadata) {
  metadataCache.delete(key)
  metadataCache.set(key, metadata)
  if (metadataCache.size > cacheLimit) metadataCache.delete(metadataCache.keys().next().value)
  return metadata
}

function formulaHash(tex, display) {
  return crypto.createHash('sha256').update(JSON.stringify({
    tex, display, mathjaxVersion, rendererVersion, metrics, fontCache: 'local', packages, macros
  })).digest('hex')
}

function readMetadata(svg) {
  const opening = svg.match(/<svg\b[^>]*>/)?.[0]
  if (!opening) throw new Error('MathJax did not produce an SVG element')
  const attribute = (name) => opening.match(new RegExp(`\\b${name}="([^"]*)"`))?.[1]
  const width = attribute('width')
  const height = attribute('height')
  const alignment = attribute('style')?.match(/vertical-align:\s*([^;]+)/)?.[1] || '0ex'
  const verticalAlign = alignment === '0' ? '0ex' : alignment
  if (!/^\d+(?:\.\d+)?ex$/.test(width || '') || !/^\d+(?:\.\d+)?ex$/.test(height || '') ||
      !/^-?\d+(?:\.\d+)?ex$/.test(verticalAlign)) {
    throw new Error(`Unexpected MathJax SVG dimensions: ${width}, ${height}, ${verticalAlign}`)
  }
  return { width, height, verticalAlign }
}

/** Materialize MathJax's SVGmtable styles, which otherwise live outside the SVG. */
export function normalizeStandaloneMathSvg(svg) {
  // Keep every formula without tables byte-for-byte unchanged. Editing opening
  // tags rather than parsing/reserializing XML also preserves IDs, geometry,
  // escaped TeX labels and every unrelated attribute in existing cached files.
  if (!/\bdata-mml-node\s*=\s*(["'])mtable\1|\bdata-table\s*=/.test(svg)) return svg
  const stack = []
  const tags = /<!--[\s\S]*?-->|<!\[CDATA\[[\s\S]*?\]\]>|<\?[\s\S]*?\?>|<\/?([a-z][\w:.-]*)\b(?:[^"'<>]|"[^"]*"|'[^']*')*>/gi
  return svg.replace(tags, (tag, name) => {
    if (!name) return tag
    if (tag.startsWith('</')) {
      stack.pop()
      return tag
    }
    const attributes = new Map()
    for (const match of tag.matchAll(/([\w:.-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g)) {
      attributes.set(match[1], match[2] ?? match[3])
    }
    const node = { name, attributes }
    const parent = stack.at(-1)
    const grandparent = stack.at(-2)
    const tableGroup = parent?.name === 'g' && (
      parent.attributes.get('data-mml-node') === 'mtable' ||
      (grandparent?.name === 'svg' && grandparent.attributes.has('data-table'))
    )
    const defaults = {}
    // Exact selectors in mathjax-full/js/output/svg/Wrappers/mtable.js:
    // mtable > line[data-line]/rect[data-frame], or svg[data-table] > g > ...
    if (tableGroup) {
      if ((name === 'line' && attributes.has('data-line')) ||
          (name === 'rect' && attributes.has('data-frame'))) {
        Object.assign(defaults, { 'stroke-width': '70px', fill: 'none' })
      }
      const classes = (attributes.get('class') || '').split(/\s+/)
      if (classes.includes('mjx-dashed')) defaults['stroke-dasharray'] = '140'
      if (classes.includes('mjx-dotted')) {
        Object.assign(defaults, { 'stroke-linecap': 'round', 'stroke-dasharray': '0,140' })
      }
    }
    // mtable > g > svg must allow its table/labels to extend outside the frame.
    if (name === 'svg' && parent?.name === 'g' && grandparent?.name === 'g' &&
        grandparent.attributes.get('data-mml-node') === 'mtable') defaults.overflow = 'visible'
    const styleProperties = new Set((attributes.get('style') || '').split(';')
      .map((declaration) => declaration.split(':', 1)[0].trim().toLowerCase()))
    const additions = Object.entries(defaults)
      .filter(([property]) => !attributes.has(property) && !styleProperties.has(property))
      .map(([property, value]) => ` ${property}="${value}"`).join('')
    if (!/\/\s*>$/.test(tag)) stack.push(node)
    return additions ? tag.replace(/\/?\s*>$/, (ending) => `${additions}${ending}`) : tag
  })
}

/** Upgrade only regular hash-named assets inside the workspace; never recurse. */
export function upgradeMathSvgCache({ assetDir = defaultAssetDir, dryRun = false } = {}) {
  const directory = fs.realpathSync(path.resolve(assetDir))
  const workspace = fs.realpathSync(root)
  const relative = path.relative(workspace, directory)
  if (!relative || relative === '..' || relative.startsWith(`..${path.sep}`) || path.isAbsolute(relative)) {
    throw new Error(`Math SVG cache must be a directory inside the workspace: ${assetDir}`)
  }
  const stats = { scanned: 0, changed: 0, written: 0 }
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (!entry.isFile() || !/^[a-f0-9]{64}\.svg$/.test(entry.name)) continue
    const file = path.join(directory, entry.name)
    const original = fs.readFileSync(file, 'utf8')
    const normalized = normalizeStandaloneMathSvg(original)
    stats.scanned++
    if (normalized === original) continue
    stats.changed++
    if (!dryRun) {
      fs.writeFileSync(file, normalized, 'utf8')
      stats.written++
    }
  }
  return stats
}

function convert(tex, display, hash) {
  // convert() creates a temporary MathItem, rather than adding it to document.math.
  // Reset equation identifiers so independently cached files do not depend on order.
  input.reset()
  output.options.localID = hash.slice(0, 16)
  const container = document.convert(tex, { display, ...metrics })
  conversions++
  let html = adaptor.outerHTML(container)
  const svgNode = adaptor.tags(container, 'svg')[0]
  if (!svgNode) throw new Error(`No SVG for formula: ${tex}`)
  const inlineSvg = adaptor.outerHTML(svgNode)
  html = html.replace(inlineSvg, normalizeStandaloneMathSvg(inlineSvg))

  // Tagged equations use a percentage SVG without a viewBox in MathJax's HTML
  // layout. Give the standalone image the same fixed coordinate frame so labels
  // and formula glyphs scale together at the surrounding text's ex size.
  const width = adaptor.getAttribute(svgNode, 'width')
  if (width?.endsWith('%') && !adaptor.hasAttribute(svgNode, 'viewBox')) {
    const minWidth = parseFloat(adaptor.getStyle(svgNode, 'min-width') || '0') * metrics.ex
    const pixels = Math.max(metrics.containerWidth * parseFloat(width) / 100, minWidth)
    const heightPixels = parseFloat(adaptor.getAttribute(svgNode, 'height')) * metrics.ex
    adaptor.setAttribute(svgNode, 'width', `${pixels / metrics.ex}ex`)
    adaptor.setAttribute(svgNode, 'viewBox', `0 0 ${pixels} ${heightPixels}`)
  }
  adaptor.removeAttribute(svgNode, 'aria-hidden')
  // liteAdaptor only escapes quotes in attribute values; a standalone SVG is
  // XML, so array separators (&) and comparison symbols also need escaping.
  adaptor.setAttribute(svgNode, 'aria-label', escapeHtml(tex))
  const svg = normalizeStandaloneMathSvg(adaptor.outerHTML(svgNode))
  return { html, svg, ...readMetadata(svg), error: /data-mjx-error|<mjx-merror\b|<merror\b|data-mml-node="merror"/.test(html) }
}

/** Keep markdown-it-mathjax3's dollar parsing rules; replace only its renderers. */
export function installMathRenderer(markdown, options = {}) {
  const { mode = 'external', assetDir = defaultAssetDir, base = '/' } = options
  if (!['external', 'inline'].includes(mode)) throw new Error(`Unknown math rendering mode: ${mode}`)
  const assetBase = `${base.endsWith('/') ? base : `${base}/`}math-svg/`
  const render = (tokens, index, display) => renderMath(tokens[index].content, {
    display, mode, assetDir, assetBase
  })
  markdown.renderer.rules.math_inline = (tokens, index) => render(tokens, index, false)
  markdown.renderer.rules.math_block = (tokens, index) => render(tokens, index, true)
}

export function renderMath(tex, options = {}) {
  const { display = false, mode = 'external', assetDir = defaultAssetDir, assetBase = '/math-svg/' } = options
  const hash = formulaHash(tex, display)
  if (mode === 'inline') return convert(tex, display, hash).html
  if (mode !== 'external') throw new Error(`Unknown math rendering mode: ${mode}`)
  const file = path.join(assetDir, `${hash}.svg`)
  const cacheKey = `${assetDir}\0${hash}`
  let metadata = metadataCache.get(cacheKey)
  if (!metadata) {
    if (fs.existsSync(file)) {
      const original = fs.readFileSync(file, 'utf8')
      const svg = normalizeStandaloneMathSvg(original)
      if (svg !== original) fs.writeFileSync(file, svg, 'utf8')
      metadata = readMetadata(svg)
    } else {
      const result = convert(tex, display, hash)
      if (result.error) throw new Error(`MathJax error in formula: ${tex}`)
      fs.mkdirSync(assetDir, { recursive: true })
      fs.writeFileSync(file, result.svg, 'utf8')
      metadata = result
    }
    // Cache only a few dimensions, never generated SVG or MathML strings.
    metadata = cacheMetadata(cacheKey, {
      width: metadata.width, height: metadata.height, verticalAlign: metadata.verticalAlign
    })
  }
  const label = escapeHtml(tex)
  // HTML attribute names are case-insensitive, so STYLE preserves exactly the
  // same ex dimensions and baseline in the browser. Keeping this immutable
  // attribute outside Vue's lowercase-style transform prevents its production
  // static-HTML/asset-URL transform from making a deeply nested client string-
  // concatenation AST, which overflows Rollup's stack in full chapters. It also
  // removes thousands of unnecessary ssrRenderStyle calls. No per-formula Vue
  // component or runtime styling is needed.
  // SRC is likewise an equivalent HTML attribute. This public URL already
  // contains the deployment base; bypass Vue's lowercase-src asset import so
  // /tolstoy/math-svg/... is not resolved as a second filesystem asset path.
  // Other Markdown/HTML images retain their normal Vite asset transformation.
  const image = `<img class="math-svg${display ? ' math-svg-display' : ' math-svg-inline'}" SRC="${escapeHtml(assetBase)}${hash}.svg" alt="${label}" aria-label="${label}" STYLE="width:${metadata.width};height:${metadata.height};vertical-align:${metadata.verticalAlign}" loading="lazy" decoding="async">`
  return display ? `<div class="math-display" tabindex="0">${image}</div>\n` : image
}

export function getMathRendererStats() {
  return { conversions, metadataCacheEntries: metadataCache.size, metadataCacheLimit: cacheLimit, mathjaxVersion }
}
