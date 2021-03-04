import requests


url = 'https://www.google.com.tw/log?format=json&hasfast=true'
heards={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'referer': 'https://translate.google.com.tw/'
}

r=requests.post(url, heards=heards)
print(r.json())

