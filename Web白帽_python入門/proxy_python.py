import requests

url="http://www.buidu.com"
proxise={'http':'http://192.168.52.132.8080','https':'https://192.168.52.132.8080'}

r=requests.get(url,proxies=proxise,verify=False)
print(r.status_code)