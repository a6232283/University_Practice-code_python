#參數的預設資料
# def power(base,exp=0):
#     print(base**exp)

# power(3,2)
# power(4)


#使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)

# divide(2,4)
# divide(n2=4,n1=2)


#無限參數
def max(*masg):
    sum=0
    for n in masg:
        print(n)
        sum+=n
    print(sum/len(masg))

max(1,2,3)
