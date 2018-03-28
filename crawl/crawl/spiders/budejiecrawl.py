# -*- coding: utf-8 -*-
import scrapy
from crawl.items import BudejiecrawlItem

class BudejiecrawlSpider(scrapy.Spider):
    name = 'budejiecrawl'
    allowed_domains = ['www.budejie.com/text']
    start_urls = ['http://www.budejie.com/text/']
    total_page = 1

    def parse(self, response):
        current_page = int(response.css('a.z-crt::text').extract_first())
        lines = response.css('div.j-r-list >ul >li')
        for li in lines:
            username = li.css('a.u-user-name::text').extract_first()
            content = '\n'.join(li.css('div.j-r-list-c-desc a::text').extract())
            yield BudejiecrawlItem(username=username, content=content)
        if current_page < self.total_page:
            yield scrapy.Request(self.start_urls[0] + f'{current_page+1}')
