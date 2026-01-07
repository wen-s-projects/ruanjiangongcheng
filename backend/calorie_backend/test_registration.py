import requests
import json

print("=== Testing Registration API ===")

# Test data
register_data = {
    "username": "wen",
    "password": "211304017"
}

print(f"Registering user: {register_data['username']}")
print(f"Password: {register_data['password']}")

try:
    # Send POST request to registration endpoint
    response = requests.post(
        "http://localhost:8001/api/auth/register/",
        json=register_data,
        headers={"Content-Type": "application/json"},
        timeout=10
    )
    
    print(f"\nResponse status code: {response.status_code}")
    print(f"Response content: {response.text}")
    
    if response.status_code == 201:
        print("\n🎉 REGISTRATION SUCCESSFUL!")
        print("The user has been successfully registered.")
    else:
        print(f"\n⚠️ Registration returned status: {response.status_code}")
        
except Exception as e:
    print(f"\n❌ Error: {e}")

print("\n=== Test Complete ===")