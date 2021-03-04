import pandas as pd

#資料索引
data=pd.DataFrame({
    "name":["any","ki","jason"],
    "salar":[3000,5000,10000]
},index=["a","b","c"])
print(data)
print("====================")


#觀察資料
# print("資料的數列",data.size)
# print("資料型態(列,欗)",data.shape)
# print("資料索引",data.index)


#取的列(橫向)的series的資料:根據順序、根據索引
# print("取得第二列",data.iloc[1],sep="\n")
# print("====================")
# print("取得第c列",data.loc["c"],sep="\n")


#取得欗(直向)的series的資料:根據欄位的名稱
# print("取得name欄位",data["name"],sep="\n")
# names=data["name"]#取的單位度的series資料
# print("把name全部轉大寫",names.str.upper(),sep="\n")

# salaries=data["salar"]
# print("薪水平均值",.mean())


#建立新的欄位
data["revenus"]=[50000,4000,3000]#data新欄位名稱=列表
data["rank"]=pd.Series([3,5,6],index=["a","b","c"])#data新欄位名稱=series的資料
data["cp"]=data["revenus"]/data["salar"]
print(data)