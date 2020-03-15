#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pipelines.py
@Time    :   2019/03/23 18:59:28
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import pymysql
import pymssql
from time import strftime
from .utils import judge_date,get_config
import time
from .config_INFO import (DATA_DB, DATA_HOST, DATA_PORT, DATA_PSWD, DATA_USER,
    SQL_DB, SQL_HOST, SQL_PSWD, SQL_USER)
from .configs import corewords

class UniversalspiderPipeline(object):
    def process_item(self, item, spider):
        return item

#原则上一个item对应一个pipeline

class NewsStandPipeline(object):
    '''

    ITEM        : news
    DATABASE    : mysql
    '''


    def process_item(self, item, spider):

        self.item_count +=1
        tag = False
        title = item.get('title','')
        url = item.get('url','')
        text = item.get('text','')
        date_time = item.get('datetime','1970/01/01')
        source = item.get('source','')
        website = item.get('website','')
        category = item.get('category', '')
        author = item.get('author','')
        keywords = item.get('keywords', '')

        if self.filter:
            for ff in self.filter:
                if ff in title or ff in text:
                    tag=True
                    break
        else:
            tag=True  

        if tag:
            self.related_count +=1
            sql = "INSERT INTO "+self.table+" (`title`,`date`,`description`,`source`,`creator`,`subject`,`url`,`attach`,`CategoryId`) "+ \
                "VALUES (%(title)s,%(date)s,%(description)s,%(source)s,%(creator)s,%(subject)s,%(url)s,%(attach)s,%(CategoryId)s)"

            value_item = {
                "title" : title,
                "url" : url,
                "description" : text,
                "date" : date_time,
                "source" : source,
                "subject" : category,
                "creator" : author,
                "attach" :"",
                "CategoryId":1
            }
            try:
                self.cur.execute(sql,value_item)
                self.cnx.commit()
            except Exception as e:
                print(e)

        if not self.last_time:
            self.last_time = time.time()
            self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
            ))
            self.last_related = self.related_count
            self.last_item = self.item_count
        else:
            if time.time()-self.last_time > 60.0:
                
                self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
                ))
                self.last_related = self.related_count
                self.last_item = self.item_count
                self.last_time = time.time()
                    
    
    def open_spider(self, spider):
        '''
            读取配置
        '''
        config = get_config(spider._name)
        self.db = config.get("db","spider_tempnews")
        self.spider_name = config.get("spider_name","default")
        self.table = config.get("table",'news')
        
        #根据语言决定关键词
        language = config.get("language",None)
        if language:
            self.filter = corewords.corewords[language]
        else:
            self.filter = []

        self.cnx = pymysql.connect(host=DATA_HOST,user=DATA_USER,password=DATA_PSWD,db=DATA_DB, charset='utf8mb4')
        self.cur = self.cnx.cursor()
        
        self.logger = spider.logger
        self.item_count = 0
        self.last_item = 0
        self.related_count = 0
        self.last_related = 0
        self.last_time = None


