#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2019/03/23 19:19:21
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   
'''

import datetime
import json
import re
from collections import defaultdict
from csv import reader
from os.path import dirname, realpath
from .configs.V2_corewords import corewords
import os
import pickle
import time
#from .configs.configs import configs
import pymysql
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

import pymssql
from .config_INFO import (CONFIG_DB, CONFIG_HOST, CONFIG_PORT, CONFIG_PSWD,
    CONFIG_TABLE, CONFIG_USER,SPIDER_ITEM_TABLE,SPIDER_CONFIG_TABLE,
    SPIDER_LOG_TABLE)
from .errors import PathNotFoundException
from .filters.bloomfilter import Bloomfilter
import logging

default_logger = logging.getLogger('UTILS_DEFAULT_LOGGER')

def get_date_withzone(tt,timezone=8):
    now_time_zone = 8
    seconds_difference = (timezone - now_time_zone) * 3600
    return tt - datetime.timedelta(0, seconds_difference, 0)


# def get_config(name):
#     '''get configs from .py file

#     due to scrapyd cannot read json file in egg package
#     '''
#     return configs.get(name,{})

def get_config(name):
    '''get config from .json file

    mainly for debug
    '''
    if name:
        print(realpath(__file__))
        path = dirname(realpath(__file__))+'\\configs\\'+name+'.json'
        with open(path,'r', encoding='utf8') as f:
            return json.loads(f.read())
    else:
        return {}

def get_configs(name,logger=default_logger):
    '''get config from mysql database

    annoying to always change configs.py 
    '''
    #pymysql!!!
    try:
        cnx = pymysql.connect(host=CONFIG_HOST, user=CONFIG_USER,
            password=CONFIG_PSWD, db=CONFIG_DB, charset="utf8mb4")
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<<[connection error]:%s" % str(e))
        return {}

    sql_string = r"SELECT configs FROM " + CONFIG_TABLE + " WHERE name=%(name)s"
    item = {
        "name":name
    }

    try:
        result = cur.execute(sql_string,item)
    except Exception as e:
        logger.warn("<<<<[query error]:%s" % str(e))
        return {}
    else:
        if result:
            config_string = cur.fetchone()[0]
            config = json.loads(config_string)
            cnx.close()
            return config
        else:
            cnx.close()
            return {}

def get_rules(name,logger=default_logger):
    '''get rules from mysql database

        rule={
            "item":[
                {
                    "linkextra":{
                        "allow":
                        "deny":
                        "restrict_xpath":
                        "restrict_css":
                    },
                    "follow":
                    "callback":
                }
            ]
        }
    '''
    #pymysql!!!
    try:
        cnx = pymysql.connect(host=CONFIG_HOST, user=CONFIG_USER,
            password=CONFIG_PSWD, db=CONFIG_DB, charset="utf8mb4")
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<<[connection error]:%s" % str(e))
        return {}

    sql_string = r"SELECT rules FROM " + CONFIG_TABLE + " WHERE name=%(name)s"
    item = {
        "name":name
    }

    try:
        result = cur.execute(sql_string,item)
    except Exception as e:
        logger.warn("<<<<[query error]:%s" % str(e))
        return {}
    else:
        if result:
            rule_string = cur.fetchone()[0]
            rules = json.loads(rule_string)
            rrs = []
            for r in rules.get("item",()):
                l = r["linkextra"]
                allow = l["allow"] if l["allow"] else ()
                deny = l["deny"] if l["deny"] else ()
                res_xp = l["restrict_xpath"] if l["restrict_xpath"] else ()
                res_cs = l["restrict_css"] if l["restrict_css"] else ()
                follow = r["follow"] if r["follow"] else None
                callback = r["callback"] if r["callback"] else None
                newR = Rule(LinkExtractor(allow=allow, deny=deny, 
                    restrict_xpaths=res_xp, restrict_css=res_cs), 
                    callback=callback, follow=follow)
                rrs.append(newR)
            cnx.close()
            return rrs
        else:
            cnx.close()
            return () 

