#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   items.py
@Time    :   2019/03/23 18:57:51
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UniversalspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsItem(scrapy.Item):
    
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    datetime = scrapy.Field()
    source = scrapy.Field()
    website = scrapy.Field()
    attrs = scrapy.Field()
    category = scrapy.Field()
    author = scrapy.Field()
    keywords = scrapy.Field()
    dcdescription = scrapy.Field()

    
class BaikeItem(scrapy.Item):

    name = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()

#-------version 3--------
class NewsItemV3(scrapy.Item):

    title = scrapy.Field()
    dateissued = scrapy.Field()
    subject = scrapy.Field()
    text = scrapy.Field()
    description= scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()


#-------version 4------- for journal
class NewsItemV4(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()
    dateissued = scrapy.Field()
    organ = scrapy.Field()
    source = scrapy.Field()
    start = scrapy.Field()
    num = scrapy.Field()
    url = scrapy.Field()
    subject = scrapy.Field()
    _class = scrapy.Field()