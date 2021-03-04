import requests
from bs4 import BeautifulSoup
def web():

    url='https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=mis&order=15&asc=0&page=%d&mode=s&jobsource=2018indexpoc'%(i)
    res=requests.get(url).text

    html=BeautifulSoup(res,'lxml')
    print(html)




web()


