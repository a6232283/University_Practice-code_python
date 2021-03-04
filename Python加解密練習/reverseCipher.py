mseeage=input("輸入文字:")
translated=''

i=len(mseeage)-1
while i>=0:
    translated=translated+mseeage[i]
    #print("數字",i,"   內容",mseeage[i],"   反轉後內容",translated)
    i=i-1

print(translated)