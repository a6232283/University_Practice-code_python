import requests
from  lxml import  etree
def web():
    for i in range (1,2):
        url='https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=mis&order=15&asc=0&page=%d&mode=s&jobsource=2018indexpoc'%(i)
        res=requests.get(url).text
        # print(res)
        html=etree.HTML(res)

        page_list=html.xpath("//div[@class='l-content--2col--main l-container jobs-content']")
        # print(page_list)

        for data in page_list:

            # print(data)
            position=data.xpath("./div/div/article/@data-job-name")
            cust=data.xpath("./div/div/article/@data-cust-name")
            # print(position)
            zipde=zip(position,cust)
            print(dict(zipde))
web()


