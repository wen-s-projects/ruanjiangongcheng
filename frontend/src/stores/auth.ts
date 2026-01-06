import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

interface User {
  id: number
  username: string
  photo?: string
  background?: string
  introduction?: string
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const accessToken = ref<string | null>(localStorage.getItem('access_token'))
  const refreshToken = ref<string | null>(localStorage.getItem('refresh_token'))

  const isAuthenticated = computed(() => !!accessToken.value && !!user.value)

  async function login(username: string, password: string) {
    try {
      const response = await axios.post('/api/auth/login/', { username, password })
      const { user: userData, tokens } = response.data
      
      user.value = userData
      accessToken.value = tokens.access_token
      refreshToken.value = tokens.refresh_token
      
      localStorage.setItem('access_token', tokens.access_token)
      localStorage.setItem('refresh_token', tokens.refresh_token)
      
      return true
    } catch (error) {
      console.error('登录失败:', error)
      return false
    }
  }

  async function register(username: string, password: string) {
    try {
      const response = await axios.post('/api/auth/register/', { username, password })
      const { user: userData, tokens } = response.data
      
      user.value = userData
      accessToken.value = tokens.access_token
      refreshToken.value = tokens.refresh_token
      
      localStorage.setItem('access_token', tokens.access_token)
      localStorage.setItem('refresh_token', tokens.refresh_token)
      
      return true
    } catch (error) {
      console.error('注册失败:', error)
      return false
    }
  }

  async function logout() {
    user.value = null
    accessToken.value = null
    refreshToken.value = null
    
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
  }

  async function refreshAccessToken() {
    try {
      const response = await axios.post('/api/auth/refresh/', {
        refresh_token: refreshToken.value,
      })
      const tokens = response.data
      
      accessToken.value = tokens.access_token
      localStorage.setItem('access_token', tokens.access_token)
      
      return true
    } catch (error) {
      console.error('刷新token失败:', error)
      await logout()
      return false
    }
  }

  return {
    user,
    accessToken,
    refreshToken,
    isAuthenticated,
    login,
    register,
    logout,
    refreshAccessToken,
  }
})
