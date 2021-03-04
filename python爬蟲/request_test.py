import requests

print("網站請求")
a=input("請輸入網頁")

url=requests.get(a)
print("請求結果:",a.text())