import requests
import re
from urllib.request import urlretrieve
def download_video():

    https=requests.get('https://www.pearvideo.com/').text
    # print(reg + https)
    reg=r' <div class="verimg-view"><div  class="img" style="background-image: url(.*?);"></div></div>'
    r=re.findall(reg,https)
    # print(void)

#拼接
    url=[]
    http='https://www.pearvideo.com/'

    for val in r:
        httpaa=http + val
        # print(httpaa)
        url.append(httpaa)
        print(url)


download_video()