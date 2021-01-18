# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AisispiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 组图的标题
    title = scrapy.Field()
    # 组图的 url
    title_url = scrapy.Field()
    # 图片的标题
    img_name = scrapy.Field()
    # 组图进入下载的主 url
    img_main_url = scrapy.Field()
    # 组图的发布时间
    img_date = scrapy.Field()
    # 组图的浏览量
    img_look_num = scrapy.Field()
