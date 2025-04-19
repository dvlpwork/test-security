import requests

# GET
res = requests.get("https://httpbin.org/get")
print(res.status_code, res.json())

# POST
res = requests.post("https://httpbin.org/post", data={"key": "value"})
print(res.status_code, res.json())

# PUT
res = requests.put("https://httpbin.org/put", json={"key": "updated"})
print(res.status_code, res.json())

# HEAD
res = requests.head("https://httpbin.org/get")
print(res.status_code, res.headers)

# 任意のメソッド
res = requests.request("DELETE", "https://httpbin.org/delete")
print(res.status_code, res.json())
