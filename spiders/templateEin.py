#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   templateEin.py
@Time    :   2019/03/23 16:26:40
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..rules import rules
from ..utils import get_config
from ..itemloader import *
from ..items import *
from .. import urls


class TemplateeinSpider(CrawlSpider):
    
    """mainly for debug the rules of crawler
    
    Attributes:
        name: template's name, not change

    other details see scrapy documention
    """

    name = 'templateEin'

    def __init__(self, *args, **kwargs):
        """initialize all params from configs/xxx.json file


        other details see scrapy
        """

        # main problem:
        # custom_settings 在对象生成时就已有，无法修改，先于__init__方法

        self._name = kwargs.get('_name',self.name)   #建议考虑scrapyd 从此处获取spider名
        config = get_config(self._name)
        self._config = config
        #self.custom_settings = config.get('settings')   #自定义settings覆盖(无用)
        self.logger.info('Show the custom_settings %s', str(self.custom_settings))

        # 获取rules, allowed_domains, start_urls
        self.rules = rules.get(config.get('rules'),()) #建议rules 通用化
        
        self.allowed_domains = config.get('allowed_domains',[])

        start_urls = config.get('start_urls',{})
        if start_urls.get('type') == 'static':
            self.start_urls = start_urls.get('value',[])
        elif start_urls.get('type') == 'dynamic':
            self.start_urls = list(eval('urls.' + start_urls.get('method'))(**start_urls.get('args',{})))
        #print(self.rules)

        # for _compile_rules
        super(TemplateeinSpider, self).__init__(*args,**kwargs)


    def parse_start_url(self,response):
        '''process start_urls
        
        start_urls not processed by parse_item due to rules and default settings
        '''
        if self._config.get("start_urls").get("need_process",None):
            return self.parse_item(response) #return never yield
        return [] #return never yield

    def parse_item(self, response):
        '''parse detail pages

        1).crawl title, date, date, description,... through rules in xxx.json
        2).use loader to execute rules. default functions include :add_xpath,add_value,add_css.
            more see scrapy;
        3).customize loader in itemloader.py for more function!
        '''
        item = self._config.get('item')
        if item:
            univer_cls =eval(item.get('class'))()
            loader = eval(item.get('loader'))(univer_cls, response=response)

            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'),**{'re': extractor.get('re')})
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'),**{'re': extractor.get('re')})
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'),**{'re': extractor.get('re')})
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')),**{'re': extractor.get('re')})
                    # mainly for current datetime       
                    if extractor.get('method') == 'func':
                        loader.add_value(key, *eval('urls.' + str(extractor.get('args')[0]))(**extractor.get('kwargs',{})),**{'re': extractor.get('re')})
            yield loader.load_item()

