import footnote from 'markdown-it-footnote'

const installed = Symbol('representationTheoryFootnotes')
function belongsToBook(env) {
  if (typeof env?.relativePath === 'string' && env.relativePath) {
    return /^library\/volume-88\//u.test(env.relativePath)
  }
  return typeof env?.frontmatter?.pageClass === 'string' &&
    env.frontmatter.pageClass.split(/\s+/u).includes('representation-theory-reading')
}

/** Native linked footnotes for this book, preserving every other volume's rules. */
export function installRepresentationTheoryFootnotes(markdown) {
  if (markdown[installed]) return
  markdown.use(footnote)
  for (const [ruler, name, alt] of [
    [markdown.block.ruler, 'footnote_def', ['paragraph', 'reference']],
    [markdown.inline.ruler, 'footnote_inline', []],
    [markdown.inline.ruler, 'footnote_ref', []],
    [markdown.core.ruler, 'footnote_tail', []]
  ]) {
    const rule = ruler.getRules('').find((candidate) => candidate.name === name)
    if (!rule) throw new Error(`The installed footnote plugin lacks ${name}`)
    ruler.at(name, (state, ...args) => belongsToBook(state.env) ? rule(state, ...args) : false, { alt })
  }
  markdown[installed] = true
}
