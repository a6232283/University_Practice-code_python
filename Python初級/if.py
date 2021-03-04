#switch不支援

#if判斷

#x=int(input("請輸入數字"));


#if(x>=200):
#    print("大於200")

#elif x>=100:
#    print("大於100，小於200")

#else:
#    print("小於100")



#四則運算
n1=input("請輸入數字一:")
if n1.isdigit():#偵測數字
    n1=int(n1)
else:
    print("請正確輸入數字")


n2=input("請輸入數字二:")
if n2.isdigit():
    n2=int(n2)
else:
    print("請正確輸入數字")


op=input("請輸入運算+,-,*,/:")

if op=="+":
    print(n1+n2)

elif op=="-":
    print(n1-n2)

elif op=="*":
    print(n1*n2)

elif op=="/":
    print(n1/n2)

else:
    print("請正確輸入運算")