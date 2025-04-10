import requests

login = requests.post("http://localhost:5000/auth/login", json={"username": "admin", "password": "password123"})
token = login.json()["token"]
headers = {"Authorization": f"Bearer {token}"}

for _ in range(1000):
    r = requests.get("http://localhost:5000/compute", headers=headers)
    print(r.json())
