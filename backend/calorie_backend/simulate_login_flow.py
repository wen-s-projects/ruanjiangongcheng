import requests
import json
import time

def simulate_login_flow():
    """模拟前端用户登录的完整流程"""
    print("=== 模拟前端用户登录流程 ===")
    print()
    
    # 步骤1: 输入用户名和密码
    print("步骤1: 输入用户名和密码")
    username = "wen"
    password = "211304017"
    print(f"   用户名: {username}")
    print(f"   密码: {password}")
    print()
    
    # 步骤2: 点击登录按钮（发送请求到前端代理）
    print("步骤2: 点击登录按钮（发送请求到前端代理）")
    proxy_url = "http://localhost:5179/api/auth/login/"
    login_data = {
        "username": username,
        "password": password
    }
    
    print(f"   请求URL: {proxy_url}")
    print(f"   请求方法: POST")
    print(f"   请求头: Content-Type: application/json")
    print(f"   请求体: {json.dumps(login_data, ensure_ascii=False)}")
    print()
    
    try:
        response = requests.post(
            proxy_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"   响应状态码: {response.status_code}")
        print(f"   响应头: {dict(response.headers)}")
        print(f"   响应内容: {response.text[:200]}...")
        print()
        
        if response.status_code == 200:
            print("   ✅ 登录成功!")
            try:
                data = response.json()
                print(f"   用户数据: {data.get('user', {})}")
                print(f"   令牌数据: {data.get('tokens', {})}")
                
                # 检查令牌格式
                access_token = data.get('tokens', {}).get('access_token', '')
                refresh_token = data.get('tokens', {}).get('refresh_token', '')
                print(f"   Access Token长度: {len(access_token)}")
                print(f"   Refresh Token长度: {len(refresh_token)}")
                
            except:
                print("   响应不是有效的JSON格式")
        elif response.status_code == 500:
            print("   ❌ 服务器内部错误 (500)")
            print("   这可能是问题所在!")
        elif response.status_code == 400:
            print("   ⚠️  客户端请求错误 (400)")
            print(f"   错误信息: {response.text}")
        else:
            print(f"   ⚠️  其他错误: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ 请求失败: {e}")
        print(f"   错误类型: {type(e).__name__}")
    
    print()
    print("=== 模拟完成 ===")

def test_direct_backend():
    """测试直接后端请求（基准测试）"""
    print("=== 测试直接后端请求（基准测试）===")
    print()
    
    direct_url = "http://localhost:8001/api/auth/login/"
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    try:
        response = requests.post(
            direct_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text[:100]}...")
        
        if response.status_code == 200:
            print("✅ 直接后端请求成功!")
        else:
            print(f"❌ 直接后端请求失败: {response.status_code}")
            
    except Exception as e:
        print(f"❌ 请求失败: {e}")
    
    print()

if __name__ == "__main__":
    # 先测试直接后端请求
    test_direct_backend()
    print()
    print()
    
    # 然后模拟前端用户登录流程
    simulate_login_flow()