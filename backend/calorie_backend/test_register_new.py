import requests
import json

url = "http://localhost:8000/api/auth/register/"
data = {
    "username": "newuser123",
    "password": "password123",
    "email": "newuser@example.com"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
except Exception as e:
    print(f"Error: {e}")
    if 'response' in locals():
        print(f"Response text: {response.text}")
