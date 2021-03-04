import requests



for i in range(0,24,2):
    url = 'https://play.google.com/books/reader?id=ukuCDwAAQBAJ&pg=GBS.PA{}&hl=zh_TW'.format(i)
    https = requests.get(url)

    with open('./test/{}'.format(i),'wb') as f:
        f.write(https.content)
