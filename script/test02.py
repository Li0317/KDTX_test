import requests


response = requests.post("http://kdtx-test.itheima.net/api/login",
                         json={"username": "admin", "password": "HM_2023_test",
                               "code": "2", "uuid": "520d4e173a09440396a73f5223319e0e"},
                         headers={"Content-Type": "application/json"})

print(response.status_code)
print(response.json())
