import requests

def test_frontend_api_proxy():
    """测试前端API代理配置是否正确"""
    # 模拟前端通过代理发送请求
    # 前端运行在 5179，代理指向 8001
    base_url = "http://localhost:5179/api/auth"
    
    print("=== 测试前端API代理 ===")
    print("前端地址: http://localhost:5179")
    print("后端地址: http://localhost:8001")
    print("-" * 50)
    
    # 测试登录功能（使用已存在的用户）
    print("测试登录 (通过前端代理):")
    login_url = f"{base_url}/login/"
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    try:
        response = requests.post(login_url, json=login_data, timeout=15)
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        print()
        
        if response.status_code == 200:
            print("✅ 前端API代理配置正确!")
            print("✅ 登录功能通过前端代理正常工作!")
            return True
        else:
            print("❌ 前端API代理可能存在问题")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {e}")
        print("可能的原因:")
        print("1. 前端服务器未启动 (npm run dev)")
        print("2. 代理配置错误")
        print("3. 后端服务器未运行")
        return False

def test_direct_backend():
    """直接测试后端API"""
    print("\n=== 测试直接后端API ===")
    base_url = "http://localhost:8001/api/auth"
    
    # 测试登录
    print("测试登录 (直接访问后端):")
    login_url = f"{base_url}/login/"
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    try:
        response = requests.post(login_url, json=login_data, timeout=10)
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        print()
        
        if response.status_code == 200:
            print("✅ 后端API正常工作!")
            return True
        else:
            print("❌ 后端API存在问题")
            return False
            
    except Exception as e:
        print(f"❌ 错误: {e}")
        print("后端服务器可能未运行")
        return False

if __name__ == "__main__":
    print("开始测试前端API配置...")
    print()
    
    # 先测试直接后端
    backend_ok = test_direct_backend()
    
    if backend_ok:
        print("\n" + "="*60)
        # 再测试前端代理
        test_frontend_api_proxy()
    
    print("\n=== 测试完成 ===")