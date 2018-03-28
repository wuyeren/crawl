# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines import images
from scrapy.http import Request
class crawlPipeline(object):
    pass

class imagePipelilne(images.ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        beg = url.rfind('/') + 1
        end = url.rfind('.')
        if end == -1:
            return f'full/{url[beg:]}.jpg'
        else:
            return f'full/{url[beg:end]}.jpg'

class imagerefererPipelilne(images.ImagesPipeline):
    def get_media_requests(self, item, info):
        requests = super().get_media_requests(item, info)
        for req in requests:
            req.headers.appendlist("referer", item['referer'])
        return requests