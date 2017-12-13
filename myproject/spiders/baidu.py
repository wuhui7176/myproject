#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/12/13 14:39 
"""
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"

    start_urls = [
        'https://tieba.baidu.com/f?kw=java&fr=index',
    ]

    def parse(self, response):
        for quote in response.css('.j_th_tit'):
            print quote

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)