#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/12/13 11:46
"""
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import scrapy
#C:\Users\Administrator\AppData\Roaming\Python\Scripts

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)



