#break
# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print("最後的值",n)


#continue
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print (x)
#     n+=1
# print("最後的值",n)


#else
# sum=0
# for n in range(11):#0~10
#     sum+=n
# else:
#     print(sum)


#綜合
n=input("輸入一個數字")
n=int(n)
for i in range(n):
    if i*i==n:
        print("平方根",i)
        break
else :
    print("沒有開根號")