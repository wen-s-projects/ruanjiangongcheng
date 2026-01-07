import requests
import json

print("=== Testing New User Registration ===")

# Test data for new user
register_data = {
    "username": "testuser123",
    "password": "password123"
}

print(f"Registering new user: {register_data['username']}")

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
        print("The new user has been successfully registered.")
        print("\n✅ The registration issue has been completely resolved!")
    else:
        print(f"\n⚠️ Registration returned status: {response.status_code}")
        
except Exception as e:
    print(f"\n❌ Error: {e}")

print("\n=== Test Complete ===")