import os
import sys
import django

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 初始化Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calorie_backend.settings')
django.setup()

import requests
from apps.users.models import User

def check_user_in_db(username):
    """检查用户是否在数据库中存在"""
    try:
        user = User.objects.get(username=username)
        print(f"✅ 用户在数据库中存在:")
        print(f"   ID: {user.id}")
        print(f"   用户名: {user.username}")
        print(f"   密码哈希: {user.password[:30]}...")  # 只显示部分哈希
        print(f"   是否激活: {user.is_active}")
        print(f"   创建时间: {user.created_at}")
        return user
    except User.DoesNotExist:
        print(f"❌ 用户在数据库中不存在: {username}")
        return None
    except Exception as e:
        print(f"❌ 数据库查询错误: {e}")
        return None

def test_register_and_login(username, password):
    """测试注册和登录完整流程"""
    base_url = "http://localhost:8001/api/auth"
    
    print(f"\n=== 测试完整流程: {username} ===")
    print(f"密码: {password}")
    print("-" * 50)
    
    # 1. 先检查数据库中是否已存在该用户
    print("1. 检查数据库状态:")
    user_exists_before = check_user_in_db(username)
    print()
    
    # 2. 测试注册
    print("2. 测试注册:")
    register_url = f"{base_url}/register/"
    register_data = {"username": username, "password": password}
    
    try:
        register_response = requests.post(register_url, json=register_data, timeout=10)
        print(f"   注册响应状态码: {register_response.status_code}")
        print(f"   注册响应内容: {register_response.text}")
        
        if register_response.status_code == 201:
            print("   ✅ 注册成功!")
        elif register_response.status_code == 400:
            print("   ⚠️  注册失败 - 用户可能已存在")
        else:
            print("   ❌ 注册失败 - 服务器错误")
    except Exception as e:
        print(f"   ❌ 注册请求错误: {e}")
    print()
    
    # 3. 再次检查数据库
    print("3. 注册后检查数据库:")
    user_exists_after = check_user_in_db(username)
    print()
    
    # 4. 测试登录
    print("4. 测试登录:")
    login_url = f"{base_url}/login/"
    login_data = {"username": username, "password": password}
    
    try:
        login_response = requests.post(login_url, json=login_data, timeout=10)
        print(f"   登录响应状态码: {login_response.status_code}")
        print(f"   登录响应内容: {login_response.text}")
        
        if login_response.status_code == 200:
            print("   ✅ 登录成功!")
            return True
        else:
            print("   ❌ 登录失败")
            return False
    except Exception as e:
        print(f"   ❌ 登录请求错误: {e}")
        return False

def list_all_users():
    """列出所有用户"""
    print("\n=== 数据库中所有用户 ===")
    try:
        users = User.objects.all()
        print(f"总用户数: {users.count()}")
        print()
        
        for user in users:
            print(f"ID: {user.id}, 用户名: {user.username}, 激活: {user.is_active}")
            
    except Exception as e:
        print(f"❌ 查询所有用户错误: {e}")

if __name__ == "__main__":
    print("=== 开始测试注册和登录完整流程 ===")
    print()
    
    # 列出所有用户
    list_all_users()
    print("\n" + "="*60 + "\n")
    
    # 测试1: 已存在的用户 (wen)
    test_register_and_login("wen", "211304017")
    print("\n" + "="*60 + "\n")
    
    # 测试2: 新用户
    test_register_and_login("testuser2026_new", "password123")
    
    print("\n=== 测试完成 ===")