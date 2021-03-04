import requests

url='http://google.com'
r=requests.get(url=url)
#响應頭
print(r.request)
#請求頭
print(r.request.headers)
print(r.url)
print(r.status_code)