def get_dates(name,logger=default_logger):
    '''get lastdate from mysql database

    '''
    #pymysql!!!
    try:
        cnx = pymysql.connect(host=CONFIG_HOST, user=CONFIG_USER,
            password=CONFIG_PSWD, db=CONFIG_DB, charset="utf8mb4")
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<<[connection error]:%s" % str(e))
        return {}
    
    sql_string = r"SELECT datelast FROM " + CONFIG_TABLE + " WHERE name=%(name)s"
    item = {
        "name":name
    }

    try:
        result = cur.execute(sql_string,item)
    except Exception as e:
        logger.warn("<<<<[query error]:%s" % str(e))
        return None
    else:
        if result:
            date_string = cur.fetchone()[0]
            cnx.close()
            return date_string
        else:
            cnx.close()
            return None

def set_dates(name, date=None, logger=default_logger):
    '''set current date in database

        date str %Y-%m-%d %H:%M:%S
    '''
    #pymysql!!!
    try:
        cnx = pymysql.connect(host=CONFIG_HOST, user=CONFIG_USER,
            password=CONFIG_PSWD, db=CONFIG_DB, charset="utf8mb4")
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<<[connection error]:%s" % str(e))
        return None
    #sql server

    #mysql
    sql_string = r"UPDATE " + CONFIG_TABLE + r" SET datelast=%(date)s WHERE name=%(name)s"
    
    #name & date
    current_date = datetime.datetime.now()

    item = {
        "name":name,
        "date":date if date else current_date.strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        cur.execute(sql_string,item)
        cnx.commit()
    except Exception as e:
        logger.warn("<<<<[change error]:%s" % str(e))
        return None
    else:
        cnx.close()
        return current_date

def judge_date(news_date,news_date_formatter=["%Y-%m-%d %H:%M:%S"],last_date=None,timezone=8,logger=default_logger):
    '''judge date of the news is after last_date
    
    '''
    dd = None
    for ff in news_date_formatter:
        try: 
            dd = datetime.datetime.strptime(news_date,ff)
        except Exception:
            pass
        else:
            break
    if dd:
        if dd > last_date - datetime.timedelta(0,3600*(8-timezone)):
            default_logger.info("<<<date true："+str(dd))
            return dd,True
        else:
            default_logger.info("<<<date false："+str(dd))
            return dd,False
    
    logger.warn("<<<<[warn]:error in date decode %s" % str(news_date))
    return None,False

def get_keyword(file):
    '''read file as keywords

    may use some search engine to search for data

    '''
    path = dirname(realpath(__file__)) + '\\files\\' + file
    with open(path,'r',encoding='gbk') as f:
        csv_reader = reader(f)
        target_name = defaultdict(list)
        keywordlist = []
        line_num = 1
        for line in csv_reader:
            
            #首项关键词判断别名和长名
            name = line[0].replace(')',"").replace('）',"").replace('(',"/").replace('（',"/").replace("、","/").replace('\\',"/").split("/")
            for nn in name:
                target_name[nn].append(line_num)
            
            if line[1:]:
                wordslist = []
                for words in line[1:]:
                    wordslist.extend(words.replace("/"," ").replace("、"," ").split(" "))
                keywordlist.append(wordslist)
            
            line_num += 1

    return target_name,keywordlist

#make request
import requests

session = requests.Session()
session.headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip,deflate,br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
}

