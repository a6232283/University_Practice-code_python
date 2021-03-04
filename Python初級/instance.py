#point實體物件的設計:平面座標上的點  上
# class point:
#     def __init__(self,x,y):#2個底線
#         self.x=x
#         self.y=y 
# #建立第一個實體物件
# p1=point(3,4)
# print(p1.x, p1.y)
# #建立第二個實體物件
# p2=point(5,6)
# print(p2.x,p2.y)


#fullName實體物件的設計:分開紀錄姓、名資料的全名
# class fullName:
#     def __init__(self,frist,lasr):
#         self.frist=frist
#         self.lasr=lasr

# name=fullName("C.W.","Penf")
# print(name.frist,name.lasr)

# name2=fullName("Tim","he")
# print(name2.frist,name2.lasr)


#下集
# class point:
#     def __init__(self,x,y):
#         self.x=x;
#         self.y=y;

#     def show(self):
#         print(self.x,self.y)

#     def distance(self,targetx,targety):
#         return (((self.x-targetx)**2)+((self.y-targety)**2))**0.5

# p=point(3,4)
# p.show()#呼叫實體方法/函式
# result=p.distance(0,0)#計算座標之間距離
# print(result)


class File:
    def __init__(self,name):
        self.name=name
        self.file=None#尚未開啟檔案:初期式None

    def open(self):
        self.file= open(self.name,mode="r",encoding="utf-8")

    def read(self):
        return self.file.read()

f1=File("data.txt")
f1.open()
data=f1.read()
print(data)