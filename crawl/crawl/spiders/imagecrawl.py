# -*- coding: utf-8 -*-
import scrapy
from crawl.items import ImageItem


class ImagecrawlSpider(scrapy.Spider):
    name = 'imagecrawl'
    allowed_domains = ['www.meizitu.com']
    start_urls = ['http://www.meizitu.com/a/5501.html']

    def parse(self, response):
        yield ImageItem(image_urls=response.css('div#picture img::attr(src)').extract())