#網路連線
# import urllib.request as request
# src="https://www.pccu.edu.tw/"
# with request.urlopen(src)as response:
#     data=response.read().decode("utf-8")#取得台大網站原始碼
# print(data)


#串接、擷取公開資料
import json
import urllib.request as request
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src)as response:
    data=json.load(response)
#將公司名稱列表出來
clist=data["result"]["results"]
#print(clist)
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+company["公司地址"]+" \n")
