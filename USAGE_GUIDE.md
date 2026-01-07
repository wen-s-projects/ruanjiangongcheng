# 🚀 卡卡项目使用指南

## 📋 前置要求

在开始之前，请确保已安装以下软件：

### 必需软件
- **Python 3.9+** - 后端运行环境
- **Node.js 18+** - 前端运行环境
- **npm 10+** - 前端包管理器

### 可选软件
- **MySQL 8.0+** - 生产数据库（开发环境可使用SQLite）
- **Redis 7+** - 缓存服务
- **MinIO** - 对象存储（开发环境可使用本地存储）
- **Docker & Docker Compose** - 容器化部署

---

## 🎯 快速开始（开发环境）

### 方式一：使用SQLite（最简单，推荐初学者）

#### 1. 启动后端

打开命令行，进入后端目录：

```bash
cd backend/calorie_backend
```

创建并激活虚拟环境（推荐）：

```bash
python -m venv venv
venv\Scripts\activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

执行数据库迁移（自动创建SQLite数据库）：

```bash
py manage.py migrate
```

启动开发服务器：

```bash
py manage.py runserver
```

✅ **成功标志**：看到类似输出：
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 06, 2026 - 10:00:00
Django version 4.2.27, using settings 'calorie_backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

#### 2. 启动前端

打开新的命令行窗口，进入前端目录：

```bash
cd frontend
```

安装依赖：

```bash
npm install
```

启动开发服务器：

```bash
npm run dev
```

✅ **成功标志**：看到类似输出：
```
  VITE v6.0.3  ready in 500 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

#### 3. 访问应用

打开浏览器，访问：

- **前端应用**：http://localhost:5173
- **后端API**：http://localhost:8000
- **Django Admin**：http://localhost:8000/admin

---

### 方式二：使用MySQL（生产环境）

#### 1. 启动MySQL服务

**使用Docker（推荐）**：

```bash
docker-compose up -d mysql
```

**或使用本地MySQL**：

确保MySQL服务正在运行，并创建数据库：

```sql
CREATE DATABASE CalorieSystem CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 2. 配置数据库连接

编辑 `backend/calorie_backend/.env` 文件：

```env
# 数据库配置
DB_NAME=CalorieSystem
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

#### 3. 初始化数据库

执行数据库初始化脚本：

```bash
docker exec -i calorie_mysql mysql -uroot -pyourpassword CalorieSystem < scripts/init_database.sql
```

#### 4. 启动后端和前端

同方式一的步骤1和2。

---

## 📱 使用指南

### 1. 用户注册

1. 打开浏览器访问 http://localhost:5173
2. 点击"还没有账号？立即注册"
3. 填写用户名和密码
4. 点击"注册"按钮
5. 注册成功后自动跳转到Dashboard

### 2. 用户登录

1. 在登录页面输入用户名和密码
2. 点击"登录"按钮
3. 登录成功后跳转到Dashboard

### 3. 查看Dashboard

Dashboard显示：
- 今日摄入热量
- 基础代谢率（BMR）
- BMI指数
- 今日记录次数
- 快速操作按钮

### 4. 记录食物

1. 点击"记录食物"按钮
2. 选择食物（从字典搜索或手动输入）
3. 输入摄入量（克）
4. 选择餐次类型（早餐/午餐/晚餐/加餐）
5. 点击"保存"

### 5. 查看历史记录

1. 点击侧边栏"历史记录"
2. 查看日历视图
3. 点击日期查看详细记录
4. 查看每日热量汇总

### 6. 写文章

1. 点击"写文章"按钮
2. 填写标题
3. 使用Markdown编写内容
4. 添加标签
5. 点击"发布"

---

## 🔧 开发指南

### 后端开发

#### 创建新的API端点

1. 在对应app的`views.py`中添加视图函数
2. 在`urls.py`中注册路由
3. 在`serializers.py`中添加序列化器（如需要）
4. 在`models.py`中添加模型（如需要）

#### 运行测试

```bash
py manage.py test
```

