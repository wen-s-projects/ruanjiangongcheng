<template>
  <div class="dashboard-container">
    <el-container>
      <el-header>
        <div class="header-content">
          <h1>卡卡 - 卡路里管理系统</h1>
          <div class="user-info">
            <span>{{ authStore.user?.username }}</span>
            <el-button type="danger" @click="handleLogout">退出</el-button>
          </div>
        </div>
      </el-header>
      
      <el-container>
        <el-aside width="200px">
          <el-menu
            :default-active="activeMenu"
            router
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
          >
            <el-menu-item index="/dashboard">
              <el-icon><HomeFilled /></el-icon>
              <span>首页</span>
            </el-menu-item>
            <el-menu-item index="/profile">
              <el-icon><User /></el-icon>
              <span>个人资料</span>
            </el-menu-item>
            <el-menu-item index="/body-data">
              <el-icon><DataAnalysis /></el-icon>
              <span>身体数据</span>
            </el-menu-item>
            <el-menu-item index="/food-records">
              <el-icon><Food /></el-icon>
              <span>食物记录</span>
            </el-menu-item>
            <el-menu-item index="/history">
              <el-icon><Calendar /></el-icon>
              <span>历史记录</span>
            </el-menu-item>
            <el-menu-item index="/articles">
              <el-icon><Document /></el-icon>
              <span>文章</span>
            </el-menu-item>
            <el-menu-item index="/create-article">
              <el-icon><Edit /></el-icon>
              <span>写文章</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        
        <el-main>
          <div class="dashboard-content">
            <el-row :gutter="20">
              <el-col :span="6">
                <el-card class="stat-card">
                  <el-statistic title="今日摄入" :value="todayCalories" suffix="kcal" />
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card class="stat-card">
                  <el-statistic title="基础代谢" :value="bmr" suffix="kcal" />
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card class="stat-card">
                  <el-statistic title="BMI" :value="bmi" :precision="1" />
                </el-card>
              </el-col>
              <el-col :span="6">
                <el-card class="stat-card">
                  <el-statistic title="今日记录" :value="todayRecords" suffix="次" />
                </el-card>
              </el-col>
            </el-row>
            
            <el-divider />
            
            <h2>快速操作</h2>
            <el-row :gutter="20">
              <el-col :span="12">
                <el-button type="primary" size="large" @click="$router.push('/food-records')" style="width: 100%">
                  <el-icon><Plus /></el-icon>
                  记录食物
                </el-button>
              </el-col>
              <el-col :span="12">
                <el-button type="success" size="large" @click="$router.push('/create-article')" style="width: 100%">
                  <el-icon><Edit /></el-icon>
                  写文章
                </el-button>
              </el-col>
            </el-row>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { HomeFilled, User, DataAnalysis, Food, Calendar, Document, Edit, Plus } from '@element-plus/icons-vue'

const route = useRoute()
const authStore = useAuthStore()

const activeMenu = computed(() => route.path)
const todayCalories = ref(0)
const bmr = ref(0)
const bmi = ref(0)
const todayRecords = ref(0)

onMounted(async () => {
  await loadDashboardData()
})

async function loadDashboardData() {
  try {
    const today = new Date().toISOString().split('T')[0]
    const response = await fetch(`/api/food-records/daily_summary/?date=${today}`)
    const data = await response.json()
    
    todayCalories.value = data.total_calories || 0
    todayRecords.value = data.record_count || 0
  } catch (error) {
    console.error('加载仪表板数据失败:', error)
  }
}

async function handleLogout() {
  await authStore.logout()
  window.location.href = '/login'
}
</script>

<style scoped>
.dashboard-container {
  height: 100vh;
}

.el-header {
  background-color: #545c64;
  color: #fff;
  line-height: 60px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-content h1 {
  margin: 0;
  font-size: 20px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 20px;
}

.el-aside {
  background-color: #545c64;
  color: #fff;
}

.el-main {
  background-color: #f0f2f5;
  padding: 20px;
}

.dashboard-content {
  max-width: 1200px;
  margin: 0 auto;
}

.stat-card {
  margin-bottom: 20px;
}

.el-divider {
  margin: 30px 0;
}

h2 {
  margin-bottom: 20px;
  color: #333;
}
</style>
