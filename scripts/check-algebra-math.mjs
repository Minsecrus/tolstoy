import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import { installMathRenderer } from './algebra-math-renderer.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const markdown = await createMarkdownRenderer(path.join(root, 'docs'), {
  math: true,
  config(md) { installMathRenderer(md, { mode: 'inline' }) }
}, '/')
let pages = 0
let expressions = 0
const failures = []

for (const language of ['en', 'zh']) {
  const directory = path.join(root, 'source', 'algebra', language)
  for (const name of fs.readdirSync(directory).filter(name => /^pdf-\d{4}\.md$/.test(name)).sort()) {
    const source = fs.readFileSync(path.join(directory, name), 'utf8')
    const rendered = markdown.render(source)
    pages++
    expressions += (rendered.match(/<mjx-container\b/g) || []).length
    if (/data-mjx-error|<mjx-merror\b|<merror\b|data-mml-node="merror"/.test(rendered)) {
      const errors = [...rendered.matchAll(/data-mjx-error="([^"]+)"/g)].map(match => match[1])
      failures.push(`${language}/${name}: ${errors.join('; ') || 'MathML merror'}`)
    }
    for (const match of source.matchAll(/!\[[^\]]*\]\((\/library\/volume-86\/[^)]+)\)/g)) {
      const asset = path.join(root, 'docs', 'public', match[1])
      if (!fs.existsSync(asset)) failures.push(`${language}/${name}: missing asset ${match[1]}`)
    }
  }
}

console.log(`Rendered ${pages} bilingual source pages and ${expressions} math expressions.`)
if (failures.length) {
  console.error(failures.join('\n'))
  process.exitCode = 1
} else {
  console.log('No MathJax errors or missing linked diagram assets. This checks rendering, not mathematical correctness.')
}