#### 创建超级用户

```bash
py manage.py createsuperuser
```

### 前端开发

#### 创建新页面

1. 在`src/views/`中创建Vue组件
2. 在`src/router/index.ts`中注册路由
3. 在侧边栏添加导航链接

#### 创建API调用

在`src/api/`中创建API函数：

```typescript
import api from './index'

export async function getUserData() {
  const response = await api.get('/users/me/')
  return response.data
}
```

---

## 🐛 常见问题

### 问题1：Python命令找不到

**错误**：`'py' 不是内部或外部命令`

**解决**：
- 使用 `python` 代替 `py`
- 或将Python添加到系统PATH

### 问题2：npm install失败

**错误**：网络错误或依赖冲突

**解决**：
```bash
# 清除缓存
npm cache clean --force

# 使用淘宝镜像
npm config set registry https://registry.npmmirror.com

# 重新安装
npm install
```

### 问题3：数据库迁移失败

**错误**：`django.db.backends.mysql` 相关错误

**解决**：
- 检查MySQL服务是否运行
- 检查`.env`文件中的数据库配置
- 或使用SQLite作为开发数据库

### 问题4：端口被占用

**错误**：`Address already in use`

**解决**：
```bash
# Windows查找占用端口的进程
netstat -ano | findstr :8000

# 结束进程
taskkill /PID <进程ID> /F
```

### 问题5：CORS错误

**错误**：浏览器控制台显示跨域错误

**解决**：
- 检查后端`settings.py`中的`CORS_ALLOWED_ORIGINS`配置
- 确保前端URL在允许列表中

---

## 📊 API测试

### 使用curl测试

#### 用户注册

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

#### 用户登录

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

#### 获取食物列表

```bash
curl http://localhost:8000/api/foods/
```

### 使用Postman测试

1. 下载并安装Postman
2. 导入API端点
3. 设置请求头：`Content-Type: application/json`
4. 发送请求查看响应

---

## 🚀 生产部署

### 1. 构建前端

```bash
cd frontend
npm run build
```

生成的文件在`frontend/dist/`目录

### 2. 配置生产环境变量

编辑`backend/calorie_backend/.env`：

```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-production-secret-key
DB_NAME=CalorieSystem
DB_USER=production_user
DB_PASSWORD=strong_password
DB_HOST=production-db-host
DB_PORT=3306
```

### 3. 收集静态文件

```bash
cd backend/calorie_backend
py manage.py collectstatic
```

### 4. 使用Gunicorn运行

```bash
pip install gunicorn
gunicorn calorie_backend.wsgi:application --bind 0.0.0.0:8000
```

### 5. 配置Nginx

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # 前端静态文件
    location / {
        root /path/to/frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # 后端API
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # 静态文件
    location /static/ {
        alias /path/to/backend/calorie_backend/staticfiles/;
    }

    # 媒体文件
    location /media/ {
        alias /path/to/backend/calorie_backend/media/;
    }
}
```

---

## 📚 相关文档

- [项目完善总结](./PROJECT_COMPLETION_SUMMARY.md)
- [后端README](./backend/calorie_backend/README.md)
- [前端README](./frontend/README.md)
- [需求文档](./Requirements/SRS.md)
- [数据库设计](./Design/Database_Schema.md)

---

## 💡 提示

1. **开发环境推荐使用SQLite**，无需额外配置
2. **生产环境必须使用MySQL**，并配置强密码
3. **定期备份数据库**，防止数据丢失
4. **使用Git进行版本控制**，方便回滚
5. **编写单元测试**，确保代码质量
6. **使用环境变量管理敏感信息**，不要提交到代码仓库

---

## 🆘 获取帮助

遇到问题？

1. 查看日志文件：`backend/calorie_backend/logs/django.log`
2. 查看Django文档：https://docs.djangoproject.com/
3. 查看Vue文档：https://vuejs.org/
4. 查看Element Plus文档：https://element-plus.org/

---

**祝您使用愉快！** 🎉
