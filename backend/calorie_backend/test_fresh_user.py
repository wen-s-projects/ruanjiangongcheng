import requests

def test_register_new_user():
    """Test registering a completely new user"""
    url = "http://localhost:8001/api/auth/register/"
    
    # Use a unique username that hasn't been tested before
    data = {
        "username": "newuser2026",
        "password": "testpassword123"
    }
    
    print("=== Testing Fresh User Registration ===")
    print(f"Registering user: {data['username']}")
    print(f"Password: {data['password']}")
    print()
    
    try:
        response = requests.post(url, json=data, timeout=10)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        print()
        
        if response.status_code == 201:
            print("✅ Registration successful!")
            print("User created with status 201 Created")
        elif response.status_code == 400:
            print("⚠️ Registration returned status: 400")
            print("This means the user already exists (good validation!)")
        else:
            print(f"❌ Registration failed with status: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print()
    print("=== Test Complete ===")

if __name__ == "__main__":
    test_register_new_user()