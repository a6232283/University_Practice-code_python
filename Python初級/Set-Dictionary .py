#集合

#s1={3,4,5}
#print (10 not in s1)


#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2   #交集:取兩集合中，相同資料 4,5
#s3=s1|s2   #聯集:取兩集合中，但不重複 3,4,5,6,7
#s3=s1-s2   #差集:S1減去S2有重疊部分 3
#s3=s1^s2    #反交集:取兩集合中，不重複部分
#print(s3)


#s=set("hello") #set(字串) 差解匯出隨機
#print("h" in s)


#字典運算:key-value配對

#dic={"apple":"蘋果","bug":"蟲蟲"};
#dic["apple"]="小蘋果";
#print(dic["apple"])


#dic={"apple":"蘋果","bug":"蟲蟲"};
#print("apple" in dic)#判斷key是否存在


#del dic["apple"];#刪除字典中的鍵值對
#print(dic)


dic={x:x*2 for x in [3,4,5]}#從列表的資料產生字典
print(dic)