<script setup lang="ts">
import { onMounted } from 'vue'
import { useData, withBase } from 'vitepress'

const { site } = useData()

// `npm run docs:build` writes the Pagefind bundle after VitePress has built
// the site. Under `docs:dev` the bundle does not exist, so search stays inert.
onMounted(() => {
  if (document.getElementById('pagefind-component-ui')) return
  const style = document.createElement('link')
  style.rel = 'stylesheet'
  style.href = withBase('/pagefind/pagefind-component-ui.css')
  const script = document.createElement('script')
  script.id = 'pagefind-component-ui'
  script.type = 'module'
  script.src = withBase('/pagefind/pagefind-component-ui.js')
  document.head.append(style, script)
})
</script>

<template>
  <!-- Pagefind cannot detect the bundle path of a script inserted at runtime
       and falls back to /pagefind/, which misses the site base. -->
  <pagefind-config :bundle-path="withBase('/pagefind/')" :base-url="site.base" />
  <pagefind-modal />
</template>
