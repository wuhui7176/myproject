#!/usr/bin/env python  
# encoding: utf-8  
"""
@version: v1.0 
@author: wuhui
@time: 2017/12/13 14:25 
"""
import sys

reload(sys)
sys.setdefaultencoding('utf8')


from scrapy import cmdline

# scrapy_spider為剛剛建立的spider name，可以在這裡切換不同的spider
cmdline.execute(['scrapy', 'crawl', 'quotes'])
# execute("scrapy crawl spider".split())