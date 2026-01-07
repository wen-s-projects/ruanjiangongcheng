import requests
import json

def test_login_like_frontend():
    """模拟前端发送的登录请求"""
    base_url = "http://localhost:8001/api/auth"
    
    print("=== 模拟前端登录请求 ===")
    print()
    
    # 测试登录
    login_url = f"{base_url}/login/"
    login_data = {
        "username": "wen",
        "password": "211304017"
    }
    
    print(f"请求URL: {login_url}")
    print(f"请求方法: POST")
    print(f"请求头: Content-Type: application/json")
    print(f"请求体: {json.dumps(login_data, ensure_ascii=False)}")
    print()
    
    try:
        response = requests.post(
            login_url, 
            json=login_data, 
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"响应状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}")
        print(f"响应内容: {response.text}")
        print()
        
        if response.status_code == 200:
            print("✅ 登录成功!")
            data = response.json()
            print(f"用户数据: {data.get('user', {})}")
            print(f"令牌数据: {data.get('tokens', {})}")
        elif response.status_code == 500:
            print("❌ 服务器内部错误 (500)")
            print("这可能是后端代码逻辑错误")
        else:
            print(f"⚠️  其他错误: {response.status_code}")
            
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        print(f"错误类型: {type(e).__name__}")

if __name__ == "__main__":
    test_login_like_frontend()