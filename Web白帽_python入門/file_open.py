# with open('dir.txt','r') as f:
#     for line in f.readlines():
#         print(line.strip())

f1=open('dir.txt','w')#a->追加，不會覆蓋
f1.write('win')
f1.close()

f2=open('dir.txt','r')
for line in f2.readlines():
    print(line.strip())
f2.close()