def make_request(url, logger, rtype="html", data=None, timeout=60, encode="utf8",**kwargs):
    r_json = {}
    try:
        if data:
            r = session.post(url, data=data, timeout=timeout)
        else:
            r = session.get(url, timeout=timeout)
        r.encoding = encode
    except Exception as err:
        logger.warn("<<<<<[%s] request error, [message]: \n\r<<<<<<%s" % (url, str(err)))
        return -1, {}
    else:
        if rtype == "json":
            try:
                r_json = r.json()
            except json.JSONDecodeError as e: 
                logger.debug("<<<<<<[%s] :\n\r <<<<<<decode error:cannot decode json directly \n\r <<<<<<%s \n\r <<<<<%s" % (url, str(e),r.text))
            else:
                return r.status_code, r_json
            finally:    
                if kwargs.get("json_formatter",""):
                    pattern = kwargs.get("json_formatter","")
                    json_str = re.search(pattern,r.text,re.DOTALL).group()
                    logger.debug("<<<<<<<results: %s" % str(json_str))
                    r_json = json.loads(json_str)
                    logger.debug("result pages:<<<< %s" % str(r_json))
                else:
                    r_json = {}
                return r.status_code,r_json
            
        elif rtype == "xml":
            return r.status_code, r.text
        elif rtype == "html":
            return r.status_code, r.text
        else:
            return r.status_code, r.text


def json_dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=4, sort_keys=True)

"""
BloomFilter 相关
"""

def get_bloom(prepath,spider_name,last_date,logger,*args,**kwargs):
    #先判断prepath是否存在
    if not prepath:
        logger.error("<<<<<<[error]:BloomFilter文件夹未设置 -----")
        raise PathNotFoundException(path=prepath)
    else:
        #文件夹是否能访问
        if not os.path.isdir(prepath):
            try:
                os.mkdir(prepath)
            except:
                logger.error("<<<<<<[error]:无法创建BloomFilter文件夹 -----"+prepath)
                raise PathNotFoundException(path=prepath)
    #判断spider_name文件夹是否存在
    spider_path = prepath+'/'+spider_name
    if not os.path.isdir(spider_path):
        try:
            os.mkdir(spider_path)
        except:
            logger.error("<<<<<<[error]:无法创建对应spider的BloomFilter文件夹 -----"+spider_path)
            raise PathNotFoundException(path=spider_path)
    
    #遍历当前文件夹下文件
    dir_li = os.listdir(spider_path)
    latest_Date = None
    target_file = None
    logger.error("要命<<<<<<<<<<<<<<<"+str(dir_li))
    if dir_li:
       
        
        for fname in dir_li:
            fn_li = fname.split(".")
            logger.error("要命<<<<<<<<<<<<<<<"+str(fn_li))
            if fn_li[-1]=='pkl':#后缀名为pkl
                p_date_str_li = fn_li[0].split("_")
                try:
                    #转化为时间
                    p_date = datetime.datetime.strptime(p_date_str_li[-1],"%Y-%m-%d %H-%M-%S")
                    if p_date!=None:
                        latest_Date = p_date if (latest_Date == None or latest_Date < p_date) else latest_Date
                        target_file= fname if (latest_Date == p_date) else target_file
                except:
                    logger.info("<<<<<<<<<<<<<<<<<<<<<pickle文件名错误")
        
        #判断时间是否超过，默认时间为24月*30=720天，鬼知道以后还用不用
        time_duration = kwargs.get("",720)
        days_delta = datetime.timedelta(time_duration,0,0)
        if latest_Date and datetime.datetime.now()-latest_Date < days_delta:
            #读取pickle，并设置logger
            #read_sbf=Bloomfilter()
            if os.path.getsize(spider_path+'/'+target_file)>0:#文件不能为空
                f = open(spider_path+'/'+target_file,'rb')
                read_sbf = pickle.load(f)
                read_sbf.setlogger(spider_name)

                sbf_filename = target_file
                f.close()
                return read_sbf, sbf_filename
        
    #是否需要删除
    if target_file:
        need_delete = kwargs.get("NEED_DELETE_BLOOM",False)
        if need_delete:
            reason = "Latest BloomFilter Need to be Deleted"
            delete_file(spider_path+'/'+target_file, logger=logger, reason=reason)
            
        
    #else:
        #文件夹下为空，直接创建一个新的bloomfilter
    #超过特定时间长度，决定重新创建
    new_sbf = Bloomfilter(spider_name)
    logger.debug("create one bloom："+str(new_sbf))
    return new_sbf, None

