import requests

url="xxx"
headers={"User-Agent":"XXX"}
r1=requests.get(url)
print(r1.request.headers)

r=requests.get(url,headers=headers)
print(r.request.headers)