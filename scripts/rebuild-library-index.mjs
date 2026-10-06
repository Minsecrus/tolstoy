import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const vitepressDir = path.join(rootDir, 'docs', '.vitepress')

async function loadLibraryModule(filename, catalogName, statsName, optional = false) {
  const modulePath = path.join(vitepressDir, filename)
  if (optional && !fs.existsSync(modulePath)) {
    return { catalog: [], stats: { volumeCount: 0, pageCount: 0, characterCount: 0 } }
  }

  const module = await import(`${pathToFileURL(modulePath).href}?rebuild=${process.hrtime.bigint()}`)
  const catalog = module[catalogName]
  const stats = module[statsName]
  if (!Array.isArray(catalog) || !stats || typeof stats !== 'object') {
    throw new Error(`${filename} 缺少目录或统计信息`)
  }
  if (stats.volumeCount !== catalog.length ||
      stats.pageCount !== catalog.reduce((sum, item) => sum + item.pageCount, 0) ||
      !Number.isFinite(stats.characterCount)) {
    throw new Error(`${filename} 的目录与统计信息不一致`)
  }
  return { catalog, stats }
}

export async function rebuildLibraryIndex() {
  const modules = await Promise.all([
    loadLibraryModule('library.generated.mjs', 'libraryCatalog', 'libraryStats'),
    loadLibraryModule('library.additional.mjs', 'additionalLibraryCatalog', 'additionalLibraryStats', true),
    loadLibraryModule('library.psychology.mjs', 'psychologyLibraryCatalog', 'psychologyLibraryStats', true),
    loadLibraryModule('library.history-problem.mjs', 'historyProblemLibraryCatalog', 'historyProblemLibraryStats', true)
  ])
  const catalog = modules.flatMap((module) => module.catalog)
  const stats = modules.reduce((total, module) => ({
    volumeCount: total.volumeCount + module.stats.volumeCount,
    pageCount: total.pageCount + module.stats.pageCount,
    characterCount: total.characterCount + module.stats.characterCount
  }), { volumeCount: 0, pageCount: 0, characterCount: 0 })

  const indexMarkdown = [
    '---',
    'title: "作品目录"',
    'description: "分卷目录"',
    '---',
    '',
    '# 作品目录',
    '',
    '站内作品已按分卷、分部和章节整理。选择一卷开始阅读。',
    '',
    `共 ${stats.volumeCount} 个分卷、${stats.pageCount} 个阅读页面，正文约 ${Math.round(stats.characterCount / 10000).toLocaleString('zh-CN')} 万字。`,
    '',
    ...catalog.map((item, index) => {
      const volumeNo = index + 1
      const label = item.volumeLabel === '新增卷' ? `第${volumeNo}卷：${item.title}` : `${item.volumeLabel}：${item.title}`
      const author = item.author ? ` — ${item.author}` : ''
      return `- [${label}](${item.link})${author}，${item.pageCount} 个阅读页面`
    }),
    ''
  ].join('\n')
  const indexPath = path.join(rootDir, 'docs', 'index.md')
  const existing = fs.existsSync(indexPath) ? fs.readFileSync(indexPath, 'utf8') : ''
  if (existing.replace(/\r\n/g, '\n') !== indexMarkdown) {
    const newline = existing.includes('\r\n') ? '\r\n' : '\n'
    fs.writeFileSync(indexPath, indexMarkdown.replaceAll('\n', newline))
  }
  return stats
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const stats = await rebuildLibraryIndex()
  console.log(`目录已更新：${stats.volumeCount} 卷，${stats.pageCount} 个阅读页面。`)
}
