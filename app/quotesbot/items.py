# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title= scrapy.Field();
    link= scrapy.Field();
    source= scrapy.Field();
    release_time= scrapy.Field(),
    xuanjiang_time= scrapy.Field(),
    xuanjiang_location = scrapy.Field(),
    pass


