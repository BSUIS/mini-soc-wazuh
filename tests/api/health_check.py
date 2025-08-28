import requests
import os
import sys

def test_api_health():
    domain = os.getenv('DOMAIN_NAME', 'siem.example.com')
    url = f"https://{domain}/api/health"
    
    try:
        response = requests.get(url, verify=False, timeout=30)
        print(f"API Health Status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"API Health Check Failed: {e}")
        return False

if __name__ == "__main__":
    if test_api_health():
        print("Health check passed")
        sys.exit(0)
    else:
        print("Health check failed")
        sys.exit(1)
