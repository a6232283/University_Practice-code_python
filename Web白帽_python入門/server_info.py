import requests

url='http://192.168.X.X'

r=requests.get(url)
print(r.headers)