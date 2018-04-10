# -*- coding: utf-8 -*-
import scrapy
from aisiSpider.items import AisispiderItem
import os


class AisiSpider(scrapy.Spider):
    name = 'aisi'
    allowed_domains = ['aitaotu.com']
    start_urls = ['https://www.aitaotu.com/tag/']

    # 分析标签，获得每个标签的名字和url
    def parse(self, response):
        # 第一个国内套图的节点
        zutu = response.xpath('//div[@class="tags_list "]/dl')[0]
        # 分组的标题
        title = zutu.xpath('./dd/a/text()').extract()
        # 分组的链接
        title_url = zutu.xpath('./dd/a/@href').extract()
        # print(title)
        # print(title_url)
        for tit, url in zip(title, title_url):
            item = AisispiderItem()
            item['title'] = tit
            url_a = 'https://www.aitaotu.com' + url
            item['title_url'] = url_a
            yield scrapy.Request(url_a, callback=self.second_parse, meta={'item': item})

    # 获得每个单独的标签下，一共有几页
    def second_parse(self, response):
        item = response.meta['item']
        group_url = item['title_url']
        # 分析页面，看给分类下有几页数据
        # 先获取最后一页的url,进行处理，获取一共几页
        # 因为有的标签只有一页，所以需要处理 这个url就只有一页 https://www.aitaotu.com/tag/tukmo.html
        page = response.xpath('//div[@id="pageNum"]//a[last()]/@href').extract()  # /tag/sijianwu/15.html
        if len(page) != 0:
            page = response.xpath('//div[@id="pageNum"]//a[last()]/@href').extract()[0]  # /tag/sijianwu/15.html
            pageNum = int(os.path.splitext(page)[0].split('/')[-1])
            for page in range(1, pageNum + 1):
                every_url = os.path.splitext(group_url)
                every_page_url = every_url[0] + '/' + str(page) + every_url[1]
                yield scrapy.Request(every_page_url, callback=self.third_parse, meta={'item': item})
        else:
            yield scrapy.Request(group_url, callback=self.third_parse, meta={'item': item})

    """
    处理url时候用到的知识点
    url = 'https://www.aitaotu.com/tag/xixiwang.html'
    for i in range(1,15):
        a = os.path.splitext(url)
        urla = a[0]+'/'+str(i) + a[1]
        print(urla)
    """

    # 每一页中的套图的处理
    def third_parse(self, response):
        item = response.meta['item']
        # 经分析没个页面 有20组套图
        data = response.xpath('//div[@id="mainbody"]//li')
        # 循环抓取每一个套图的名字，和进入下载的主url
        for each in data:
            # 组图的名称
            item['img_name'] = each.xpath('./a/img/@alt').extract()[0]
            # 组图的 url
            item['img_main_url'] = 'https://www.aitaotu.com' + each.xpath('./a/@href').extract()[0]
            # 组图的发布时间
            item['img_date'] = each.xpath('./div/i/text()').extract()[1]
            # 组图的浏览量
            item['img_look_num'] = each.xpath('./div/i/text()').extract()[0]

            yield item
