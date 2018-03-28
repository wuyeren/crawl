# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class MoviecrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    movieinfo = scrapy.Field()
    star = scrapy.Field()
    quote = scrapy.Field()

class BudejiecrawlItem(scrapy.Item):
    username = scrapy.Field()
    content = scrapy.Field()

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()

class ImagererfreItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    referer = scrapy.Field()