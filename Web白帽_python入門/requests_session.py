import requests

url='http://google.com'

s=requests.session()
r=s.get(url)
print (r.cookies)
print(r.request.headers)

r1=s.get(url)
print(r1.request.headers)

