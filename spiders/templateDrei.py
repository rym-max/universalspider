#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   templateDrei.py
@Time    :   2019/08/29 13:55:42
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   bloom and new configs get method
@memo    :   get方法----rym
'''

# here put the import lib

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#change 1
# get project settings
from scrapy.utils.project import get_project_settings

# from ..rules import rules #get rules from sql server
from ..utils import get_bloom, set_bloom


from ..utils import (get_spider_configV4,get_spider_ruleV4,
    get_last_crawl_date,set_last_crawl_date)
from ..utils import set_start_action,set_stop_action,set_error_action

from ..itemloader import *
from ..items import *
from ..urls import get_start_urls
from ..errors import PathNotFoundException

import os
import json

from ..filters.bloomfilter import Bloomfilter

class TemplatedreiSpider(CrawlSpider):

    """ version 3.0
    main change:
    1.bloomfilter
    2.more settings to decide start spider

    """

    name = "templateDrei"

    def __init__(self,*args,**kwargs):
        """init all params & interact with db 
        --params list as follow
        1.[self]_name:spider_item_name/name:spider_config_name|project_spider_name
        2.[self]_config: include project_spider_config & custom_config
        3.settings: project & custom
        4.[self]last_crawl_date: according to _name
        5.[self]bloomfilter : according to website/spider_name
        6.[self]rules : just project_spider_config
        7.[self]allowed_domains : from config
        8.[self]timezone: from config, for judge date
        9.[self]starturls: user v2 function
        10.[self]current_date
        11.[self]user/ip/spider_id : from kwargs
        --interact list as follow
        1.get_spider_config
        2.get_spider_rule
        3.get_last_crawl_date
        4.set_last_crawl_date
        5.set_start_action
        """
        #params 1
        self._name = kwargs.get('_name', self.name)

        #params 2/interact 1
        project_spider_config = get_spider_configV4(self.name,self.logger)
        self.logger.debug("<<<spider config origin:\r\n"+str(project_spider_config))
        try:
            custom_config = json.loads(kwargs.get("CUSTOM_CONFIG","{}"))
        except:
            self.logger.warn("CUSTOM_CONIG string type wrong, please check if json!")
            custom_config ={}
        self._config = project_spider_config
        project_spider_config.update(custom_config)
        self.logger.debug("<<<spider config with custom:\r\n"+str(self._config))
        #params 3
        project_settings = get_project_settings().copy()
        try:
            custom_settings = json.loads(kwargs.get("CUSTOM_SETTINGS","{}"))
        except:
            self.logger.warn("CUSTOM_SETTINGS string type wrong, please check if json!")
            custom_settings ={}
        settings = project_settings
        project_settings.update(custom_settings)
        self.logger.debug("<<<spider config:\r\n"+str(settings))
        #params 4/interact 3
        success, self.last_crawl_date = get_last_crawl_date(self._name,self.logger)
        self.logger.info("LAST_CRAWL_DATE: %s" % self.last_crawl_date)

        #params 5
        self.bloomfilter = None
        if self._config.get("NEED_BLOOM",False):
            self.bloom_path = settings.get("BLOOM_PATH",
                self._config.get("BLOOM_PATH",None))
            self.website = self._config.get("WEBSITE",self.name)
            self.bloomfilter, self.bloomname = get_bloom(self.bloom_path,\
                self.website,self.last_crawl_date,self.logger)
            self.logger.debug("Bloom Type:"+str(self.bloomfilter)+"----------"+str(self.bloomname))
            self.logger.debug("BLOOM TYPE: "+str(isinstance(self.bloomfilter, Bloomfilter)))
            self.logger.info("BLOOM INIT Success ,Name:"+str(self.bloomname))
        else:    
            self.logger.info("NOT USE BLOOM !")

        #params 6/interact 2
        self.rules = get_spider_ruleV4(self.name,self.logger)

        #params 7
        self.allowed_domains = self._config.get('allowed_domains',[])

        #params 8
        self.timezone = self._config.get('timezone',8)

        #params 9
        start_urls_params = self._config.get("start_urls",{})
        if start_urls_params:
            Case = start_urls_params.get("case",10)
            Kwargs = start_urls_params.get("Kwargs",{})
            self.start_urls = get_start_urls(self.last_crawl_date,self.timezone,
                Case,self.logger,**Kwargs)
            self.logger.debug("start_urls<<<<<<<"+str(self.start_urls))
        else:
            self.start_urls = []
        self.logger.info("START_URLS INIT Success!")

        #params 10/interact 4
        if success:
            success, self.current_date = set_last_crawl_date(self._name,self.logger)

        #params 11/interact 5
        self.user=kwargs.get("user","AUTO")
        self.ip=kwargs.get("ip","127.0.0.1")
        self.spider_id=kwargs.get("spider_id",0)
        if not success:
            result={
                "success":0,
                "reason":"init spider wrong"
            }
            result = json.dumps(result)
        else:
            result = ""

        if self.user != "AUTO":
            action="USER_RUN"
        else:
            action="AUTO_RUN"

        if success:
            set_start_action(self._name,self.spider_id, self.logger,
                self.user,self.ip,action,result)
        else:
            set_error_action(self._name,self.spider_id, self.logger,
                self.user,self.ip,action,result)

        # for _compile_rules
        super(TemplatedreiSpider, self).__init__(*args,**kwargs)
        self.logger.info("Spider Init Success, [Spide Name]:"+self.name+" [Spider Item]:"+self._name)

    def closed(self,reason):
        if self.bloomfilter:
            set_bloom(self.bloomfilter,self.bloom_path+'/'+self.website,self.bloomname,self.logger,spidername=self._name)
        #stop action in pipeline
    
        self.logger.info("Spider closed. [Spider Name]:"+self.name+
            " [Spider Item]:"+self._name+" [reason]:"+str(reason))
    
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


    def add_bloom_to_request(self,request):
        '''add tag in request

        for middleware to check this request need to be filter by bloom
        '''
        request.meta.setdefault("NEED_BLOOM",False)
        return request
    
