from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
###網頁

def spidy(url, keyId):
    diver = webdriver.Chrome('chromedriver.exe')
    diver.get(url)
    # print(diver)

    try:
        diver.implicitly_wait(3)
        input_tag = diver.find_element_by_id('keyword')
        input_tag.send_keys(keyId)#填寫需求
        input_tag.send_keys(Keys.ENTER)
        google(diver)
    finally:
        diver.close()


def google(get_diver):
    try:
        goods = get_diver.find_elements_by_class_name('col3f')#一整個版面
        for good in goods:

            prod_name = good.find_element_by_css_selector('.prod_name a').text
            url = good.find_element_by_tag_name('a').get_attribute('href')
            coin = good.find_element_by_css_selector('.price span').text
            name = good.find_element_by_class_name('nick').text

            msg = '''
            商品名稱:%s
            連結:%s
            價格:%s
            產品介紹:%s
            ''' % (prod_name, url, coin,name)
            print(msg)



    except Exception:
        pass


if __name__ == '__main__':
    spidy('https://shopping.pchome.com.tw/', '筆電')


