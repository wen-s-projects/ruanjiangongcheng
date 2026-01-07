import requests
import json

url = "http://localhost:8001/api/auth/register/"
data = {
    "username": "testuser",
    "password": "password123",
    "email": "test@example.com"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
except Exception as e:
    print(f"Error: {e}")
