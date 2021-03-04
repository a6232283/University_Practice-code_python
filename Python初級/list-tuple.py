#list
x=[12,60,15,70,90];

#x[0:2]=[]; #刪掉0~2，不包含2

x=x+[5,1];

x[1]=22;#修改陣列內容

print(x);

print(x[0:3]);

print(len(x));#列表長度


data=[[3,4,5],[6,7,8]];
print(data);
data[0][0:2]=[5,5,5];
print(data);



#tuple
a=(3,4,5)
#a[0]=5    錯誤:tuple的資料不可變動
print(a[0:2])