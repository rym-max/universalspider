#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   middlewares.py
@Time    :   2019/03/23 18:58:45
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from .errors import PathNotFoundException
from scrapy.exceptions import IgnoreRequest
import os


class UniversalspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UniversalspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class BloomFilterMiddlewares(object):

    @classmethod
    def from_crawler(cls,crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def process_request(self,request,spider):
        configs = spider._config
        need_bloom_config = configs.get("NEED_BLOOM", False)
        need_bloom_url = request.meta.get("NEED_BLOOM",True)
        need_bloom_start_url = configs.get("start_url_need_bloom",False)
        
        url = request.url
        if url in spider.start_urls and not need_bloom_start_url:
            return None
        
        if need_bloom_config and need_bloom_url:
            sbf = spider.bloomfilter
            if sbf != None:
                url = request.url
                if sbf.check(url):
                    spider.logger.debug("<<<<<<<<[debug]:url already crawled:\n%s" % url)
                    raise IgnoreRequest

        return None
    
    def process_response(self,request,response,spider):
        configs = spider._config
        need_bloom_config = configs.get("NEED_BLOOM", False)
        need_bloom_url = request.meta.get("NEED_BLOOM",True)
        need_bloom_start_url = configs.get("start_url_need_bloom",False)
        
        url = request.url
        if url in spider.start_urls and not need_bloom_start_url:
            return response

        if need_bloom_config and need_bloom_url:
            sbf = spider.bloomfilter
            if sbf != None:
                url = request.url
                sbf.add_in_sbf(url)
        
        return response
        
        