class NewsSQLServerPipeline(object):
    '''

    ITEM        : news
    DATABASE    : SQL SERVER 
    '''

    def process_item(self, item):
                
        title = item.get('title','')
        url = item.get('url','')
        text = item.get('text','')
        date_time = item.get('datetime','1970/01/01')
        source = item.get('source','')
        #website = item.get('website','')
        category = item.get('category', '')
        author = item.get('author','')
        #keywords = item.get('keywords', '')

        if self.filter:
            for ff in self.filter:
                if ff in title or ff in text:
                    tag=True
                    break
        else:
            tag=True  

        if tag:
            sql = "INSERT INTO "+self.table+ " (`title`,`date`,`description`,`source`,`creator`,`subject`,`url`,`attach`,`CategoryId`,`dcdescription`) " + \
                "VALUES (%(title)s,%(date)s,%(description)s,%(source)s,%(creator)s,%(subject)s,%(url)s,%(attach)s,%(CategoryId)s,%(dcdescription)s)"

            value_item = {
                "title" : title,
                "url" : url,
                "description" : text,
                "date" : date_time,
                "source" : source,
                "subject" : category,
                "creator" : author,
                "attach" :"",
                "CategoryId":1,
                "dcdescription":""
            }
            try:
                self.cur.execute(sql,value_item)
                self.cnx.commit()
                self.related_count +=1
            except Exception as e:
                print(e)

        if not self.last_time:
            self.last_time = time.time()
            self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
            ))
            self.last_related = self.related_count
            self.last_item = self.item_count
        else:
            if time.time()-self.last_time > 60.0:
                
                self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
                ))
                self.last_related = self.related_count
                self.last_item = self.item_count
                self.last_time = time.time()    


    def open_spider(self, spider):
        config = get_config(spider._name)
        self.db = config.get("db","Vip_TongJi")
        self.spider_name = config.get("spider_name","default")
        self.table = config.get("table",'temp'+strftime('%Y%m%d%H%M%S')+self.spider_name)#data

        #根据语言决定关键词
        language = config.get("language",None)
        if language:
            self.filter = corewords.corewords[language]
        else:
            self.filter = []

        self.cnx = pymssql.connect(host=SQL_HOST,user=SQL_USER,password=SQL_PSWD,database=SQL_DB)
        self.cur = self.cnx.cursor()
        
        self.logger = spider.logger
        self.item_count = 0
        self.last_item = 0
        self.related_count = 0
        self.last_related = 0
        self.last_time = None





class NewsStandFilterPipeline(object):
    '''filter with last_date

    ITEM        : news
    DATABASE    : mysql
    '''


    def process_item(self, item, spider):

        self.item_count +=1
        tag = False
        title = item.get('title','')
        url = item.get('url','')
        text = item.get('text','')
        source = item.get('source','')
        #website = item.get('website','')
        category = item.get('category', '')
        new_date = item.get('datetime', '1970-1-1 00:00:00')
        author = item.get('author','')
        keywords = item.get('keywords', '')
        dcdescription = item.get('dcdescription',text)
        #spider.logger.debug("<<<<<<<<[item]:%s" % str(item))

        if self.filter:
            for ff in self.filter:
                if re.search(ff,title,re.IGNORECASE) and self.filter_depth >=1:
                    tag=True
                    break
                if re.search(ff,keywords,re.IGNORECASE) and self.filter_depth >=2:
                    tag=True
                    break
                if re.search(ff,text,re.IGNORECASE) and self.filter_depth >=3:
                    tag=True
                    break
        else:
            tag=True  

        news_date, tag_date = judge_date(new_date,self.news_date_formatter,self.last_date, self.timezone)

        if tag and (tag_date or not self.need_filter_date):
            self.related_count +=1
            sql = "INSERT INTO "+self.table+" (`title`,`date`,`description`,`source`,`creator`,`subject`,`url`,`attach`,`CategoryId`,`dcdescription`) "+ \
                "VALUES (%(title)s,%(date)s,%(description)s,%(source)s,%(creator)s,%(subject)s,%(url)s,%(attach)s,%(CategoryId)s,%(dcdescription)s)"

            value_item = {
                "title" : title,
                "url" : url,
                "description" : text,
                "date" : news_date.strftime("%Y-%m-%d"),
                "source" : source,
                "subject" : keywords,
                "creator" : author,
                "attach" :"",
                "CategoryId":1,
                "dcdescription":dcdescription
            }
            try:
                self.cur.execute(sql,value_item)
                self.cnx.commit()
            except Exception as e:
                print(e)

        if not self.last_time:
            self.last_time = time.time()
            self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
            ))
            self.last_related = self.related_count
            self.last_item = self.item_count
        else:
            if time.time()-self.last_time > 60.0:
                
                self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
                ))
                self.last_related = self.related_count
                self.last_item = self.item_count
                self.last_time = time.time()
                    
    
    def open_spider(self, spider):
        '''
            读取配置
        '''
        config = spider._config
        self.db = config.get("db","spider_tempnews")
        self.spider_name = config.get("spider_name","default")
        self.table = config.get("table",'news')
        
        #根据语言决定关键词
        language = config.get("language",None)
        if language:
            self.filter = corewords.corewords[language]
        else:
            self.filter = []

        self.cnx = pymysql.connect(host=DATA_HOST,user=DATA_USER,password=DATA_PSWD,db=DATA_DB, charset='utf8mb4')
        self.cur = self.cnx.cursor()
        
        self.logger = spider.logger
        self.item_count = 0
        self.last_item = 0
        self.related_count = 0
        self.last_related = 0
        self.last_time = None

        self.last_date = spider.last_date
        self.timezone = spider.timezone
        self.news_date_formatter = config.get('date_formatter',["%Y-%m-%d %H:%M:%S"])
        self.need_filter_date = config.get("need_filter_date",True) #日报
        self.filter_depth = config.get("filter_depth",3)

