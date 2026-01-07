# 卡卡项目 - 简化启动脚本

Write-Host "========================================"
Write-Host "卡卡项目 - 启动菜单"
Write-Host "========================================"
Write-Host ""

Write-Host "[1] 启动后端（Django）"
Write-Host "[2] 启动前端（Vue）"
Write-Host "[3] 全部启动"
Write-Host "[0] 退出"
Write-Host ""

$choice = Read-Host "请选择操作: "

switch ($choice) {
    "1" { Start-Backend }
    "2" { Start-Frontend }
    "3" { Start-All }
    "0" { Exit-Script }
    default { Write-Host "无效选择"; Exit-Script }
}

function Start-Backend {
    Write-Host ""
    Write-Host "========================================"
    Write-Host "启动后端服务器..."
    Write-Host "========================================"
    Write-Host ""
    
    $backendDir = "backend\calorie_backend"
    
    if (-not (Test-Path "$backendDir")) {
        Write-Host "错误: 后端目录不存在: $backendDir" -ForegroundColor Red
        return
    }
    
    Set-Location $backendDir
    
    # 检查虚拟环境
    if (-not (Test-Path "venv")) {
        Write-Host "[1/4] 创建Python虚拟环境..." -ForegroundColor Cyan
        python -m venv venv
    }
    
    # 激活虚拟环境
    Write-Host "[2/4] 激活虚拟环境..." -ForegroundColor Cyan
    & .\venv\Scripts\Activate.ps1
    
    # 安装依赖
    Write-Host "[3/4] 安装依赖..." -ForegroundColor Cyan
    pip install -r requirements.txt -q
    
    # 执行数据库迁移
    Write-Host "[4/4] 执行数据库迁移..." -ForegroundColor Cyan
    python manage.py migrate
    
    # 启动服务器
    Write-Host ""
    Write-Host "========================================"
    Write-Host "后端服务器启动成功！"
    Write-Host "========================================"
    Write-Host ""
    Write-Host "后端API: http://localhost:8000" -ForegroundColor Green
    Write-Host "Django Admin: http://localhost:8000/admin" -ForegroundColor Green
    Write-Host ""
    Write-Host "按 Ctrl+C 停止服务器" -ForegroundColor Yellow
    Write-Host ""
    
    python manage.py runserver
}

function Start-Frontend {
    Write-Host ""
    Write-Host "========================================"
    Write-Host "启动前端开发服务器..."
    Write-Host "========================================"
    Write-Host ""
    
    $frontendDir = "frontend"
    
    if (-not (Test-Path "$frontendDir")) {
        Write-Host "错误: 前端目录不存在: $frontendDir" -ForegroundColor Red
        return
    }
    
    Set-Location $frontendDir
    
    # 检查node_modules
    if (-not (Test-Path "node_modules")) {
        Write-Host "[1/2] 安装前端依赖..." -ForegroundColor Cyan
        npm install
    }
    
    # 启动开发服务器
    Write-Host "[2/2] 启动开发服务器..." -ForegroundColor Cyan
    Write-Host ""
    Write-Host "========================================"
    Write-Host "前端服务器启动成功！"
    Write-Host "========================================"
    Write-Host ""
    Write-Host "前端应用: http://localhost:5173" -ForegroundColor Green
    Write-Host ""
    Write-Host "按 Ctrl+C 停止服务器" -ForegroundColor Yellow
    Write-Host ""
    
    npm run dev
}

function Start-All {
    Write-Host ""
    Write-Host "========================================"
    Write-Host "启动所有服务..."
    Write-Host "========================================"
    Write-Host ""
    
    # 启动后端（在新窗口）
    $backendScript = {
        Start-Backend
    }
    
    Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", $backendScript -NoNewWindow
    
    # 等待3秒
    Start-Sleep -Seconds 3
    
    # 启动前端
    Start-Frontend
}

function Exit-Script {
    Write-Host ""
    Write-Host "再见！" -ForegroundColor Green
    Write-Host ""
    exit
}