def set_bloom(bloomF,bloompath=None,bloomname=None,logger=default_logger,create_Date=False,*args,**kwargs):
    """
    params:不解释
    desc:pickle文件日期格式
    spidername_YYYY-mm-dd HH:MM:SS.pickle
    """
    logger.info(bloomF)
    if not isinstance(bloomF, Bloomfilter):
        logger.error("<<<<<<<<<<<<<<<[error]:传入了错误格式的bloomfilter")
        raise ValueError
    if bloompath == None:
        logger.error("<<<<<<<<<<<<<<<[error]:bloomfilter根目录路径为空")
        raise ValueError
    filename = None


    #判断bloomname格式
    if bloomname==None:
        create_Date = True

    spider_name = kwargs.get("spidername","TEMPORARY")
    if not create_Date:
        if bloomname != None:
            re_pattern  = r"_\d+-\d+-\d+ \d+-\d+-\d+\.pkl"
            if re.search(re_pattern, bloomname):
                filename = bloomname
                logger.info("<<<<<<<[info]:target bloom")
            else:
                logger.warn("<<<<<<<[warning]:文件格式错误")
    
    if filename == None:
        now_time = datetime.datetime.now()
        filename = now_time.strftime(spider_name+"_%Y-%m-%d %H-%M-%S.pkl")
    try:
        f = open(bloompath +'/'+ filename,'wb')
        bloomF.clearlogger()
        pickle.dump(bloomF,f)
        f.close()
    except Exception as e:
        logger.error("<<<<<<<<<[error]存储bloomfilter错误,%s" % str(e))
    else:
        logger.info("<<<<<<<<<[info]成功存储bloomfilter")


def delete_file(filepath,logger=default_logger,reason='Delete'):
    try:
        os.remove(filepath)
    except Exception as e:
        logger.error("Failed to Delete File'" + filepath + "', [Error]:" + str(e))
    else:
        logger.info("Successfully Delete File '" + filepath + "', [Reason]:"+ reason)

#-------------------------version 3--------
def get_spider_config(name,logger=default_logger):
    '''get configs from sql server table
    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V3 in get config]:%s"%str(e))
        return {}

    sql_string = r"SELECT Configs FROM " + SPIDER_CONFIG_TABLE +" WHERE name=%(name)s"
    item = {
        "name":name
    }

    try:
        cur.execute(sql_string,item)
        result = cur.fetchone()[0]
    except Exception as e:
        logger.error("<<<[query error V3 in get config]:%s"%str(e))
        return {}
    else:
        if result:
            config = json.loads(result)
            cnx.close()
            logger.debug("<<<[success in get config V3] \r\n"+str(config))
            return config
        else:
            cnx.close()
            return {}

def get_spider_rule(name,logger=default_logger):
    '''get rules from sqlserver database

        rule={
            "item":[
                {
                    "linkextra":{
                        "allow":
                        "deny":
                        "restrict_xpath":
                        "restrict_css":
                    },
                    "follow":
                    "callback":
                }
            ]
        }
    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V3 in get RULE]:%s"%str(e))
        return {}
    
    sql_string = r"SELECT Rules FROM "+ SPIDER_CONFIG_TABLE + " WHERE name=%(name)s"
    item = {
        "name":name
    }

    try:
        cur.execute(sql_string,item)
        result = cur.fetchone()[0]
    except Exception as e:
        logger.warn("<<<<[query error V3 in get RULE]:%s" % str(e))
        return ()
    else:
        if result:
            rules = json.loads(result)
            rrs = []
            for r in rules.get("item",()):
                l = r["linkextra"]
                allow = l["allow"] if l["allow"] else ()
                deny = l["deny"] if l["deny"] else ()
                res_xp = l["restrict_xpath"] if l["restrict_xpath"] else ()
                res_cs = l["restrict_css"] if l["restrict_css"] else ()
                follow = r["follow"] if r["follow"] else None
                callback = r["callback"] if r["callback"] else None
                newR = Rule(LinkExtractor(allow=allow, deny=deny, 
                    restrict_xpaths=res_xp, restrict_css=res_cs), 
                    callback=callback, follow=follow)
                rrs.append(newR)
            cnx.close()
            return rrs
        else:
            cnx.close()
            return () 


