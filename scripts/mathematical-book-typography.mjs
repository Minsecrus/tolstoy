const mathematicalBookPath = /^library\/volume-(?:86|87|88)\//
const mathematicalPageClasses = new Set(['algebra-reading', 'category-theory-reading', 'representation-theory-reading'])
const parenthesizedLabel = /\((?:[a-z]|tm)\)/gi

function isMathematicalBook(env) {
  // VitePress supplies a slash-normalized path relative to its docs directory.
  // A supplied path takes precedence, so other volumes retain their typography.
  if (typeof env.relativePath === 'string' && env.relativePath.length) {
    return mathematicalBookPath.test(env.relativePath)
  }
  // Content-loader rendering has no path but still parses page frontmatter.
  return String(env.frontmatter?.pageClass || '').split(/\s+/)
    .some((name) => mathematicalPageClasses.has(name))
}

/** Preserve mathematical item labels before markdown-it's typographic replacements. */
export function installMathematicalBookTypography(markdown) {
  markdown.core.ruler.before('replacements', 'mathematical_book_labels', (state) => {
    if (!isMathematicalBook(state.env)) return
    for (const block of state.tokens) {
      if (block.type !== 'inline' || !block.children) continue
      block.children = block.children.flatMap((token) => {
        // Code, HTML, links and math tokens retain their original types and contents.
        if (token.type !== 'text') return [token]
        const parts = []
        let position = 0
        for (const match of token.content.matchAll(parenthesizedLabel)) {
          if (match.index > position) {
            parts.push(Object.assign(new state.Token('text', '', 0), token, {
              content: token.content.slice(position, match.index)
            }))
          }
          // markdown-it and VitePress both restore text_special in text_join,
          // after replacements and smartquotes, just as they do escaped text.
          parts.push(Object.assign(new state.Token('text_special', '', 0), token, {
            type: 'text_special', content: match[0]
          }))
          position = match.index + match[0].length
        }
        if (!parts.length) return [token]
        if (position < token.content.length) {
          parts.push(Object.assign(new state.Token('text', '', 0), token, {
            content: token.content.slice(position)
          }))
        }
        return parts
      })
    }
  })
}
