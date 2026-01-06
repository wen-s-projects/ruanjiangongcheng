# 卡卡前端项目

基于Vue 3 + TypeScript + Element Plus的卡路里管理系统前端。

## 技术栈

- Vue 3.5+
- TypeScript
- Vite
- Vue Router
- Pinia
- Element Plus
- Axios

## 项目结构

```
frontend/
├── src/
│   ├── api/          # API请求封装
│   ├── assets/       # 静态资源
│   ├── components/    # 公共组件
│   ├── router/       # 路由配置
│   ├── stores/       # 状态管理
│   ├── views/        # 页面组件
│   ├── App.vue       # 根组件
│   └── main.ts      # 应用入口
├── index.html
├── package.json
├── vite.config.ts
└── tsconfig.json
```

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 启动开发服务器

```bash
npm run dev
```

### 3. 构建生产版本

```bash
npm run build
```

### 4. 预览生产构建

```bash
npm run preview
```

## 功能特性

### 用户认证
- 用户注册
- 用户登录
- Token自动刷新
- 退出登录

### 用户管理
- 个人资料编辑
- 头像上传
- 背景图设置

### 身体数据
- BMI计算
- 基础代谢率计算
- 身体数据记录

### 食物记录
- 食物字典查询
- 食物摄入记录
- 每日热量统计
- AI识图功能

### 历史记录
- 日历视图
- 每日记录统计
- 月度汇总

### 文章系统
- 文章列表
- 文章详情
- 创建文章
- Markdown编辑
- 标签管理
- 评论功能

## 开发指南

### 代码规范

- 使用TypeScript类型注解
- 遵循Vue 3 Composition API最佳实践
- 使用Pinia进行状态管理
- 组件命名使用PascalCase
- 文件命名使用kebab-case

### 样式规范

- 使用scoped样式
- 避免使用!important
- 使用CSS变量管理主题色

### API调用

```typescript
import api from '@/api'

// GET请求
const response = await api.get('/users/')

// POST请求
const response = await api.post('/auth/login/', { username, password })

// PUT请求
const response = await api.put(`/users/${id}/`, data)

// DELETE请求
const response = await api.delete(`/users/${id}/`)
```

### 状态管理

```typescript
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()

// 访问状态
console.log(authStore.user)
console.log(authStore.isAuthenticated)

// 调用方法
await authStore.login(username, password)
await authStore.logout()
```

## 部署

### 环境变量

创建`.env.production`文件：

```
VITE_API_BASE_URL=https://api.example.com
```

### 构建和部署

```bash
npm run build
# 将dist目录部署到服务器
```

## 浏览器支持

- Chrome >= 87
- Firefox >= 78
- Safari >= 14
- Edge >= 88

## 许可证

MIT
