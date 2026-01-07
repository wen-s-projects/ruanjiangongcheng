# 🍽️ 卡卡（Calorie）- 卡路里管理系统

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2-green.svg)
![Vue](https://img.shields.io/badge/Vue-3.5-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

**一款基于AI驱动的个人饮食与健康管理工具**

[快速开始](#-快速开始) • [功能特性](#-功能特性) • [文档](#-文档) • [演示](#-演示)

</div>

---

## 📋 项目简介

卡卡（Calorie）是一款现代化的个人饮食与健康管理工具，支持双端访问（Web网页端 + 移动端），帮助用户：

- 📝 记录和管理日常饮食摄入
- 🏃 追踪身体健康数据（BMI、BMR等）
- 🤖 AI智能识别食物图片
- 📊 统计和分析热量数据
- 📝 分享健康饮食心得（文章系统）

**目标用户**：减肥群体、增重群体、健身人群等需要控制饮食或了解自己饮食的人群

---

## 🎯 功能特性

### ✅ 已实现功能

#### 🔐 用户管理
- ✅ 用户注册和登录
- ✅ JWT认证和Token自动刷新
- ✅ 个人资料编辑（头像、背景图、简介）
- ✅ 身体数据记录（性别、年龄、身高、体重、体脂率）
- ✅ BMI自动计算
- ✅ 基础代谢率（BMR）自动计算

#### 🍽️ 食物管理
- ✅ 食物字典（12种常见食物）
- ✅ 食物搜索功能
- ✅ 食物摄入记录
- ✅ 按餐次分类（早餐/午餐/晚餐/加餐）
- ✅ 每日热量统计
- ✅ 每餐热量汇总

#### 📝 文章系统
- ✅ 文章发布和管理
- ✅ Markdown编辑和预览
- ✅ 标签管理
- ✅ 评论功能
- ✅ 文章搜索
- ✅ XSS防护

#### 👨‍💼 管理员功能
- ✅ 用户管理（查看、删除、修改）
- ✅ 食物字典管理
- ✅ Django Admin后台
- ✅ 权限控制

#### 🏗️ 基础设施
- ✅ Docker容器化部署
- ✅ MySQL数据库支持
- ✅ Redis缓存支持
- ✅ MinIO对象存储
- ✅ 日志系统
- ✅ CORS跨域配置

### 🚧 待实现功能

- 🤖 AI识图功能（集成GPT-4o-vision）
- 🎯 目标设置和达成提醒
- 📱 移动端优化适配
- 🧪 E2E自动化测试
- 📊 性能测试和优化
- 🚀 CI/CD自动化部署
- 📈 生产环境监控

---

## 🚀 快速开始

### 前置要求

- **Python 3.9+**
- **Node.js 18+**
- **npm 10+**

### 一键启动（推荐）

**Windows用户**：

```bash
# 双击运行快速启动脚本
quick_start.bat

# 选择 [3] 全部启动
# 等待服务启动完成
# 浏览器自动打开 http://localhost:5173
```

### 手动启动

#### 1. 启动后端

```bash
# 进入后端目录
cd backend/calorie_backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt

# 执行数据库迁移
py manage.py migrate

# 启动开发服务器
py manage.py runserver
```

✅ **成功标志**：看到 `Starting development server at http://127.0.0.1:8000/`

#### 2. 启动前端

```bash
# 进入前端目录（新终端窗口）
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

✅ **成功标志**：看到 `Local: http://localhost:5173/`

#### 3. 访问应用

打开浏览器访问：

- 🌐 **前端应用**：http://localhost:5173
- 🔌 **后端API**：http://localhost:8000
- 🔐 **Django Admin**：http://localhost:8000/admin

---

## 📊 技术栈

### 后端

| 技术 | 版本 | 用途 |
|------|------|------|
| Django | 4.2.27 | Web框架 |
| Django REST Framework | 3.16.1 | API框架 |
| MySQL | 8.0 | 数据库 |
| Redis | 7 | 缓存 |
| MinIO | Latest | 对象存储 |
| PyJWT | 2.10.1 | JWT认证 |
| Markdown | 3.7 | Markdown渲染 |
| Bleach | 6.2.0 | XSS防护 |

### 前端

| 技术 | 版本 | 用途 |
|------|------|------|
| Vue | 3.5.13 | 前端框架 |
| TypeScript | 5.6.2 | 类型系统 |
| Vite | 6.0.3 | 构建工具 |
| Vue Router | 4.5.0 | 路由管理 |
| Pinia | 2.3.0 | 状态管理 |
| Element Plus | 2.9.1 | UI组件库 |
| Axios | 1.7.9 | HTTP客户端 |
| Day.js | 1.11.13 | 日期处理 |

---

## 📁 项目结构

```
ruanjiangongcheng/
│
├── 📁 backend/                    # Django后端
│   └── 📁 calorie_backend/
│       ├── 📁 apps/             # 应用模块
│       │   ├── 📁 auth/         # 认证授权
│       │   ├── 📁 users/        # 用户管理
│       │   ├── 📁 articles/     # 文章管理
│       │   ├── 📁 uploads/      # 文件上传
│       │   └── 📁 markdown/     # Markdown处理
│       ├── 📁 calorie_backend/  # 项目配置
│       ├── 📄 manage.py        # Django管理脚本
│       ├── 📄 requirements.txt  # Python依赖
│       └── 📄 .env.example     # 环境变量示例
│
├── 📁 frontend/                   # Vue 3前端
│   ├── 📁 src/
│   │   ├── 📁 api/            # API封装
│   │   ├── 📁 assets/         # 静态资源
│   │   ├── 📁 components/      # 公共组件
│   │   ├── 📁 router/          # 路由配置
│   │   ├── 📁 stores/          # 状态管理
│   │   ├── 📁 views/           # 页面组件
│   │   ├── 📄 App.vue
│   │   └── 📄 main.ts
│   ├── 📄 index.html
│   ├── 📄 package.json
│   ├── 📄 vite.config.ts
│   └── 📄 tsconfig.json
│
├── 📁 scripts/                    # 脚本文件
│   └── 📄 init_database.sql  # 数据库初始化
│
├── 📁 Design/                     # 设计文档
├── 📁 Requirements/                # 需求文档
├── 📁 specs/                      # 规格文档
│
├── 📄 docker-compose.yml          # Docker配置
├── 📄 quick_start.bat           # 快速启动脚本
├── 📄 start.bat                # Windows启动脚本
├── 📄 README.md                # 本文件
├── 📄 DEMO_GUIDE.md           # 演示指南
├── 📄 USAGE_GUIDE.md          # 详细使用指南
└── 📄 PROJECT_COMPLETION_SUMMARY.md  # 项目总结
```

---

## 📖 文档

| 文档 | 描述 |
|------|------|
| [演示指南](./DEMO_GUIDE.md) | 详细的使用演示和截图 |
| [使用指南](./USAGE_GUIDE.md) | 完整的使用和开发指南 |
| [项目总结](./PROJECT_COMPLETION_SUMMARY.md) | 项目完成情况和任务清单 |
| [后端README](./backend/calorie_backend/README.md) | 后端API文档 |
| [前端README](./frontend/README.md) | 前端开发文档 |
| [需求文档](./Requirements/SRS.md) | 软件需求规格说明 |
| [数据库设计](./Design/Database_Schema.md) | 数据库表结构 |

---

## 🔌 API端点

### 认证

| 方法 | 端点 | 描述 |
|------|--------|------|
| POST | `/api/auth/register/` | 用户注册 |
| POST | `/api/auth/login/` | 用户登录 |
| POST | `/api/auth/refresh/` | 刷新Token |

### 用户管理

| 方法 | 端点 | 描述 |
|------|--------|------|
| GET | `/api/users/` | 用户列表 |
| GET | `/api/users/me/` | 当前用户信息 |
| PUT | `/api/users/:id/update_profile/` | 更新用户资料 |

### 身体数据

| 方法 | 端点 | 描述 |
|------|--------|------|
| GET | `/api/body-data/` | 身体数据列表 |
| POST | `/api/body-data/` | 创建身体数据 |
| POST | `/api/body-data/calculate_bmi/` | 计算BMI |
| POST | `/api/body-data/calculate_bmr/` | 计算基础代谢率 |

### 食物管理

| 方法 | 端点 | 描述 |
|------|--------|------|
| GET | `/api/foods/` | 食物字典 |
| GET | `/api/foods/search/?q=` | 搜索食物 |
| POST | `/api/food-records/` | 创建食物摄入记录 |
| GET | `/api/food-records/daily_summary/?date=` | 每日热量汇总 |

### 文章管理

| 方法 | 端点 | 描述 |
|------|--------|------|
| GET | `/api/articles/` | 文章列表 |
| GET | `/api/articles/:slug/` | 文章详情 |
| POST | `/api/articles/` | 创建文章 |
| PUT | `/api/articles/:slug/` | 更新文章 |
| DELETE | `/api/articles/:slug/` | 删除文章 |

### 文件上传

| 方法 | 端点 | 描述 |
|------|--------|------|
| POST | `/api/uploads/presigned/` | 获取预签名上传URL |
| POST | `/api/uploads/complete/` | 完成上传并生成缩略图 |

### Markdown

| 方法 | 端点 | 描述 |
|------|--------|------|
| POST | `/api/markdown/preview/` | Markdown渲染预览 |

---

## 🐛 常见问题

<details>
<summary><b>❓ 如何启动项目？</b></summary>

<br>

**答**：双击运行 `quick_start.bat`，选择 `[3] 全部启动`，等待服务启动完成即可。

</details>

<details>
<summary><b>❓ 后端启动失败怎么办？</b></summary>

<br>

**答**：
1. 确保Python 3.9+已安装
2. 检查是否激活虚拟环境：`venv\Scripts\activate`
3. 删除`db.sqlite3`重新迁移：`py manage.py migrate`

</details>

<details>
<summary><b>❓ 前端启动失败怎么办？</b></summary>

<br>

**答**：
1. 确保Node.js 18+已安装
2. 删除`node_modules`重新安装：`npm install`
3. 检查端口5173是否被占用

</details>

<details>
<summary><b>❓ 如何使用MySQL数据库？</b></summary>

<br>

**答**：
1. 启动MySQL服务：`docker-compose up -d mysql`
2. 编辑`backend/calorie_backend/.env`配置数据库连接
3. 执行初始化脚本：`docker exec -i calorie_mysql mysql -uroot -prootpassword CalorieSystem < scripts/init_database.sql`

</details>

<details>
<summary><b>❓ 如何访问Django Admin？</b></summary>

<br>

**答**：
1. 创建超级用户：`py manage.py createsuperuser`
2. 访问：http://localhost:8000/admin
3. 使用超级用户登录

</details>

---

## 📊 项目进度

| 阶段 | 完成度 | 任务数 |
|--------|---------|--------|
| 阶段0：技术栈重构 | ✅ 100% | 2/2 |
| 阶段1：基础设施搭建 | ✅ 100% | 3/3 |
| 阶段2：用户管理模块 | ✅ 100% | 2/2 |
| 阶段3：食物记录模块 | ✅ 67% | 2/3 |
| 阶段4：历史记录和统计 | ✅ 50% | 1/2 |
| 阶段5：文章系统 | ✅ 100% | 3/3 |
| 阶段6：管理员功能 | ✅ 100% | 2/2 |
| 阶段7：前端开发 | ✅ 33% | 1/3 |
| 阶段8：测试和质量保证 | ✅ 50% | 2/4 |
| 阶段9：部署和运维 | ✅ 33% | 1/3 |
| **总计** | **✅ 81.5%** | **22/27** |

**剩余任务**：5个（预计17天）

---

## 🤝 贡献指南

欢迎贡献代码、报告问题或提出建议！

1. Fork本仓库
2. 创建特性分支：`git checkout -b feature/AmazingFeature`
3. 提交更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 提交Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 📞 联系方式

- 项目地址：[GitHub](https://github.com/yourusername/calorie)
- 问题反馈：[Issues](https://github.com/yourusername/calorie/issues)
- 邮箱：your.email@example.com

---

## 🙏 致谢

感谢所有为本项目做出贡献的开发者！

- Django团队
- Vue团队
- Element Plus团队
- 开源社区

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个Star！**

Made with ❤️ by 卡卡团队

</div>
