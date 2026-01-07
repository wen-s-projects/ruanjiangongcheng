<template>
  <div class="history">
    <el-container>
      <el-header>
        <h1>历史记录</h1>
      </el-header>
      <el-main>
        <el-calendar v-model="selectedDate" />
      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const selectedDate = ref(new Date())
</script>

<style scoped>
.history {
  padding: 20px;
}
</style>
