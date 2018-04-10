# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import requests
from lxml import etree
import os
class AisispiderPipeline(object):
    def process_item(self, item, spider):

        # 将获取的数据写入本地json文件
        # file = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        # with open("mm.json", 'ab') as f:
        #     f.write(file.encode("utf-8"))  # 经encode（）编码后是二进制数据，所以上面用'ab'写入

        # 获得每组套图的主链接
        img_load = item['img_main_url']
        # print(img_load)
        # 进入分析，获得共几页，和每张图片的url
        session = requests.session()
        res = session.get(img_load).text
        html = etree.HTML(res)
        # 分析获取一共有几页
        page = html.xpath('//div[@class="pages"]//li[last()]/a/@href')[0]  # /guonei/35314_23.html
        # print(page)
        # 进行截取，取出最后一页的数字
        num = os.path.splitext(page)[0].split('_')[-1]
        # 重新编写URL 每组套图的每一页的URL
        for page in range(1,int(num)+1):
            url_f = os.path.splitext(img_load)
            url_fin = url_f[0] + "_" + str(page) + url_f[1]
            # 重新进行发送，请求数据，这里是每一页的数据，分析找出每张图片的src 属性
            res1 = session.get(url_fin).text
            html1 = etree.HTML(res1)
            # 这里找到的是一个列表，下载需要循环
            # 图片的下载地址
            img_src = html1.xpath('//div[@id="big-pic"]//a/img/@src')
            # 图片的名字
            img_fin_name = html1.xpath('//div[@id="big-pic"]//a/img/@alt')
            print(img_src,img_fin_name)

            # 创建下载路径，每个标签为一个文件夹，在该文件夹下每组套图为一个文件夹
            path = 'F:\五层链接爬出图片/' + item['title'] + "/" + item['img_name']
            if not os.path.exists(path):
                os.makedirs(path)
            # print(path)
            # 进行下载
            for src,name in zip(img_src,img_fin_name):
                resp = session.get(src).content
                # 获取图片的后缀
                hz = os.path.splitext(src)[1]

                file = open(path+'/'+name+ hz, 'wb')
                file.write(resp)
                file.close()



        return item
