import requests

url="XXX"
data={"xxx":"xxx","xxx":"xxx"}

r=requests.get(url,params=data)

result=r.content

if str(result).find("succ"):
    print("xxx:xxx"+"succ")