def get_last_crawl_date(name,logger=default_logger):
    '''get last crawl date & status from sql server table

        status: 0:finished;2:suspending;3:runnning;5:error;

    return:
        success: boolean
        last_crawl_date : datetime.datetime/None
    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V3 in get RULE]:%s" % str(e))
        return False,None

    sql_string = r"SELECT LastCrawlDate,Status FROM " +SPIDER_ITEM_TABLE + " WHERE name=%(name)s"
    item = {
        "name":name
    }
    #循环以保证从suspending 状态启动,多次循环不成功放弃
    
    try:
        for _ in range(10):
            cur.execute(sql_string,item)
            result = cur.fetchone()
            # if True:#debug
            #     break
            if not result or result[1] == 2:
                break
            time.sleep(5)
    except Exception as e:
        logger.error("<<<[query error V3 in get crawl date]:%s" % str(e))
        cnx.close()
        return False,None
    else:
        cnx.close()
        if not result:
            logger.error("<<<[query error V3 in get crawl date]:no specific spider")
            return False,None
        
        if result[0]:
            logger.info("<<<[query success V3 in get crawl date]:last one,"+str(result[0]))
            return True, result[0]
        else:
            logger.info("<<<[query success V3 in get crawl date]:new one,")
            return True, datetime.datetime.now()
    

def set_last_crawl_date(name,logger=default_logger):
    '''set last crawl date in sql server
    
    return:
    success: bool
    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V3 in get RULE]:%s" % str(e))
        return False,None

    sql_string = r"UPDATE " + SPIDER_ITEM_TABLE + " SET LastCrawlDate=%(crawldate)s WHERE name=%(name)s"
    item = {
        "crawldate":datetime.datetime.now(),
        "name":name
    }

    try:
        cur.execute(sql_string,item)
        cnx.commit()
    except Exception as e:
        logger.error("<<<[update error V3 in set crawl date]:%s" % str(e))
        cnx.close()
        return False, None
    else:
        logger.info("<<<[update success V3 in set crawl date]")
        cnx.close()
        return True, item["crawldate"]

