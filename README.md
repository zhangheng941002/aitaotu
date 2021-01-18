# https://www.aitaotu.com/tag/
#### 项目由来
基于与爬虫的热爱</br>

#### 项目简介
1、每个标签的 url 和名字保存下来了,每个标签中的每一组套图的 url 和名字保存下来了,每个标签是一个大文件夹，每个套图是小文件夹</br>
2、在aisi.py中我抓取了三层信息，下载图片的处理我放在了管道文件中</br>
3、日志文件不需要可以自行在setting.py中注销</br>
4、该代码没有做代理的处理，如果你的ip被封掉，你可以自行在setting.py文件中，加入代理的设置，不过经测验不用设置

#### 安装依赖
`由于Windows环境下安装各种限制，建议在Linux环境中使用`
```
# 建议使用单独的依赖环境
pip install -r requirements.txt
```
#### 运行爬虫
```
# myspider 是爬虫名称
scrapy crawl myspider
```

#### 运行爬虫，并且保存组装的item信息
```
# myspider 是爬虫名称
scrapy crawl myspider -o items.json
```
`备注：scrapy在使用json encoder的时候默认所有数据均是ascii的，因此我们需要将数据编码设置为utf-8，在settings.py中增加配置
FEED_EXPORT_ENCODING = 'utf-8'`