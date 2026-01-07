import requests
import json

def test_login_with_detailed_debug():
    """详细测试登录API"""
    base_url = "http://localhost:8001/api/auth"
    
    print("=== 详细测试登录API ===")
    print()
    
    # 测试1: 检查后端服务器是否运行
    print("1. 检查后端服务器状态:")
    try:
        response = requests.get("http://localhost:8001/health/", timeout=5)
        print(f"   健康检查响应: {response.status_code}")
        print(f"   响应内容: {response.text}")
        if response.status_code == 200:
            print("   ✅ 后端服务器运行正常")
        else:
            print("   ❌ 后端服务器可能有问题")
    except Exception as e:
        print(f"   ❌ 无法连接到后端服务器: {e}")
        return
    print()
    
    # 测试2: 测试登录API
    print("2. 测试登录API:")
    login_url = f"{base_url}/login/"
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    print(f"   请求URL: {login_url}")
    print(f"   请求数据: {json.dumps(login_data, ensure_ascii=False)}")
    print(f"   请求头: Content-Type: application/json")
    print()
    
    try:
        response = requests.post(
            login_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"   响应状态码: {response.status_code}")
        print(f"   响应头: {dict(response.headers)}")
        print(f"   响应内容: {response.text}")
        print()
        
        if response.status_code == 200:
            print("   ✅ 登录成功!")
            try:
                data = response.json()
                print(f"   返回的用户数据: {data.get('user', {})}")
                print(f"   返回的令牌数据: {data.get('tokens', {})}")
            except:
                print("   响应不是有效的JSON格式")
        elif response.status_code == 500:
            print("   ❌ 服务器内部错误 (500)")
            print("   这可能是后端代码逻辑错误")
        elif response.status_code == 400:
            print("   ⚠️  客户端请求错误 (400)")
            print("   可能是用户名或密码错误")
        else:
            print(f"   ❌ 未知错误: {response.status_code}")
            
    except requests.exceptions.ConnectionError as e:
        print(f"   ❌ 连接错误: {e}")
        print("   后端服务器可能未运行")
    except requests.exceptions.Timeout as e:
        print(f"   ❌ 请求超时: {e}")
    except Exception as e:
        print(f"   ❌ 未知错误: {e}")
        print(f"   错误类型: {type(e).__name__}")
    
    print()
    print("=== 测试完成 ===")

if __name__ == "__main__":
    test_login_with_detailed_debug()