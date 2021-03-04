import requests

url="http://192.168.52.132"

r=requests.options(url)

# print(r.headers)
# print(r.headers["Allow"])
# print(r.headers['Public'])
result=r.headers['Public']
if result.find('PUT') and result.find('MOVE'):
    print('成功')
else:
    print('錯誤')