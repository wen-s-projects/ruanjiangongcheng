<template>
  <div class="profile">
    <el-container>
      <el-header>
        <h1>个人资料</h1>
      </el-header>
      <el-main>
        <el-form :model="form" label-width="120px">
          <el-form-item label="用户名">
            <el-input v-model="form.username" disabled />
          </el-form-item>
          <el-form-item label="个人简介">
            <el-input v-model="form.introduction" type="textarea" :rows="4" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="handleSave">保存</el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'

const form = ref({
  username: '',
  introduction: ''
})

onMounted(() => {
  loadProfile()
})

const loadProfile = async () => {
  try {
    const authStore = useAuthStore()
    form.value.username = authStore.user?.username || ''
  } catch (error) {
    ElMessage.error('加载个人资料失败')
  }
}

const handleSave = async () => {
  try {
    ElMessage.success('保存成功')
  } catch (error) {
    ElMessage.error('保存失败')
  }
}
</script>

<style scoped>
.profile {
  padding: 20px;
}
</style>
