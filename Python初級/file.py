#存入檔案

# file=open("data.txt",mode="w",encoding="utf-8")#開啟、可寫、文字編碼
# file.write("Hello\n 測試中文")#操作
# file.close()#關閉

#最佳用法
# with open("data.txt",mode="w",encoding="utf-8")as file:
#     file.write("6\n6")


#讀取檔案

# sum=0
# with open("data.txt",mode="r",encoding="utf-8")as file:
#     for line in file:#一行一行讀取
#         sum+=int(line)
# print(sum)


#使用json格式讀取、複寫檔案
import json
#從檔案中讀取json資料，放入變數data裡面
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data)
data["name"]="new name"#修改變數中資料
#把最新資料複寫檔案中
with open("config.json",mode="w") as file:
     json.dump(data,file)