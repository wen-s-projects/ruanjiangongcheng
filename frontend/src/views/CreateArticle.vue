<template>
  <div class="create-article">
    <el-container>
      <el-header>
        <h1>写文章</h1>
      </el-header>
      <el-main>
        <el-form :model="form" label-width="120px">
          <el-form-item label="标题">
            <el-input v-model="form.title" />
          </el-form-item>
          <el-form-item label="内容">
            <el-input v-model="form.markdown" type="textarea" :rows="10" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="handlePublish">发布</el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const form = ref({
  title: '',
  markdown: ''
})

const handlePublish = async () => {
  try {
    ElMessage.success('发布成功')
  } catch (error) {
    ElMessage.error('发布失败')
  }
}
</script>

<style scoped>
.create-article {
  padding: 20px;
}
</style>
