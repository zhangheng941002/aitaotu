# 人丑就要多学习

import requests
from lxml import etree


# url = 'https://www.aitaotu.com/tag/'
# session = requests.session()
#
# res = session.get(url).text
#
# html = etree.HTML(res)
# res = html.xpath('//div[@class="tags_list "]/dl')[0].xpath('./dd/a/text()')
# print(res)
# import os
# str1 = 'https://img.aitaotu.cc:8089/Pics/2018/0314/08/5.1.jpg'
#
# a = os.path.splitext(str1)
# b = a.split('/')[-1]
# print(a)
# print(b)

# url = 'https://www.aitaotu.com/tag/xixiwang.html'
# for i in range(1,15):
#     a = os.path.splitext(url)
#     urla = a[0]+'/'+str(i) + a[1]
#     print(urla)


url = "https://img.aitaotu.cc:8089/Ximg/2016/0401/145947108919826.jpg"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    "Referer": "https://www.aitaotu.com/"

}
session = requests.session()
resp = session.get(url, headers=headers)
print(resp.status_code)