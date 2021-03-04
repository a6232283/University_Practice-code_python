import requests
import time
import json
def main(url,headers):
    time.sleep(5)
    s=requests.session()
    s.headers.update(headers)
    s.get(url=url,headers=headers).text
    s_=s.json()
    print(s_)

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Referer': 'https://www.google.com/',
}

r = requests.get('https://www.lagou.com/', headers=headers).text


main(r,headers)