# 卡卡后端项目

基于Django REST Framework的卡路里管理系统后端。

## 技术栈

- Python 3.9+
- Django 4.2
- Django REST Framework
- MySQL
- JWT认证
- S3兼容对象存储（MinIO）

## 项目结构

```
calorie_backend/
├── apps/
│   ├── auth/          # 认证授权模块
│   ├── users/         # 用户管理模块
│   ├── articles/      # 文章管理模块
│   ├── uploads/       # 文件上传模块
│   └── markdown/      # Markdown处理模块
├── calorie_backend/    # 项目配置
├── manage.py
├── requirements.txt
└── .env.example
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 编辑.env文件，配置数据库和S3等信息
```

### 3. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 创建超级用户

```bash
python manage.py createsuperuser
```

### 5. 启动开发服务器

```bash
python manage.py runserver
```

## API文档

### 认证相关

- POST /api/auth/register/ - 用户注册
- POST /api/auth/login/ - 用户登录
- POST /api/auth/refresh/ - 刷新Token

### 用户管理

- GET /api/users/ - 用户列表
- GET /api/users/me/ - 当前用户信息
- PUT /api/users/:id/update_profile/ - 更新用户资料

### 身体数据

- GET /api/body-data/ - 身体数据列表
- POST /api/body-data/ - 创建身体数据
- POST /api/body-data/calculate_bmi/ - 计算BMI
- POST /api/body-data/calculate_bmr/ - 计算基础代谢率

### 食物管理

- GET /api/foods/ - 食物字典
- GET /api/foods/search/?q=关键词 - 搜索食物
- POST /api/food-records/ - 创建食物摄入记录
- GET /api/food-records/daily_summary/?date=日期 - 每日热量汇总

### 文章管理

- GET /api/articles/ - 文章列表
- GET /api/articles/:slug/ - 文章详情
- POST /api/articles/ - 创建文章
- PUT /api/articles/:slug/ - 更新文章
- DELETE /api/articles/:slug/ - 删除文章

### 标签管理

- GET /api/tags/ - 标签列表
- GET /api/tags/:id/articles/ - 标签下的文章

### 评论管理

- GET /api/comments/ - 评论列表
- POST /api/comments/ - 创建评论

### 文件上传

- POST /api/uploads/presigned/ - 获取预签名上传URL
- POST /api/uploads/complete/ - 完成上传并生成缩略图

### Markdown预览

- POST /api/markdown/preview/ - Markdown渲染预览

## 开发指南

### 代码规范

- 遵循PEP 8代码风格
- 使用类型注解
- 编写单元测试
- API文档使用中文

### 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 运行测试

```bash
python manage.py test
```

## 部署

### Docker部署

```bash
docker-compose up -d
```

### 生产环境配置

1. 设置DEBUG=False
2. 配置ALLOWED_HOSTS
3. 使用生产级数据库
4. 配置HTTPS
5. 配置日志和监控

## 许可证

MIT
