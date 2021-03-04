#載入模組
import pandas as pd

#建立series
# data=pd.Series([20,10,15])
#基本series操作
# print(data)

# print(data.max())
# print(data.median())
# data=data*2
# print(data)

# data=data==20
# print(data)

#建立DataFram
data=pd.DataFrame({
    "name":["an","jan","ki"],
    "salary":[3000,5000,10000],
    "scd":[25,15,30]
})

#基本DataFram操作
# print(data)

#取得特定欄位
# print(data["name"])

#取得特定列表
# x=0
# for x in range(0,3):
    print(data.iloc[x])
    print("======")
    