#-------------------------version 4--------
def get_spider_configV4(name,logger=default_logger):
    '''
    1.get spider_item from table for ConfigId
    2.get spider_config from table for Config with ConfigId Id
    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V4 in get config]:%s"%str(e))
        return {}

    sql_string = r"SELECT ConfigId FROM " + SPIDER_ITEM_TABLE +" WHERE name=%(name)s"
    item = {
        "name":name
    }

    sql_string_for_config = r"SELECT Configs FROM " + SPIDER_CONFIG_TABLE +" WHERE Id=%(config)s"

    try:
        cur.execute(sql_string,item)
        ConfigId = cur.fetchone()[0]
        cur.execute(sql_string_for_config,{"config":str(ConfigId)})
        result = cur.fetchone()[0]
    except Exception as e:
        logger.error("<<<[query error V4 in get config]:%s"%str(e))
        return {}
    else:
        if result:
            config = json.loads(result)
            cnx.close()
            logger.debug("<<<[success in get config V4] \r\n"+str(config))
            return config
        else:
            cnx.close()
            return {}



def get_spider_ruleV4(name,logger=default_logger):
    '''
    1.get spider_item from table for ConfigId
    2.get spider_config from table for Config with ConfigId Id
    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V4 in get RULE]:%s"%str(e))
        return {}
    
    
    sql_string = r"SELECT ConfigId FROM " + SPIDER_ITEM_TABLE +" WHERE name=%(name)s"
    item = {
        "name":name
    }
    sql_string_for_config = r"SELECT Rules FROM " + SPIDER_CONFIG_TABLE +" WHERE Id=%(config)s"

    try:
        cur.execute(sql_string,item)
        ConfigId = cur.fetchone()[0]
        cur.execute(sql_string_for_config,{"config":str(ConfigId)})
        result = cur.fetchone()[0]
    except Exception as e:
        logger.warn("<<<<[query error V4 in get RULE]:%s" % str(e))
        return ()
    else:
        if result:
            rules = json.loads(result)
            rrs = []
            for r in rules.get("item",()):
                l = r["linkextra"]
                allow = l["allow"] if l["allow"] else ()
                deny = l["deny"] if l["deny"] else ()
                res_xp = l["restrict_xpath"] if l["restrict_xpath"] else ()
                res_cs = l["restrict_css"] if l["restrict_css"] else ()
                follow = r["follow"] if r["follow"] else None
                callback = r["callback"] if r["callback"] else None
                newR = Rule(LinkExtractor(allow=allow, deny=deny, 
                    restrict_xpaths=res_xp, restrict_css=res_cs), 
                    callback=callback, follow=follow)
                rrs.append(newR)
            cnx.close()
            return rrs
        else:
            cnx.close()
            return () 




