import secrets

a=secrets.randbelow(10)# randbelow適用數字
print (a)

b=secrets.choice('safojff')# choice適用文字
print(b)

test=''
for i in range(30+1):
    test+=secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(test)
