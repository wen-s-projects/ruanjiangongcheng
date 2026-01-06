@echo off
echo ========================================
echo 卡卡项目 - 快速启动脚本
echo ========================================
echo.

echo [1] 启动数据库和基础设施 (MySQL, Redis, MinIO)
echo [2] 初始化数据库
echo [3] 启动后端服务器
echo [4] 启动前端开发服务器
echo [5] 全部启动
echo [0] 退出
echo.

set /p choice=请选择操作:

if "%choice%"=="1" goto start_infra
if "%choice%"=="2" goto init_db
if "%choice%"=="3" goto start_backend
if "%choice%"=="4" goto start_frontend
if "%choice%"=="5" goto start_all
if "%choice%"=="0" goto exit

:start_infra
echo.
echo 正在启动基础设施...
docker-compose up -d mysql redis minio
echo.
echo 基础设施已启动！
echo MySQL: localhost:3306
echo Redis: localhost:6379
echo MinIO: http://localhost:9000 (minioadmin/minioadmin)
goto menu

:init_db
echo.
echo 正在初始化数据库...
docker exec -i calorie_mysql mysql -uroot -prootpassword CalorieSystem < scripts\init_database.sql
echo.
echo 数据库初始化完成！
goto menu

:start_backend
echo.
echo 正在启动后端服务器...
cd backend\calorie_backend
if not exist .env (
    echo 警告: .env文件不存在，正在从.env.example创建...
    copy .env.example .env
    echo 请编辑.env文件配置数据库连接信息后重试
    goto menu
)
py manage.py migrate
py manage.py runserver
goto menu

:start_frontend
echo.
echo 正在启动前端开发服务器...
cd frontend
if not exist node_modules (
    echo 正在安装前端依赖...
    call npm install
)
call npm run dev
goto menu

:start_all
echo.
echo 正在启动所有服务...
docker-compose up -d
timeout /t 5 /nobreak
cd backend\calorie_backend
if not exist .env (
    copy .env.example .env
)
py manage.py migrate
start cmd /k "py manage.py runserver"
cd ..\..
cd frontend
if not exist node_modules (
    call npm install
)
start cmd /k "npm run dev"
echo.
echo 所有服务已启动！
echo 后端: http://localhost:8000
echo 前端: http://localhost:5173
echo.
goto menu

:menu
echo.
pause
cls
goto start

:exit
echo.
echo 再见！
pause
