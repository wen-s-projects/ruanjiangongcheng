<template>
  <div class="articles">
    <el-container>
      <el-header>
        <h1>文章列表</h1>
      </el-header>
      <el-main>
        <el-button type="primary" @click="handleCreate">写文章</el-button>
        <el-card v-for="article in articles" :key="article.id" style="margin-top: 20px">
          <template #header>
            <div>{{ article.title }}</div>
          </template>
          <div>{{ article.rendered_html }}</div>
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'

const articles = ref([])

onMounted(() => {
  loadArticles()
})

const loadArticles = async () => {
  try {
  } catch (error) {
    ElMessage.error('加载文章失败')
  }
}

const handleCreate = () => {
  ElMessage.info('写文章功能开发中')
}
</script>

<style scoped>
.articles {
  padding: 20px;
}
</style>