class NewsSQLFilterPipeline(object):
    '''filter date

    ITEM        : news
    DATABASE    : SQL SERVER 
    '''

    def process_item(self, item, spider):

        self.item_count +=1
        tag = False

        title = item.get('title','')
        url = item.get('url','')
        text = item.get('text','')
        date_time = item.get('datetime','1970-01-01 00:00:00')
        source = item.get('source','')
        #website = item.get('website','')
        category = item.get('category', '')
        author = item.get('author','')
        keywords = item.get('keywords', '')
        
        if self.filter:
            for ff in self.filter:
                if ff in title and self.filter_depth >=1:
                    tag=True
                    break
                if ff in keywords and self.filter_depth >=2:
                    tag=True
                    break
                if ff in text and self.filter_depth >=3:
                    tag=True
                    break
        else:
            tag=True  

        news_date, tag_date = judge_date(date_time,self.news_date_formatter,self.last_date, self.timezone)

        if tag and (tag_date or not self.need_filter_date):
            sql = "INSERT INTO "+self.table+ " (`title`,`date`,`description`,`source`,`creator`,`subject`,`url`,`attach`,`CategoryId`,`dcdescription`) " + \
                "VALUES (%(title)s,%(date)s,%(description)s,%(source)s,%(creator)s,%(subject)s,%(url)s,%(attach)s,%(CategoryId)s,%(dcdescription)s)"

            value_item = {
                "title" : title,
                "url" : url,
                "description" : text,
                "date" : news_date.strftime("%Y-%m-%d"),
                "source" : source,
                "subject" : category,
                "creator" : author,
                "attach" :"",
                "CategoryId":1,
                "dcdescription":""
            }
            try:
                self.cur.execute(sql,value_item)
                self.cnx.commit()
                self.related_count +=1
            except Exception as e:
                print(e)

        if not self.last_time:
            self.last_time = time.time()
            self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
            ))
            self.last_related = self.related_count
            self.last_item = self.item_count
        else:
            if time.time()-self.last_time > 60.0:
                
                self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
                ))
                self.last_related = self.related_count
                self.last_item = self.item_count
                self.last_time = time.time()    


    def open_spider(self, spider):
        config = spider._config
        self.db = config.get("db","Vip_TongJi")
        self.spider_name = config.get("spider_name","default")
        self.table = config.get("table","data")#data

        #根据语言决定关键词
        language = config.get("language",None)
        if language:
            self.filter = corewords.corewords[language]
        else:
            self.filter = []

        self.cnx = pymssql.connect(host=SQL_HOST,user=SQL_USER,password=SQL_PSWD,database=SQL_DB)
        self.cur = self.cnx.cursor()
        
        self.logger = spider.logger
        self.item_count = 0
        self.last_item = 0
        self.related_count = 0
        self.last_related = 0
        self.last_time = None

        self.last_date = spider.last_date
        self.timezone = spider.timezone
        self.news_date_formatter = config.get('date_formatter',["%Y-%m-%d %H:%M:%S"])
        self.need_filter_date = config.get("need_filter_date",True) #日报
        self.filter_depth = config.get("filter_depth",3)

