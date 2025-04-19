import urllib.request
import urllib.parse

# GET
with urllib.request.urlopen("https://httpbin.org/get") as response:
    print(response.read().decode())

# POST
data = urllib.parse.urlencode({"key": "value"}).encode()
req = urllib.request.Request("https://httpbin.org/post", data=data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode())
