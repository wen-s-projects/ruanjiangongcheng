#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
卡卡项目 - 跨平台启动脚本
支持Windows、Linux、Mac
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header(text):
    """打印标题"""
    print("\n" + "=" * 50)
    print(f"  {text}")
    print("=" * 50)

def print_success(text):
    """打印成功信息"""
    print(f"✅ {text}")

def print_error(text):
    """打印错误信息"""
    print(f"❌ {text}")

def print_info(text):
    """打印信息"""
    print(f"ℹ️  {text}")

def check_python():
    """检查Python是否安装"""
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        print_success(f"Python版本: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print_error("Python未安装，请先安装Python 3.9+")
        return False

def check_node():
    """检查Node.js是否安装"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        print_success(f"Node.js版本: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print_error("Node.js未安装，请先安装Node.js 18+")
        return False

def install_backend_deps():
    """安装后端依赖"""
    backend_dir = Path('backend/calorie_backend')
    if not backend_dir.exists():
        print_error("后端目录不存在")
        return False
    
    os.chdir(backend_dir)
    
    print_info("安装后端依赖...")
    
    if not Path('venv').exists():
        print_info("创建Python虚拟环境...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'])
    
    venv_python = Path('venv/Scripts/python.exe') if platform.system() == 'Windows' else Path('venv/bin/python')
    
    print_info("安装Python依赖...")
    subprocess.run([str(venv_python), '-m', 'pip', 'install', '-r', 'requirements.txt'])
    
    print_success("后端依赖安装完成")
    return True

def install_frontend_deps():
    """安装前端依赖"""
    frontend_dir = Path('frontend')
    if not frontend_dir.exists():
        print_error("前端目录不存在")
        return False
    
    os.chdir(frontend_dir)
    
    if not Path('node_modules').exists():
        print_info("安装前端依赖...")
        subprocess.run(['npm', 'install'])
    
    print_success("前端依赖安装完成")
    return True

def migrate_database():
    """执行数据库迁移"""
    backend_dir = Path('backend/calorie_backend')
    os.chdir(backend_dir)
    
    venv_python = Path('venv/Scripts/python.exe') if platform.system() == 'Windows' else Path('venv/bin/python')
    
    print_info("执行数据库迁移...")
    subprocess.run([str(venv_python), 'manage.py', 'migrate'])
    
    print_success("数据库迁移完成")
    return True

def start_backend():
    """启动后端服务器"""
    backend_dir = Path('backend/calorie_backend')
    os.chdir(backend_dir)
    
    venv_python = Path('venv/Scripts/python.exe') if platform.system() == 'Windows' else Path('venv/bin/python')
    
    print_header("启动后端服务器")
    print_info("后端API: http://localhost:8000")
    print_info("Django Admin: http://localhost:8000/admin")
    print("\n按 Ctrl+C 停止服务器\n")
    
    try:
        subprocess.run([str(venv_python), 'manage.py', 'runserver'])
    except KeyboardInterrupt:
        print("\n后端服务器已停止")

def start_frontend():
    """启动前端开发服务器"""
    frontend_dir = Path('frontend')
    os.chdir(frontend_dir)
    
    print_header("启动前端开发服务器")
    print_info("前端应用: http://localhost:5173")
    print("\n按 Ctrl+C 停止服务器\n")
    
    try:
        subprocess.run(['npm', 'run', 'dev'])
    except KeyboardInterrupt:
        print("\n前端服务器已停止")

def start_all():
    """启动所有服务"""
    import threading
    
    print_header("启动所有服务")
    
    backend_thread = threading.Thread(target=start_backend)
    frontend_thread = threading.Thread(target=start_frontend)
    
    backend_thread.start()
    
    import time
    time.sleep(3)
    
    frontend_thread.start()
    
    backend_thread.join()
    frontend_thread.join()

def main():
    """主函数"""
    print_header("卡卡项目 - 启动菜单")
    
    if not check_python():
        sys.exit(1)
    
    if not check_node():
        sys.exit(1)
    
    print("\n请选择操作:")
    print("[1] 启动后端（Django）")
    print("[2] 启动前端（Vue）")
    print("[3] 全部启动")
    print("[4] 仅安装依赖")
    print("[5] 清除缓存重新安装")
    print("[0] 退出\n")
    
    try:
        choice = input("请输入选项 (0-5): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n再见！")
        sys.exit(0)
    
    if choice == '1':
        if not install_backend_deps():
            sys.exit(1)
        if not migrate_database():
            sys.exit(1)
        start_backend()
    elif choice == '2':
        if not install_frontend_deps():
            sys.exit(1)
        start_frontend()
    elif choice == '3':
        if not install_backend_deps():
            sys.exit(1)
        if not install_frontend_deps():
            sys.exit(1)
        if not migrate_database():
            sys.exit(1)
        start_all()
    elif choice == '4':
        install_backend_deps()
        install_frontend_deps()
        print_success("所有依赖安装完成！")
    elif choice == '5':
        backend_dir = Path('backend/calorie_backend')
        if backend_dir.exists():
            if Path('backend/calorie_backend/venv').exists():
                import shutil
                shutil.rmtree('backend/calorie_backend/venv')
                print_info("已删除后端虚拟环境")
        
        frontend_dir = Path('frontend')
        if frontend_dir.exists():
            if Path('frontend/node_modules').exists():
                import shutil
                shutil.rmtree('frontend/node_modules')
                print_info("已删除前端node_modules")
            if Path('frontend/package-lock.json').exists():
                Path('frontend/package-lock.json').unlink()
                print_info("已删除package-lock.json")
        
        install_backend_deps()
        install_frontend_deps()
        print_success("缓存清除并重新安装完成！")
    elif choice == '0':
        print("\n再见！")
        sys.exit(0)
    else:
        print_error("无效选择")
        sys.exit(1)

if __name__ == '__main__':
    main()
