<template>
  <div class="food-records">
    <el-container>
      <el-header>
        <h1>食物记录</h1>
      </el-header>
      <el-main>
        <el-button type="primary" @click="handleAdd">添加记录</el-button>
        <el-table :data="records" style="margin-top: 20px">
          <el-table-column prop="food_name" label="食物名称" />
          <el-table-column prop="intake_amount" label="摄入量(g)" />
          <el-table-column prop="calorie" label="热量(kcal)" />
          <el-table-column prop="intake_time" label="时间" />
        </el-table>
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'

const records = ref([])

onMounted(() => {
  loadRecords()
})

const loadRecords = async () => {
  try {
  } catch (error) {
    ElMessage.error('加载记录失败')
  }
}

const handleAdd = () => {
  ElMessage.info('添加记录功能开发中')
}
</script>

<style scoped>
.food-records {
  padding: 20px;
}
</style>
