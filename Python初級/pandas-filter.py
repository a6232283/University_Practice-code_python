import pandas as pd

#篩選練習-series
# data=pd.Series([30,15,20])
# condition=data>18
# print(condition)
# fileteredData=data[condition]
# print(fileteredData)

# data=pd.Series(["你好","python","ki"])
# condition=data.str.contains("p")
# print(condition)
# fileteredData=data[condition]
# print(fileteredData)


#篩選練習-DataFram
data=pd.DataFrame({
    "name":["jc","jan","ki"],
    "salary":[3000,5000,10000]
})
condition=data["name"]=="jan"
fileteredData=data[condition]
print(fileteredData)


