import requests
from lxml import etree

'''
eval():将字符串str当成有效的表达式来求值并返回计算结果
'''
url = 'http://114.67.246.176:10629/'
response = requests.session()
re = response.get(url=url).content.decode('utf-8')
elements = etree.HTML(re).xpath('//div/text()')[0][0:-3]
result = eval(elements)
#print(result,'\n')
data = {
    'value':result
}
flag = response.post(url=url,data=data).content.decode('utf-8')
# flag_x = etree.HTML(flag)
# # print(etree.tostring(flag_x,encoding='utf-8').decode('utf-8'))
print(flag)

