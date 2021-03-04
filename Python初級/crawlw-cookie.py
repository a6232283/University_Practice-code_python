#抓PPT八卦版網頁原始嗎(html)
import urllib.request as req
def getdata(url):

    #建立一個Request物件，附加Request handers的資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #print(data)

    #解析原始碼，取得每篇文章標題
    #安裝第三套建:  pip install beautifulsoup4
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")#尋找所有div、class的標籤
    for title in titles:
        if title.a !=None: #如果標籤包含a標籤。印出來
            print(title.a.string)

    #抓取上一頁連接
    nextLink=root.find("a",string="‹ 上頁")#找到內文式上頁的A標籤
    return nextLink["href"]

#主程序:抓取一個頁面標題
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageurl="https://www.ptt.cc"+getdata(pageurl)
    count+=1
    