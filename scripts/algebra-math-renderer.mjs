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
// Increment when the rendering settings or standalone SVG normalization change.
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

function convert(tex, display, hash) {
  // convert() creates a temporary MathItem, rather than adding it to document.math.
  // Reset equation identifiers so independently cached files do not depend on order.
  input.reset()
  output.options.localID = hash.slice(0, 16)
  const container = document.convert(tex, { display, ...metrics })
  conversions++
  const html = adaptor.outerHTML(container)
  const svgNode = adaptor.tags(container, 'svg')[0]
  if (!svgNode) throw new Error(`No SVG for formula: ${tex}`)

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
  const svg = adaptor.outerHTML(svgNode)
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
      metadata = readMetadata(fs.readFileSync(file, 'utf8'))
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
