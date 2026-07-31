import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const scriptDir = path.dirname(fileURLToPath(import.meta.url))
const rootDir = path.resolve(scriptDir, '..')
const libraryDir = path.join(rootDir, 'docs', 'library')

const markdownFiles = []
for (const volume of fs.readdirSync(libraryDir, { withFileTypes: true })) {
  if (!volume.isDirectory() || !volume.name.startsWith('volume-')) continue
  const volumeDir = path.join(libraryDir, volume.name)
  for (const entry of fs.readdirSync(volumeDir, { withFileTypes: true })) {
    if (entry.isFile() && /^chapter-\d+\.md$/.test(entry.name)) {
      markdownFiles.push(path.join(volumeDir, entry.name))
    }
  }
}

const pages = new Map()
let definitionCount = 0
let sourceDefinitionCount = 0
let localDefinitionCount = 0
let referenceCount = 0
let backlinkCount = 0

for (const file of markdownFiles) {
  const markdown = fs.readFileSync(file, 'utf8')
  const relative = path.relative(libraryDir, file).replaceAll(path.sep, '/').replace(/\.md$/, '')
  const route = `/library/${relative}`
  const ids = [...markdown.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1])
  const duplicateIds = ids.filter((id, index) => ids.indexOf(id) !== index)
  if (duplicateIds.length) {
    throw new Error(`${file} 存在重复锚点：${[...new Set(duplicateIds)].join(', ')}`)
  }

  definitionCount += (markdown.match(/class="footnote-definition\b/g) || []).length
  sourceDefinitionCount += (markdown.match(/footnote-source/g) || []).length
  localDefinitionCount += (markdown.match(/footnote-local/g) || []).length
  referenceCount += (markdown.match(/class="footnote-ref"/g) || []).length
  backlinkCount += (markdown.match(/class="footnote-backref"/g) || []).length
  pages.set(route, {
    file,
    ids: new Set(ids),
    links: [
      ...[...markdown.matchAll(/href="(\/library\/volume-\d+\/chapter-\d+)#([^"]+)"/g)]
        .map((match) => ({ route: match[1], id: match[2] })),
      ...[...markdown.matchAll(/href="#((?:note|note-ref)-[^"]+)"/g)]
        .map((match) => ({ route, id: match[1] }))
    ]
  })
}

for (const page of pages.values()) {
  for (const link of page.links) {
    const targetPage = pages.get(link.route)
    if (!targetPage) throw new Error(`${page.file} 指向不存在的页面：${link.route}`)
    if (!targetPage.ids.has(link.id)) {
      throw new Error(`${page.file} 指向不存在的锚点：${link.route}#${link.id}`)
    }
  }
}

if (referenceCount !== backlinkCount) {
  throw new Error(`正文引用 ${referenceCount} 处，但返回链接为 ${backlinkCount} 处`)
}
if (definitionCount !== sourceDefinitionCount + localDefinitionCount) {
  throw new Error('存在没有标明来源类型的注释定义')
}

console.log(`脚注检查通过：${sourceDefinitionCount.toLocaleString('zh-CN')} 条原注释，分发为 ${localDefinitionCount.toLocaleString('zh-CN')} 条页内注释；${referenceCount.toLocaleString('zh-CN')} 处正文引用的双向链接全部有效。`)
