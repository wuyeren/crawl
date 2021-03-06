# -*- coding: utf-8 -*-
import scrapy
from crawl.items import ImagererfreItem

class ImagererfercrawlSpider(scrapy.Spider):
    name = 'imagererfercrawl'
    allowed_domains = ['www.mm131.com']
    start_urls = ['http://www.mm131.com/xinggan/3473.html',
                  'http://www.mm131.com/xinggan/2746.html',
                  'http://www.mm131.com/xinggan/3331.html']

    def parse(self, response):
        total_page = int(response.css('span.page-ch::text').extract_first()[1:-1])
        current_page = int(response.css('span.page_now::text').extract_first())
        item = ImagererfreItem()
        item['image_urls'] = response.css('div.content-pic img::attr(src)').extract()
        item['referer'] = response.url
        yield item
        if response.url.rfind('_') == -1:
            head, sep, tail = response.url.rpartition('.')
        else:
            head, sep, tail = response.url.rpartition('_')
        if current_page < total_page:
            yield scrapy.Request(head + f'_{current_page+1}.html')
