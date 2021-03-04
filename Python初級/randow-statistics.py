#隨機模組
import random
#隨機選取
#data =random.choice([1,5,8,4,9])取一
#data =random.sample([1,5,8,4,9],2)取2以上，不超過列表
#print (data)

#隨機變換順序
# data=[5,48,7,5]
# random.shuffle(data)
# print(data)

#隨機取得亂數
# data=random.random()#0~1之間隨機亂數
# print(data)

# for x in range(1,11):
#     data=random.uniform(60,100)#0~60之間隨機亂數
#     data=int(data)
#     print(data)

#取得常態分配亂數
#平均數100，標準差10，取得資料｛多數｝再90~110之間
# data=random.normalvariate(100,10)
# print(data)


#統計模組
import statistics as stat
data=stat.stdev([1,5,6,1,8,15,13,100])
print(data)