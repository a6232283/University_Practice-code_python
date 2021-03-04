import requests

url='https://httpbin.org/get'
r=requests.get(url)
print(r.request.headers)
print(r.headers)
print(r.status_code)