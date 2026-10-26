import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import PagefindSearch from './PagefindSearch.vue'
import DuFuPoem from './DuFuPoem.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('DuFuPoem', DuFuPoem)
  },
  Layout: () => h(DefaultTheme.Layout, null, {
    // Where VitePress's own search button sits; the modal lives outside the
    // nav bar so no nav styling can clip the overlay.
    'nav-bar-content-before': () => h('pagefind-modal-trigger', { placeholder: '搜索全文' }),
    'layout-bottom': () => h(PagefindSearch)
  })
} satisfies Theme
