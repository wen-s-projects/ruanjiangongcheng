import requests
import json

def test_backend():
    print("=" * 60)
    print("测试后端API")
    print("=" * 60)
    print()

    base_url = "http://localhost:8000"

    print("1. 测试根URL...")
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        print(f"   ✓ 根URL响应: {response.status_code}")
    except Exception as e:
        print(f"   ✗ 根URL失败: {e}")
    print()

    print("2. 测试注册API...")
    try:
        data = {
            "username": "testuser123",
            "password": "testpass123"
        }
        response = requests.post(
            f"{base_url}/api/auth/register/",
            json=data,
            timeout=5
        )
        print(f"   ✓ 注册API响应: {response.status_code}")
        print(f"   响应内容: {response.text[:200]}")
    except Exception as e:
        print(f"   ✗ 注册API失败: {e}")
    print()

    print("3. 测试登录API...")
    try:
        data = {
            "username": "testuser123",
            "password": "testpass123"
        }
        response = requests.post(
            f"{base_url}/api/auth/login/",
            json=data,
            timeout=5
        )
        print(f"   ✓ 登录API响应: {response.status_code}")
        print(f"   响应内容: {response.text[:200]}")
    except Exception as e:
        print(f"   ✗ 登录API失败: {e}")
    print()

    print("=" * 60)
    print("测试完成")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_backend()
    except KeyboardInterrupt:
        print("\n测试已取消")
    except Exception as e:
        print(f"\n测试出错: {e}")
        import traceback
        traceback.print_exc()

    input("\n按Enter键退出...")
