<template>
  <div class="body-data">
    <el-container>
      <el-header>
        <h1>身体数据</h1>
      </el-header>
      <el-main>
        <el-form :model="form" label-width="120px">
          <el-form-item label="性别">
            <el-select v-model="form.gender" placeholder="请选择">
              <el-option label="男" :value="1" />
              <el-option label="女" :value="2" />
            </el-select>
          </el-form-item>
          <el-form-item label="年龄">
            <el-input-number v-model="form.age" :min="1" :max="120" />
          </el-form-item>
          <el-form-item label="身高(cm)">
            <el-input-number v-model="form.height" :min="50" :max="250" />
          </el-form-item>
          <el-form-item label="体重(kg)">
            <el-input-number v-model="form.weight" :min="20" :max="300" :precision="1" />
          </el-form-item>
          <el-form-item label="体脂率(%)">
            <el-input-number v-model="form.fat_rate" :min="0" :max="50" :precision="1" />
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
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const form = ref({
  gender: 1,
  age: 25,
  height: 170,
  weight: 65,
  fat_rate: 20
})

const handleSave = async () => {
  try {
    ElMessage.success('保存成功')
  } catch (error) {
    ElMessage.error('保存失败')
  }
}
</script>

<style scoped>
.body-data {
  padding: 20px;
}
</style>
