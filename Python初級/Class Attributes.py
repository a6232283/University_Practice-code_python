#定義2個類別
class IO:
    supportedSrcs=["consloe","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("not supportedSrcs")
        else:
            print("Read from",src)

#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("aabbcc")