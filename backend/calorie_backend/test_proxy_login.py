import requests
import json

def test_proxy_login():
    """测试通过前端代理的登录请求"""
    base_url = "http://localhost:5180/api/auth"
    
    print("=== 测试前端代理登录 ===")
    print()
    
    # 测试1: 没有token的请求
    print("1. 测试没有token的登录请求:")
    login_url = f"{base_url}/login/"
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    try:
        response = requests.post(
            login_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"   响应状态码: {response.status_code}")
        print(f"   响应内容: {response.text[:200]}...")
        print()
        
        if response.status_code == 200:
            print("   ✅ 登录成功!")
        elif response.status_code == 500:
            print("   ❌ 服务器内部错误 (500)")
            print("   这是前端报告的错误!")
        else:
            print(f"   ⚠️  其他错误: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ 请求失败: {e}")
    
    print()
    
    # 测试2: 带有旧token的请求（模拟前端可能的情况）
    print("2. 测试带有旧token的登录请求:")
    old_token = "some-old-token-12345"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {old_token}"
    }
    
    try:
        response = requests.post(
            login_url, 
            json=login_data, 
            headers=headers,
            timeout=10
        )
        
        print(f"   响应状态码: {response.status_code}")
        print(f"   响应内容: {response.text[:200]}...")
        print()
        
        if response.status_code == 200:
            print("   ✅ 登录成功!")
        elif response.status_code == 500:
            print("   ❌ 服务器内部错误 (500)")
            print("   这可能是问题所在!")
        else:
            print(f"   ⚠️  其他错误: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ 请求失败: {e}")
    
    print()
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_proxy_login()