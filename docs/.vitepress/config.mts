import { defineConfig } from 'vitepress'
import { librarySidebar } from './library.generated.mjs'
import { additionalLibrarySidebar } from './library.additional.mjs'
import { psychologyLibrarySidebar } from './library.psychology.mjs'
import { historyProblemLibrarySidebar } from './library.history-problem.mjs'
import { algebraLibrarySidebar } from './library.algebra.mjs'
import { categoryTheoryLibrarySidebar } from './library.category-theory.mjs'
import { representationTheoryLibrarySidebar } from './library.representation-theory.mjs'
import { ostepLibrarySidebar } from './library.ostep.mjs'
import { translatedBooksLibrarySidebar } from './library.translated-books.mjs'
import { curateLibrarySidebar } from './library.sidebar.manual.mjs'
import { installMathRenderer } from '../../scripts/algebra-math-renderer.mjs'
import { installMathematicalBookTypography } from '../../scripts/mathematical-book-typography.mjs'
import { installCategoryTheoryDiagramRenderer } from '../../scripts/category-theory-diagram-renderer.mjs'
import { installRepresentationTheoryDiagramRenderer } from '../../scripts/representation-theory-diagram-renderer.mjs'
import { installRepresentationTheoryFootnotes } from '../../scripts/representation-theory-footnotes.mjs'

const curatedLibrarySidebar = curateLibrarySidebar([
  ...librarySidebar,
  ...additionalLibrarySidebar,
  ...psychologyLibrarySidebar,
  ...historyProblemLibrarySidebar,
  ...algebraLibrarySidebar,
  ...categoryTheoryLibrarySidebar,
  ...representationTheoryLibrarySidebar,
  ...ostepLibrarySidebar,
  ...translatedBooksLibrarySidebar
])

const librarySidebarByPath = {
  ...Object.fromEntries(
    curatedLibrarySidebar.map((volume) => [volume.items[0].link, [volume]])
  ),
  '/': curatedLibrarySidebar
}

// Many chapters are titled only "3" or "第一章"; search results name the book.
const volumeTitleByDirectory = new Map(
  curatedLibrarySidebar.map((volume) => [volume.items[0].link, volume.text])
)

function escapeAttribute(value: string) {
  return value.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;')
}

export default defineConfig({
  lang: 'zh-CN',
  title: '文学作品阅读站',
  description: '文学作品在线阅读',
  base: process.env.VITEPRESS_BASE || '/',
  cleanUrls: true,
  lastUpdated: false,
  metaChunk: true,
  themeConfig: {
    siteTitle: '文学作品阅读站',
    nav: [
      { text: '作品目录', link: '/' },
      { text: '阅读说明', link: '/about' }
    ],
    sidebar: librarySidebarByPath,
    outline: {
      level: [2, 3],
      label: '本页目录'
    },
    docFooter: {
      prev: '上一章',
      next: '下一章'
    },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '作品目录',
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式'
  },
  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => tag.startsWith('pagefind-')
      }
    }
  },
  // Full-text search is built by Pagefind from the finished HTML (see
  // pagefind.yml). Only the article body is indexed, and pages with
  // `search: false` stay unmarked so they remain out of search.
  transformHtml(html, _id, { pageData }) {
    if (pageData.frontmatter.search === false) return
    const volume = volumeTitleByDirectory.get(`/${pageData.relativePath.replace(/[^/]*$/, '')}`)
    const title = volume && volume !== pageData.title ? `${volume} · ${pageData.title}` : pageData.title
    return html.replace(
      / class="vp-doc\b/,
      ` data-pagefind-body data-pagefind-meta="title:${escapeAttribute(title)}" class="vp-doc`
    )
  },
  markdown: {
    math: true,
    config(md) {
      installMathRenderer(md, { base: process.env.VITEPRESS_BASE || '/' })
      installMathematicalBookTypography(md)
      installCategoryTheoryDiagramRenderer(md, { base: process.env.VITEPRESS_BASE || '/' })
      installRepresentationTheoryDiagramRenderer(md, { base: process.env.VITEPRESS_BASE || '/' })
      installRepresentationTheoryFootnotes(md)
    },
    typographer: true,
    headers: {
      level: [2, 3]
    }
  }
})
