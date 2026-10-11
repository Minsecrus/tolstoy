import fs from 'node:fs'

const dimensions = JSON.parse(fs.readFileSync(
  new URL('./category-theory-diagram-widths.json', import.meta.url), 'utf8'
)).diagrams
const installed = Symbol('categoryTheoryDiagramRenderer')
const diagramPrefix = '/library/volume-87/diagrams/'

function diagramPath(src, base) {
  if (typeof src !== 'string' || /^(?:[a-z][a-z\d+.-]*:|\/\/)/i.test(src)) return null
  let pathname = src.split(/[?#]/, 1)[0]
  // The existing renderer remains responsible for base rewriting. Recognizing
  // an already-based URL must not change that URL or the site's other images.
  if (base !== '/' && pathname.startsWith(base)) pathname = pathname.slice(base.length - 1)
  return pathname.startsWith(diagramPrefix) ? pathname : null
}

/** Scale this book's reviewed crops with the surrounding text, retaining VitePress's image rule. */
export function installCategoryTheoryDiagramRenderer(markdown, { base = '/' } = {}) {
  if (markdown[installed]) return
  const previousImageRule = markdown.renderer.rules.image
  if (typeof previousImageRule !== 'function') throw new Error('An existing image renderer is required')
  const normalizedBase = `/${String(base).replace(/^\/+|\/+$/g, '')}/`.replace(/^\/\/$/, '/')
  markdown.renderer.rules.image = (tokens, index, options, env, self) => {
    const token = tokens[index]
    const entry = dimensions[diagramPath(token.attrGet('src'), normalizedBase)]
    if (entry) {
      const existing = token.attrGet('style')?.trim() || ''
      const separator = existing && !existing.endsWith(';') ? ';' : ''
      const sizing = `width:${entry.widthEm}em;max-width:100%;height:auto;display:inline-block;vertical-align:middle;`
      if (!existing.endsWith(sizing)) token.attrSet('style', `${existing}${separator}${sizing}`)
      // A diagram followed only by its sentence punctuation is still a display
      // paragraph. Real prose/math siblings identify the two sentence-inline
      // crops without changing their paragraph or any pre-existing classes.
      if (tokens.some((sibling) => sibling.type === 'math_inline' ||
          (sibling.type === 'text' && /[^\p{P}\p{Z}\s]/u.test(sibling.content)))) {
        const classes = (token.attrGet('class') || '').split(/\s+/).filter(Boolean)
        if (!classes.includes('category-theory-inline-diagram')) token.attrJoin('class', 'category-theory-inline-diagram')
      }
    }
    return previousImageRule(tokens, index, options, env, self)
  }
  markdown[installed] = true
}
