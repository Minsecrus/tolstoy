import { defineConfig } from 'vitepress'
import { librarySidebar } from './library.generated.mjs'

const librarySidebarByPath = {
  ...Object.fromEntries(
    librarySidebar.map((volume) => [volume.items[0].link, [volume]])
  ),
  '/': librarySidebar
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
    darkModeSwitchTitle: '切换到深色模式',
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索全文',
            buttonAriaLabel: '搜索全文'
          },
          modal: {
            noResultsText: '没有找到相关内容',
            resetButtonTitle: '清除查询',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭'
            }
          }
        }
      }
    }
  },
  markdown: {
    typographer: true,
    headers: {
      level: [2, 3]
    }
  }
})
