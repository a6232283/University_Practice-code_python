#定義函式
def multiply(n1, n2):
    #print(n1*n2)
    return n1*n2;

#呼叫函式
val=multiply(6,9)
print(val)

#multiply(6,9)


#程式包裝:同樣邏輯可重複利用
def calculate(x,y):
    sum=0;
    for n in range(x,y+1):
        sum+=n;
    print(sum);

calculate(1,10)
calculate(1,20)