#action
def set_action_details(name,logger=default_logger,**kwargs):
    '''update action details in sql server table
    
    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V3 in set action details]:%s" % str(e))
        return False

    #default
    item = {
        "name":name,
        "result":"",
        "user":"AUTO",
        "action":"AUTO_RUN",
        "actionTime":datetime.datetime.now(),
        "status":3
    }
    item.update(kwargs)


    sql_string = "UPDATE " + SPIDER_ITEM_TABLE + \
        " SET LastActionTime=%(actionTime)s,"+ \
        " LastResult=%(result)s, LastActionUser=%(user)s, " +\
        " LastAction=%(action)s, Status=%(status)d" +\
        " WHERE Name=%(name)s"
    
    try:
        cur.execute(sql_string,item)
        cnx.commit()
    except Exception as e:
        logger.info("<<<[update error V3 in set action details]:" + str(e))
    else:
        logger.info("<<<[update success V3 in set action details]")
    finally:
        cnx.close()

#spider_log
def set_spider_logger(spider_id,logger=default_logger,**kwargs):
    '''insert spider logger

    '''
    #pymssql
    try:
        cnx = pymssql.connect(host=CONFIG_HOST,user=CONFIG_USER,
            password=CONFIG_PSWD, database=CONFIG_DB)
        cur = cnx.cursor()
    except Exception as e:
        logger.error("<<<[connection error V3 in set spider log]:%s" % str(e))
        return False
    
    item = {
        "spider":spider_id,
        "user" : "AUTO",
        "IP"   : "127.0.0.1",
        "action": "AUTO_RUN",
        "result": "",
        "create": datetime.datetime.now() 
    }
    item.update(kwargs)

    sql_string = "INSERT INTO " + SPIDER_LOG_TABLE + \
        " (Spider, ActionUser, IP, Action, Result,CreateTime,ModifyTime) " +\
        "VALUES (%(spider)s,%(user)s,%(IP)s,%(action)s,%(result)s,%(create)s,%(create)s)"

    try:
        cur.execute(sql_string,item)
        cnx.commit()
    except Exception as e:
        logger.info("<<<[insert error V3 in insert spider log]:" + str(e))
    else:
        logger.info("<<<[insert success V3 in insert spider log]")
    finally:
        cnx.close()
    


def set_start_action(name,spider_id,logger=default_logger,user="AUTO",ip="127.0.0.1",action="AUTO_RUN",result=""):
    '''update action & insert spider log

    '''

    item = {
        "user":user,
        "status":3,
        "IP"   :ip,
        "action": action,
        "result": "{'success':1}" if not result else result
    }

    set_action_details(name,logger,**item)
    set_spider_logger(name,logger,**item)

def set_stop_action(name,spider_id,logger=default_logger,user="AUTO",ip="127.0.0.1",action="CRAWL_OVER",result=""):
    '''update action & insert spider log
    '''

    item = {
        "user":user,
        "status":0,
        "IP"   :ip,
        "action": action,
        "result": "{'success':1}" if not result else result
    }

    set_action_details(name,logger,**item)
    set_spider_logger(name,logger,**item)

def set_error_action(name,spider_id,logger=default_logger,user="AUTO",ip="127.0.0.1",action="ERROR",result=""):
    '''
    '''
    item = {
        "user":user,
        "status":5,
        "IP"   :ip,
        "action": action,
        "result": "{'success':1}" if not result else result
    }

    set_action_details(name,logger,**item)
    set_spider_logger(name,logger,**item)

#xml

#re filter
def isContain(text="",filters=[]):
    if text and filters:
        for pa in filters:
            if re.search(pa,text,re.IGNORECASE):
                return True

    return False

#is German 
def isGerman(text,language):
    keywords = {
        "CHINESE":["中德","德国","德方"],
        "GERMAN" :[r"\bGerman\b",r"\bGermany\b"]
    }
    return isContain(text,keywords.get(language,[]))

#date
def get_now_date(input_datestr="",formatter="%Y-%m-%d %H:%M:%S.%f"):
    '''get datetime.datetime from str or now_date
    '''
    if input_datestr:
        return datetime.datetime.strptime(input_datestr,formatter)
    else:
        return datetime.datetime.now()

#xml
import xml.dom.minidom as minidom

def dict_XML(data_dict,*args,**kwargs):
    '''dict to xml
    params:
        data_dict: input dict
        field_name : custom or ''
        multi_split : custom or '' 
    '''
    
    # field_name = kwargs.get("field_name" , "")
    # multi_split = kwargs.get("multi_split" , "")

    doc = minidom.Document()
    rootDoc = doc.createElement("doc")
    doc.appendChild(rootDoc)

    for k,v in data_dict.items():
        if isinstance(v,list):
            for vv in v:
                oneNode = doc.createElement("field")
                oneNode.setAttribute("name",k)
                oneNodeText = doc.createTextNode(vv)
                oneNode.appendChild(oneNodeText)
                rootDoc.appendChild(oneNode)
        else:
            oneNode = doc.createElement("field")
            oneNode.setAttribute("name",k)
            oneNodeText = doc.createTextNode(v)
            oneNode.appendChild(oneNodeText)
            rootDoc.appendChild(oneNode)

    return doc.toprettyxml()


def xml_DICT(data_xml,*args,**kwargs):
    pass
#-------------------------end-----------------
#version2       --rym
def back_core(language):
    """
    :param language: 语言
    :return: 关键词的列表
    """
    word_set = corewords.get(language,"")
    word_list = list(word_set)
    return word_list

def V2_make_request_htm(url,formatter,logger):
    """
    for get html
    :param 请求的url:
    :param formatter: 解析返回json的正则表达式
    like  r'"(url)":"(https://.*?/\d+-.*?\.htm)"' 二维元组
    :return: status_code,详情页url的列表
    暂时fir_result:
    [('url', 'https://politics.gmw.cn/2020-03/14/content_33649378.htm'),...]
    """
    try:
        js_response = requests.get(url)
    except Exception as e:
        logger.warn(e)
    js_text = js_response.text
    pattern = re.compile(formatter)
    fir_result = pattern.findall(js_text)
    detail_url = []
    for i in fir_result:
        detail_url.append(i[1])
    return detail_url







