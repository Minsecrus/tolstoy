<script setup lang="ts">
import { nextTick, onBeforeUnmount, onMounted, ref } from 'vue'

const annotated = ref(false)

async function followAnchor() {
  const hash = decodeURIComponent(window.location.hash.slice(1))
  if (!hash || hash === 'VPContent') return
  annotated.value = !hash.startsWith('original-')
  await nextTick()
  document.getElementById(hash)?.scrollIntoView({ block: 'start' })
}

function chooseVersion(value: boolean) {
  annotated.value = value
  const hash = window.location.hash
  if (hash && hash !== '#VPContent') {
    window.history.replaceState(window.history.state, '', window.location.pathname + window.location.search)
  }
}

onMounted(() => {
  followAnchor()
  window.addEventListener('hashchange', followAnchor)
})

onBeforeUnmount(() => window.removeEventListener('hashchange', followAnchor))
</script>

<template>
  <div class="du-fu-poem">
    <div class="du-fu-version-tabs" role="tablist" aria-label="阅读版本" data-pagefind-ignore>
      <button
        id="du-fu-original-tab"
        role="tab"
        type="button"
        :aria-selected="!annotated"
        aria-controls="du-fu-original-panel"
        @click="chooseVersion(false)"
        @keydown.right.prevent="chooseVersion(true)"
      >只读原文</button>
      <button
        id="du-fu-annotated-tab"
        role="tab"
        type="button"
        :aria-selected="annotated"
        aria-controls="du-fu-annotated-panel"
        @click="chooseVersion(true)"
        @keydown.left.prevent="chooseVersion(false)"
      >原文与笺注</button>
    </div>
    <section
      v-show="!annotated"
      id="du-fu-original-panel"
      class="du-fu-original-panel"
      role="tabpanel"
      aria-labelledby="du-fu-original-tab"
      data-pagefind-ignore
    ><slot name="original" /></section>
    <section
      v-show="annotated"
      id="du-fu-annotated-panel"
      role="tabpanel"
      aria-labelledby="du-fu-annotated-tab"
    ><slot name="annotated" /></section>
  </div>
</template>

<style scoped>
.du-fu-version-tabs {
  display: flex;
  width: fit-content;
  gap: 4px;
  margin-bottom: 1.5rem;
  padding: 4px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
}

.du-fu-version-tabs button {
  padding: 6px 14px;
  border-radius: 5px;
  color: var(--vp-c-text-2);
  font-size: 14px;
  line-height: 1.6;
  cursor: pointer;
}

.du-fu-version-tabs button[aria-selected='true'] {
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg);
  box-shadow: 0 1px 3px rgb(0 0 0 / 8%);
}

.du-fu-version-tabs button:focus-visible {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 2px;
}

.du-fu-original-panel :deep(h1) {
  margin-top: 0;
}

.du-fu-poem :deep(.du-fu-poem-outline) {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1rem;
  margin-bottom: 1.5rem;
  font-size: 14px;
}

.du-fu-poem :deep(.du-fu-original-heading) {
  scroll-margin-top: 96px;
}
</style>
