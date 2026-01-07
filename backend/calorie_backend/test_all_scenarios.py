import requests
import json

def test_all_scenarios():
    """测试所有可能的场景"""
    print("=== 测试所有场景 ===")
    print()
    
    # 场景1: 直接后端请求（基准测试）
    print("1. 直接后端请求（基准测试）:")
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
        
        print(f"   状态码: {response.status_code}")
        print(f"   响应内容: {response.text[:100]}...")
        print()
        
        if response.status_code == 200:
            print("   ✅ 直接后端请求成功!")
        else:
            print(f"   ❌ 直接后端请求失败: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ 请求失败: {e}")
    
    print()
    
    # 场景2: 前端代理请求
    print("2. 前端代理请求:")
    proxy_url = "http://localhost:5181/api/auth/login/"
    
    try:
        response = requests.post(
            proxy_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"   状态码: {response.status_code}")
        print(f"   响应头: {dict(response.headers)}")
        print(f"   响应内容: {response.text[:100]}...")
        print()
        
        if response.status_code == 200:
            print("   ✅ 前端代理请求成功!")
        elif response.status_code == 500:
            print("   ❌ 前端代理请求返回500!")
            print("   这表明问题在前端代理或后端处理代理请求时")
        else:
            print(f"   ❌ 前端代理请求失败: {response.status_code}")
            
    except Exception as e:
        print(f"   ❌ 请求失败: {e}")
    
    print()
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_all_scenarios()