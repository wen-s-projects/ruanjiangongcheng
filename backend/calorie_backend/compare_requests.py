import requests
import json

def compare_requests():
    """对比前端代理请求和直接后端请求"""
    print("=== 对比请求差异 ===")
    print()
    
    # 测试数据
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    # 测试1: 直接后端请求
    print("1. 直接后端请求:")
    direct_url = "http://localhost:8001/api/auth/login/"
    
    try:
        response1 = requests.post(
            direct_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"   状态码: {response1.status_code}")
        print(f"   响应内容: {response1.text[:100]}...")
        print()
    except Exception as e:
        print(f"   错误: {e}")
        print()
    
    # 测试2: 前端代理请求
    print("2. 前端代理请求:")
    proxy_url = "http://localhost:5179/api/auth/login/"
    
    try:
        response2 = requests.post(
            proxy_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"   状态码: {response2.status_code}")
        print(f"   响应内容: {response2.text[:100]}...")
        print()
    except Exception as e:
        print(f"   错误: {e}")
        print()
    
    # 对比结果
    print("3. 结果对比:")
    if response1.status_code == 200 and response2.status_code == 500:
        print("   ❌ 前端代理返回500，但直接后端返回200")
        print("   这表明问题在前端代理或后端处理代理请求时")
    elif response1.status_code == 200 and response2.status_code == 200:
        print("   ✅ 两种请求都成功")
    else:
        print(f"   ⚠️  不同的结果: 直接={response1.status_code}, 代理={response2.status_code}")

if __name__ == "__main__":
    compare_requests()