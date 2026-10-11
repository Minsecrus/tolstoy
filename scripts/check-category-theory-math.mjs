import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { createMarkdownRenderer } from 'vitepress'
import { installMathRenderer } from './algebra-math-renderer.mjs'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const expected = JSON.parse(fs.readFileSync(path.join(root, 'scripts/category-theory-source-manifest.json'), 'utf8')).pdfPageCount
const markdown = await createMarkdownRenderer(path.join(root, 'docs'), {
  math: true,
  config(md) { installMathRenderer(md, { mode: 'inline' }) }
}, '/')
let pages = 0
let expressions = 0
const failures = []
for (const language of ['en', 'zh']) {
  const directory = path.join(root, 'source/category-theory', language)
  const names = fs.existsSync(directory) ? fs.readdirSync(directory).filter(name => /^pdf-\d{4}\.md$/.test(name)).sort() : []
  if (process.argv.includes('--require-complete') && names.length !== expected) failures.push(`${language}: expected ${expected} source pages, found ${names.length}`)
  for (const name of names) {
    const source = fs.readFileSync(path.join(directory, name), 'utf8')
    const rendered = markdown.render(source)
    pages++
    expressions += (rendered.match(/<mjx-container\b/g) || []).length
    if (/data-mjx-error|<mjx-merror\b|<merror\b|data-mml-node="merror"/.test(rendered)) {
      const errors = [...rendered.matchAll(/data-mjx-error="([^"]+)"/g)].map(match => match[1])
      failures.push(`${language}/${name}: ${errors.join('; ') || 'MathML merror'}`)
    }
    for (const match of source.matchAll(/!\[[^\]]*\]\((\/library\/volume-87\/[^)]+)\)/g)) {
      if (!fs.existsSync(path.join(root, 'docs/public', match[1]))) failures.push(`${language}/${name}: missing asset ${match[1]}`)
    }
    if (source.includes('\ufffd')) failures.push(`${language}/${name}: unresolved replacement character`)
  }
}
console.log(`Rendered ${pages}/${expected * 2} bilingual source pages and ${expressions} math expressions.`)
if (failures.length) {
  console.error(failures.join('\n'))
  process.exitCode = 1
} else {
  console.log('No MathJax errors, replacement characters or missing diagram assets. This verifies rendering, not mathematical correctness.')
}
