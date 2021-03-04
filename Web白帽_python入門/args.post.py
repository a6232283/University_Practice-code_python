import requests

url="XXX"
data={"xxx":"xxx","xxx":"xxx"}

r=requests.post(url,data=data)

print(r.status_code)

if r.text.find('succ'):
    print("xxx:xxx"+"succ")