#------------version 3---------------
import logging
import json

from .utils import isContain,isGerman
from .utils import get_now_date,dict_XML
from .utils import set_stop_action

class NewsMetaPipeline(object):

    def process_item(self,item,spider):
        '''process item with different validation & prepare item & log details 
        validation as follows:
        1.filter is necessary
        2.date is well
        prepare as follows:
        1.meta value
        2.db item
        '''
        self.item_count += 1
        #if need store
        tag=False

        title = item.get('title','')
        dateissued = item.get('dateissued','1970-01-01 00:00:00')
        subject = item.get('subject',[])
        text = item.get('text','')
        description= item.get('description','')
        source = item.get('source','')
        author = item.get('author',[])
        url = item.get('url','')

        #validation 1
        tag = isContain(text,self.filter)
        #validation 2
        news_date, tag_date = judge_date(dateissued,self.news_date_formatter,self.last_date, self.timezone)
        self.logger.debug("tag<<<<<<<<"+str(tag))
        self.logger.debug("datetag<<<<<<<<<"+str(tag_date))

        if tag and (tag_date or not self.need_filter_date):
        
            self.logger.debug("进来过一次")
            sql_string = "INSERT INTO " + self.table + \
                " (ChannelId,CategoryId,MetadataValue,IsGermany,Sort,Click,Status,IsSolr,CreateTime,ModifyTime) "+\
                " VALUES "+\
                " (%(channel)s,%(category)s,%(metadata)s,%(isGermany)s,0,0,0,1,%(create)s,%(create)s)"
            #prepare 1
            metavalue ={
                "dc.title":title,
                "dc.date.issued":news_date.strftime("%Y-%m-%d"),
                "dc.subject":subject,
                "dc.description":description,
                "dc.source":source,
                "dc.author":author,
                "dc.url":url,
                "dc.language":self.language
            }
            #prepare 2
            value_item = {
                "channel":self.channel,
                "category":self.category,
                "metadata":dict_XML(metavalue,field_name ="field"),
                "isGermany":self.isGerman or isGerman(text,self.language),
                "create":get_now_date()
            }

            try:
                self.cur.execute(sql_string,value_item)
                self.cnx.commit()
                self.related_count +=1
            except Exception as e:
                self.logger.warn("insert one item error,reason:"+str(e))

        self._log_for_once()


    def _log_for_once(self):
        if not self.last_time:
            self.last_time = time.time()
            self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
            ))
            self.last_related = self.related_count
            self.last_item = self.item_count
        else:
            if time.time()-self.last_time > 60.0:
                
                self.logger.info("Crawled %d pages (at %d pages/min), scraped %d items (at %d items/min)" %(
                    int(self.item_count),int(self.item_count-self.last_item),int(self.related_count),int(self.related_count-self.last_related)
                ))
                self.last_related = self.related_count
                self.last_item = self.item_count
    
    def open_spider(self,spider):
        '''init pipeline version 3
        init params
        params list as followw
        1.db config
        2.db connect
        3.isGerman
        4.language & filter & filter params
        5.logger & log result
        6.date judge params
        7.ERMS detail
        '''
        #param 1
        config = spider._config

        #param 2
        # self.db = config.get("db","Vip_TongJi") banned
        self.spider_name = config.get("spider_name",spider._name)
        self.table = config.get("table","ERMS_All")#data

        self.cnx = pymssql.connect(host=DATA_HOST,user=DATA_USER,password=DATA_PSWD,database=DATA_DB)
        self.cur = self.cnx.cursor()

        #param 3
        # self.isGerman = False
        self.isGerman = config.get("isGerman",False)
        #param 4
        self.language = config.get("language",None)
        if self.language:
            self.filter = corewords.corewords[self.language]
            if self.language == "GERMAN":
                self.isGerman = True
        else:
            self.filter = []
        self.filter_depth = config.get("filter_depth",3)

        #param 5
        self.logger = logging.getLogger(self.spider_name+".NewsMetaPipeline")
        self.item_count = 0
        self.last_item = 0
        self.related_count = 0
        self.last_related = 0
        self.last_time = None

        #param 6
        self.last_date = spider.last_crawl_date
        self.timezone = spider.timezone
        self.news_date_formatter = config.get('date_formatter',["%Y-%m-%d %H:%M:%S"])
        
        self.need_filter_date = config.get("need_filter_date",True) or \
            spider.bloom_path == None
        #param 7
        self.channel = config.get("channel",1)
        self.category = config.get("category",1)

    def close_spider(self,spider):
        '''when spider stop 
        '''
        self.logger.info("prepare to stop pipeline ---" + "NewsMetaPipeline")
        
        #先不管中断问题
        result_item ={
            "success":1,
            "reason":"Crawl finished",
            "result":{
                "crawl_page":self.item_count,
                "crawl_item":self.related_count
            }
        }

        result_str = json.dumps(result_item)
        
        set_stop_action(spider._name,spider.spider_id,self.logger,user=spider.user,ip=spider.ip,result=result_str)



