# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import re

from baiduphoto.items import BaiduphotoItem


class PhotosSpider(Spider):
    name = 'photos'
    allowed_domains = ['http://image.baidu.com/']
    start_urls = ['http://image.baidu.com//']
    headline = "壁纸"
    phootos_url = 'http://image.baidu.com/search/index?tn=baiduimage&word='+ headline +'&pn={next}&width=1920&height=1080'
    def start_requests(self):
        for num in range(1, 180):
            yield Request (self.phootos_url.format(next=num*10),callback = self.parse_url)

    def parse_url(self,response):
        resp = re.compile('"objURL":"(.*?)",')
        urls = re.findall(resp,response.text)
        item = BaiduphotoItem()
        item['image_urls'] = urls
        yield item








