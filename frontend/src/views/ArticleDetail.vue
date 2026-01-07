<template>
  <div class="article-detail">
    <el-container>
      <el-header>
        <h1>{{ article?.title }}</h1>
      </el-header>
      <el-main>
        <div v-html="article?.rendered_html"></div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const article = ref(null)

onMounted(() => {
  loadArticle()
})

const loadArticle = async () => {
  try {
  } catch (error) {
  }
}
</script>

<style scoped>
.article-detail {
  padding: 20px;
}
</style>