#------------------------------version4------------------------------
class JournalMetaPipeline(NewsMetaPipeline):

    def process_item(self,item,spider):
        '''JORRNAL VERSION
        '''
        self.item_count += 1
        #if need store
        tag=False

        title = item.get('title','')
        text = item.get('text','')
        description= item.get('description','')
        author = item.get('author',[])
        dateissued = item.get('dateissued','1970')
        organ = item.get('organ',[])
        source = item.get('source','')
        start = item.get('start',"1970")
        num = item.get('num',"1")
        url = item.get('url','')
        subject = subject = item.get('subject',[])
        _class = item.get('_class','')

        
        #validation 1
        tag = True
        # #validation 2
        # news_date, tag_date = judge_date(dateissued,self.news_date_formatter,self.last_date, self.timezone)
        tag_date = True

        self.logger.debug("tag<<<<<<<<"+str(tag))
        self.logger.debug("datetag<<<<<<<<<"+str(tag_date))

        if tag and (tag_date or not self.need_filter_date):
        
            self.logger.debug("进来过一次")
            sql_string = "INSERT INTO " + self.table + \
                " (ChannelId,CategoryId,MetadataValue,IsGermany,Sort,Click,Status,IsSolr,CreateTime,ModifyTime) "+\
                " VALUES "+\
                " (%(channel)s,%(category)s,%(metadata)s,%(isGermany)s,0,0,0,1,%(create)s,%(create)s)"
            #prepare 1
            metavalue ={
                "dc.title":title,
                "dc.date.issued":dateissued,
                "dc.date.year":dateissued,
                "dc.subject":subject,
                "dc.description":description,
                "dc.creator":author,
                "dc.url":url,
                "dc.language":self.language,
                "dc.organ":organ,
                "dc.vol":self.calculate_vol(start,dateissued),
                "dc.num":num,
                "dc.title.name":source,
                "dc.class":_class
            }
            #prepare 2
            value_item = {
                "channel":self.channel,
                "category":self.category,
                "metadata":dict_XML(metavalue,field_name ="field"),
                "isGermany":self.isGerman,
                "create":get_now_date()
            }

            try:
                self.cur.execute(sql_string,value_item)
                self.cnx.commit()
                self.related_count +=1
            except Exception as e:
                self.logger.warn("insert one item error,reason:"+str(e))

        self._log_for_once()
    
    def calculate_vol(self,start,year):
        # 无start字段，year如14 November 2019
        self.logger.debug(year)
        self.logger.debug(start)
        if int(start)==1970 and not year.isdigit():
            self.logger.debug("进入到if循环")
            result = re.split(" ",year)
            return result[-1]
        else:
            self.logger.debug("进入else循环")
            return str(int(year)-int(start)+1)