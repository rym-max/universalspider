#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2019/04/06 11:40:29
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''
import copy

'''
Update

@Time :  2020/3/13
@Author : rym
@version : 2.0

'''


import csv
import re
import requests
import time
import datetime
import json
from os.path import realpath, dirname
from .utils import get_keyword, get_date_withzone, make_request, set_dates,back_core,V2_make_request_htm,V2_make_request_json

#日后再考虑既有page又有keywords
#这部分需重新考虑，完成后删除这条注释
import logging
default_logger = logging.getLogger(__name__)


def fromfunc(formatter,start,end,*args):
    for page in range(start, end+1):
        yield formatter % page


def fromfile(filename,formatter,num,*args):

    path = dirname(realpath(__file__)+'/files/'+filename)
    with open(path,'r',encoding='gbk') as f: #使用csv/excel文件
        csv_reader = csv.reader(f)
        for line in csv_reader:
            yield formatter % tuple(line[0:num])

def fromname(filename,formatter,num,*args):

    target_name, keywords = get_keyword(filename)
    for name in target_name.keys():
        yield formatter % name

def fromajax(url, code1, pattern, re_mode, formatter, group_num, need_unix,**kwargs):
    
    data_response = requests.get(url) #headers之后
    api = re.search(pattern, data_response.content.decode(code1),eval(re_mode)).group(group_num)

    if need_unix:
        yield formatter % (api, int(time.time()))
    else:
        yield formatter % (api)

def fromasp(api,regex,*args):
    pass


#采用
def fromdate(website, formatters,**kwargs):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    times = now_time.split("-")
    value_date ={
        "YYYY":times[0],
        "mm":times[1],
        "dd":times[2],
        "HH":times[3],
        "MM":times[4],
        "SS":times[5],
        "YY":times[0][2:4],
        "m":str(int(times[1])),
        "d":str(int(times[2]))
    }
    value_date.update(kwargs)

    for ff in formatters:
        yield ff % value_date

#采用
def fromjson(url, pattern, code1, re_mode, group_num, formatter, code2, need_unix, key1, key2):
    data_response = requests.get(url) #headers之后
    api = re.search(pattern, data_response.content.decode(code1),eval(re_mode)).group(group_num)

    if need_unix:
        data_json = requests.get(formatter % (api, int(time.time()))).content.decode(code2)
    else:
        data_json = requests.get(formatter % api).content.decode(code2)

    data_dict = json.loads(data_json)

    # print("Look here:",isinstance(data_dict,dict))
    # print(data_dict)
    # for k, v in data_dict.items():
    #     print(k)
    
    for ddd in data_dict.get(key1,[]):
        print(ddd)
        if ddd.get(key2,None) is not None:
            yield ddd.get(key2)

def getdate():
    return [datetime.datetime.now().strftime("%Y-%m-%d")]

#below new util function
def number_strs(digits,number):
    n = int(number)
    if n >= 10 ** (digits-1):
        return str(n)
    n += 10**(digits-1)
    n_l = list(str(n))
    n_l[0]="0"
    return "".join(n_l)

def format_date(date,formatter,**kwargs):
    # default_logger.debug("i'm here 4")
    now_time = date.strftime("%Y-%m-%d-%H-%M-%S")
    yy = date.year
    year_start_time = datetime.datetime(yy,1,1,0,0,0)
    times = now_time.split("-")
    value_date ={
        "YYYY":times[0],
        "mm":times[1],
        "dd":times[2],
        "HH":times[3],
        "MM":times[4],
        "SS":times[5],
        "YY":times[0][2:4],
        "m":str(int(times[1])),
        "d":str(int(times[2])),
        "days": str((date - year_start_time).days + 1),
        "days-1":str((date - year_start_time).days),
        "days3": number_strs(3,(date - year_start_time).days + 1),
        "UNIX":str(int(time.mktime(date.timetuple())))
    }
    value_date.update(kwargs)
    default_logger.debug("i'm here 5")
    default_logger.debug("更新dict后<<<<<"+str(kwargs.get("YYYY","haha")))
    return formatter % value_date

def format_number(formatter,number=0,digits=0):
    ff = formatter
    nn = number
    dd = digits
    n_str = number_strs(dd,nn)
    return ff % {"number":n_str}

#below return start_urls list
def URLSZERO(dt,timezone,logger,**kwargs):
    '''time formatter, e.g. daily newspaper
        dt      :date
        spider  :spider
        kwargs  :formatter,start_hour

        description: 
        判断上次时间是不是超过起始时间，超过则调整循环第一天，不找过加一天循环；
        判断这次时间是不是超过起始时间，不超过则减一天循环
    '''
    current_date = get_date_withzone(datetime.datetime.now(),timezone)
    last_date = get_date_withzone(dt,timezone)
    
    oneday_delta = datetime.timedelta(1,0,0)
    logger.debug("i'm here 3")
    results = []
    for li in kwargs.get("pageargs",[]):
        start_hour = li.get("start_hour",None)
        logger.debug("i'm here 4")
        start_date = last_date
        if start_hour:
            if last_date.hour >= start_hour:
                start_date += oneday_delta

            if current_date.hour < start_hour:
                current_str = current_date.strftime("%Y-%m-%d 00:00:00")
            else:
                current_str = (current_date+oneday_delta).strftime("%Y-%m-%d 00:00:00")
        else:
            current_str = current_date.strftime("%Y-%m-%d %H:%M:%S")

        end_date = datetime.datetime.strptime(current_str,"%Y-%m-%d %H:%M:%S")

        loop_date = start_date
        formatter = li['formatter']
        while loop_date < end_date:
            results.append(format_date(loop_date,formatter))
            loop_date += oneday_delta

    return results
    

def URLSONE(dt,timezone,logger,**kwargs):
    ''' use time_difference to give a group of number to format, like paging
        dt      :date
        spider  :logger
        kwargs  :
            pageargs:[{
                formatter:,
                pages:[
                    start_number, default 0
                    ratio(page/days), default 0
                    last_page, default 0
                    digits default 0
                    ]
            }]

        description:
        根据天数计算页数 将页数匹配进数字 同样适用全静态
        问题 01和1两个区别怎么办 number_strs digits
    '''
    logger.debug("i'm here 2")
    current_date = get_date_withzone(datetime.datetime.now(),timezone)
    last_date = get_date_withzone(dt, timezone)
    time_delta = current_date - last_date
    day_difference = time_delta.days + 1 #可能少个一天，按大的算
    logger.debug("i'm here 3")
    results = []

    for li in kwargs.get("pageargs",[]):
        formatter = li.get('formatter',"")
        pages = li.get('pages',"")
        logger.debug("i'm here 4")
        if pages:
            start_number = pages[0]
            ratio = pages[1]
            last_page = pages[2]
            digits = pages[3]

            logger.debug("i'm here 5")
            page_difference = int(day_difference * ratio) + 1
            logger.debug("i'm here 6")
            pa_di = page_difference if page_difference < last_page else last_page
            logger.debug("i'm here 7 %s----%s" % (str(start_number), str(pa_di)))
            for i in range(start_number, start_number + pa_di):
                logger.debug("i'm here 8")
                results.append(format_number(formatter,i,digits))
        else:
            results.append(format_number(formatter,0,0))
                
    return results

def URLSTWO(dt,timezone,logger,**kwargs):
    '''use time_difference to select a url list
        dt      :date
        spider  :logger
        kwargs  :
            pageargs:[{
                "0":today_url
                "1":yesterday_url
                ...
                "max":7
            }]

        description:
        根据天数选网页，0表示今天 1表示昨天 ...
    '''
    current_date = get_date_withzone(datetime.datetime.now(),timezone)
    last_date = get_date_withzone(dt, timezone)
    time_delta = current_date - last_date
    day_difference = time_delta.days + 1
    
    results = []
    for li in kwargs.get("pageargs",[]):
        dd = day_difference if day_difference < li.get("max",7) else li.get("max",7)
        for i in range(0,dd+1):
            url = li.get(str(i),"")
            if url:
                results.append(url)
    
    return results

def URLSTHREE(dt,timezone,logger,**kwargs):
    '''paging,need to set depth;use two
        dt      :date
        spider  :logger
        kwargs  :value
    '''
    raise ValueError

def URLSFOUR(dt,timezone,logger,**kwargs):
    '''get date from api
        dt      :date
        timezone:timezone
        spider  :logger
        kwargs  :
            api_li :[{
                "api_formatter":[]
                "pattern_str":{"json_formatter":"","xml_formatter":""}
            }]

        description: 这个最麻烦 谨慎
        api返回json或html或xml格式数据，此处将返回数据中所有url正则匹配下来或读取为
        json文件，以所有url为start_url，故不在去重范围，但理论上不重复
        只做xml与json的转换识别为dict
    '''
    logger.debug("i'm here 2")
    current_date = get_date_withzone(datetime.datetime.now(),timezone)
    logger.debug("i'm here 3")
    results = []
    for li in kwargs.get("api_li",[]):
        api_url = li.get("api_formatter",[])
        for apuu in api_url:
            apu = format_date(current_date,apuu)
            status_code, res = make_request(apu,logger,"json",None,60,
                li.get("api_code","utf8"),**li.get("pattern_str",{}))
            logger.debug("response result<<<<%s" % str(res))
            logger.debug("response status<<<<%s" % str(status_code))
            logger.debug("至少在这")
            if status_code in [202, 200]:
                itemls = li.get("itemname",[])
                a = res
                for itl in itemls:
                    logger.debug("last_string <<<<<%s" % str(a.keys()))
                    a = a.get(itl,{})

                if a:
                    for ls in a:
                        item_url = ls.get(li.get("itemurl","url"),"")
                        if item_url:
                            results.append(item_url)

    return results

def URLSFIVE(dt,timezone,logger,**kwargs):
    '''get url from a series api

    dt      :date
    timezone:timezone
    spider  :logger
    kwargs  :
        api_li :[{
            "api_forma":[
                {
                    "formatter":""
                    "pages":[start,ratio,end,step,digit]
                },
                {
                    "formatter":""
                }
            ]
            "pattern_str"   :{"json_formatter":"","xml_formatter":""},
            "api_code"      :
            "itemname"      :
            "itemurl"       :
        }]
    '''
    logger.debug("i'm here 2")
    current_date = get_date_withzone(datetime.datetime.now(),timezone)
    last_date = get_date_withzone(dt, timezone)
    time_delta = current_date - last_date
    day_difference = time_delta.days + 1 #可能少个一天，按大的算
    logger.debug("i'm here 3")
    results = []
    input_args = {"api_li":[]}
    for apili in kwargs.get("api_li",[]):
        valueitem = apili
        page_results = []
    
        for li in apili.get('api_forma',[]):
            formatter = li.get('formatter',"")
            pages = li.get('pages',"")
            logger.debug("i'm here 4")
            if pages:
                start_number = pages[0]
                ratio = pages[1]
                last_page = pages[2]
                step = pages[3]
                digits = pages[4]

                logger.debug("i'm here 5")
                page_difference = int(day_difference * ratio) + 1
                logger.debug("i'm here 6")
                pa_di = page_difference if page_difference < last_page - start_number +1 else last_page - start_number + 1
                logger.debug("i'm here 7 %s----%s" % (str(start_number), str(pa_di)))
                for i in range(start_number, start_number + pa_di, step):
                    logger.debug("i'm here 8")
                    page_results.append(format_number(formatter,i,digits))
            else:
                page_results.append(format_number(formatter,0,0))
        
        valueitem['api_formatter'] = page_results
        input_args["api_li"].append(valueitem)
    
    results.extend(URLSFOUR(dt,timezone,logger,**input_args))
                
    return results


def URLSTEN(dt,timezone,logger,**kwargs):
    '''get date from api
        dt      :date
        timezone:timezone
        spider  :logger
        kwargs  :
            pageargs :[
                {}
            ]

        description: 综合前面的
    '''
    funclist = [
        "URLSZERO",
        "URLSONE",
        "URLSTWO",
        "URLSTHREE",
        "URLSFOUR"
    ]
    alldata = kwargs.get("pageargs",[])
    results = []
    for al in alldata:
        logger.debug('[show some data]<<<< %s' % str(al))
        func_string = funclist[al['case']] if al['case'] < len(funclist) else ""
        logger.debug('')
        if func_string:
            result = eval(func_string)(dt,timezone,logger,**al['Kwargs'])
            results.extend(result)

    return results


def URLSELEVEN(dt,timezone,logger,**kwargs):
    # get start_urls directly and completely(result is a list)
    # "kwargs":{
    # "pageargs": [
    #     "https://www.zeit.de/politik/index", "https://www.zeit.de/gesellschaft/index",
    #     "https://www.zeit.de/wirtschaft/index"
    # ]}
    # the results must be a list
    logger.debug("url-11:i'm here")
    results = kwargs.get("pageargs")
    return results


def URLTWELVE(dt,timezone,logger,**kwargs):
    # get start_url from now_month,like JCMS
    logger.debug("i'm here,url-12，当前月份：")
    nowdate = datetime.datetime.now()
    ndstr = nowdate.strftime("%Y-%m-%d")
    now_year,now_month = re.split("-",ndstr)[0],re.split("-",ndstr)[1]
    back_year,back_month = back_process(int(now_year),int(now_month))
    logger.debug("start_point is:year+month")
    logger.debug(back_year);logger.debug(back_month)
    url_prefix = kwargs.get("page_prefix")[0]
    # produce volume num with year,issue num with month
    volume = prod_vol(back_year)
    issue = int(back_month/2+1)
    start_url = url_prefix+str(back_year)+"/"+str(volume)+"/"+str(issue)
    return [start_url]


def V2_URLONE(dt,timezone,logger,**kwargs):
    # 例：http: // search.gmw.cn / service / search.do?q=   +     "一带一路"
    #kwargs:"Kwargs":{"prefix": ,"q_params": ,"langu": }
    #here  the  prefix+keword is one url
    #返回含大量详情页url的url

    logger.debug("i'm here V2_URLONE")
    prefix_url = kwargs.get("prefix"," ") #注意加?
    params = kwargs.get("q_params"," ")
    language = kwargs.get("langu")

    coreword = back_core(language)  #语言确定返回关键词的列表
    start_url=[]
    for x in coreword:
        start_url.append(prefix_url+params.get("keyword","")+x) #注意加=
    return start_url


def V2_URLTWO(dt,timezone,logger,**kwargs):
    """
    :param kwargs:
    prefix:网址前缀(有"?")
    params:查询的关键字keyword,页码page(分页功能暂未实现)
    language:语言确定拼接的关键词
    url_formatter:正则表达式

    :return:详情页的url列表
    """
    logger.debug("i'm here V2_TWO")
    prefix_url = kwargs.get("prefix", " ")
    params = kwargs.get("q_params", " ")
    url_formatter = kwargs.get("formatter"," ")
    logger.debug(prefix_url + params.get("keyword"," "))

    language = kwargs.get("langu"," ")
    coreword = back_core(language)  # 语言确定返回关键词的列表
    start_url = []
    for x in coreword:
        start_url.append(prefix_url + params.get("keyword"," ") + x)
    detail_url = []
    for url in start_url:
        status_code, js_url = V2_make_request_htm(url,url_formatter,logger)
        logger.debug("status&&json_url" + str(status_code) + str(js_url))
        detail_url.append((js_url))
        # js_url是一个json正则匹配出来的url列表
    return detail_url


def get_start_urls(dt,timezone,case,logger,**kwargs):
    '''for start_urls


    '''
    logger.debug("i'm here 1")
    if case == 0:
        #dateformatter
        try:
            return URLSZERO(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)

    elif case == 1:
        #loop for number
        try:
            return URLSONE(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)

    elif case == 2:
        #select via date
        try:
            return URLSTWO(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)

    elif case == 3:
        #null
        try:
            return URLSTHREE(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    elif case == 4:
        #from josn
        try:
            return URLSFOUR(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    elif case == 5:
        #a series of api
        try:
            return URLSFIVE(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    elif case == 10:
        #综合
        try:
            return URLSTEN(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    elif case==11:
        #直接获取完整start_urls的列表
        try:
            return URLSELEVEN(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    elif case==12:
        # 通过获取当前月份获得start_url
        try:
            return URLTWELVE(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    elif case==21:
        #get方法的获取html文本
        try:
            return V2_URLONE(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    elif case==22:
        # get方法获取json
        try:
            return V2_URLTWO(dt,timezone,logger,**kwargs)
        except Exception as e:
            logger.warn(e)
    else:
        
        return []
    
    return []

#version 4.0  start_requests get start_url & related form data list

def REQUESTSONE(dt,logger,**kwargs):
    '''
    Case:1
    Kwargs:{
        start_url_list:[],
        form_data_list:[{
            formatter:{
                "a":"0"
            }
            value:[6,60]
                # 平均一年多少期 -->平均一期多少天 
                # 暂时只考虑这个吧 只考虑一个数字 和 年份 即 只有一个 %(year)d %(num)d
            }
        }]
    }
    
    '''
    logger.debug("[REQUESTSONE]: just enter")
    #时间参数 两个年份 两个天数
    current_date = datetime.datetime.now()
    last_date = dt

    last_year = last_date.year
    current_year = current_date.year

    last_days = (last_date- datetime.datetime(last_year-1,12,31)).days
    current_days = (current_date - datetime.datetime(current_year-1,12,31)).days


    logger.debug("[REQUESTSONE]: <<<[last_date]:%s<<<[last_days]:%s<<<[last_year]:%s\n<<<[current_date]:%s<<<[current_days]:%s<<<[current_year]:%s" % (last_date,last_days,last_year,current_date,current_days,current_year))

    #计算期号
    # min_num = int(last_days / 365 * average_days) # average_days 是一期平均间隔时间 向下取整
    # max_num = int(current_days / 365 * average_days) +1 #向上取整
    # max_num = max_num if max_num<= max_nn else max_nn #max_nn 是一年平均多少期

    start_url_li = kwargs.get("start_url_list",[])
    form_data_li = kwargs.get("form_data_list",[])

    #初步判断参数 url和data数量要一直 就算没有 也得传个空list进来
    if len(start_url_li)!=len(form_data_li) or len(start_url_li)==0:
        logger.warn(">>>>>>>>>>[error in start data build]: check config file")
        return [],[]

    #初始化
    result_li = []
    result_di = {}
    try:
        #开始构造
        for i in range(0,len(start_url_li)):
            #提取每一个参数
            url = start_url_li[i]
            data = form_data_li[i]
            formatter = data.get("formatter",{})
            logger.debug("[formatter]:<<<<<< " + str(formatter))
            value = data.get("value",[])#必须要有两个不然报错
            average_days = None if len(value)!=2 else value[1]
            max_nn = None if len(value)!=2 else value[0]
            temporary_li = []
            #开始考虑formatter
            if average_days!=None and max_nn!=None:
                #计算期号
                min_num = int(last_days / average_days) # average_days 是一期平均间隔时间 向下取整
                min_num = min_num if min_num>=1 else 1
                max_num = int(current_days / average_days) +1 #向上取整
                max_num = max_num if max_num<= max_nn else max_nn #max_nn 是一年平均多少期
                logger.debug("<<<<[this loop]:[min]:%d---[max]:%d" % (min_num,max_num))

                #注意，考虑到出版日期的延后，开头往前推3期，反正有bloom
                min_num = min_num-3
                last_year_this = last_year
                if min_num<=0:
                    min_num=min_num+max_nn
                    last_year_this = last_year_this-1

                for yy in range(last_year_this,current_year+1):
                    min_num_this = 1 if yy!=last_year else min_num
                    max_num_this = max_nn if yy!=current_year else max_num
                    for i in range(min_num_this,max_num_this+1):
                        temporary_li.append(get_formdata(formatter.copy(),YYYY=str(yy),num=i))
            
            result_li.append(url)
            result_di.setdefault(url,temporary_li)

    except Exception as e:
        logger.error(">>>>>>>>>[error in start data build]: check config file")
        logger.error(e)
        return [],{}
    else:
        return result_li,result_di

def REQUESTTWO(dt,logger,**kwargs):
    # post html
    # {startrequests:
    #      {
    #          "kwargs":{
    #              "url":[https:\\,...] 暂时只有一个url，但为列表形式
    #                 "q_params":["keyword1",...]暂时只有一个
    #                 "langugage":"CHINESE"
    #                     "code":"gbk"
    #          }
    #      }
    #  }
    # 通过kwargs生成start_urls列表和
    # {"url1":[{"keyword":"一带一路"},"keyword":"新冠肺炎",...]}
    # 列表每一个url为键，post的键值对组成的列表为值的form_list_dic字典
    po_url = kwargs.get("url"," ")
    po_param = kwargs.get("q_params"," ")
    langu = kwargs.get("language"," ")
    lang_code = kwargs.get("code"," ")
    # 自带的start_requests 不一定编码方式要显式申明 先放着
    po_dic = {}
    corelist = back_core(langu)
    logger.debug(len(po_url))
    try:
        for url in po_url:
            urlword = []
            for word in corelist:
                urlword.append({po_param:word}) #加不加.encode(lang_code)
            po_dic[url] = urlword
    except Exception as e:
        logger.warn(e)
    return po_url,po_dic


def REQUESTThree(dt, logger, **kwargs):
    # post json
    # 通过post返回json，解析json内容，正则表达式匹配返回url_list
    # {startrequests:
    #      {
    #          "kwargs":{
    #              "url":[https:\\,...] 暂时只有一个url，查询端口只有一个
    #                 "q_params":["keyword1",...] 索引字段只有一个，暂时只有一个，不行！
    #                 "langugage":"CHINESE"
    #                     "code":"gbk"
    #                  "url_formatter":正则表达式，跟进详情页的格式只有一个，暂时只有一个
    #          }
    #      }
    #  }
    # 表单:{q_params:corelist中的词}

    be_url = kwargs.get("url","")  #开始的url
    u_headers = kwargs.get("headers","") #不/需要变更的headers，
    core_in_url = kwargs.get("core_in_url","")  #关键词是否在url中的标志位
    final_param = kwargs.get("final_params","")  #formdata中无变化参数，字典形式{}
    key_param = kwargs.get("keyword","") #formdata中关键词键,如果core在url中，则无此项
    page_num = kwargs.get("page_num",)  #翻多少页的数字
    page_params = kwargs.get("page_params","")  #formdata翻页功能的参数
    langu = kwargs.get("language","")      #根据语言筛选关键词
    lang_code = kwargs.get("code","")   #第二种情况的关键词value的编码方式
    formatter = kwargs.get("formatter","") #筛选详情页url的正则
    patt = re.compile(formatter,re.IGNORECASE)
    corelist = back_core(langu)
    logger.info("输出一大堆参数<<<<<<<,首先kwargs")
    logger.info(str(kwargs))

    if core_in_url:
        # 若关键词在request url中，formdata只有翻页功能
        urllist = []  #request url
        total_url =[] #返回的start_urls列表
        for x in corelist:
            urllist.append(be_url+key_param+"="+x)  #拼接关键词发起post的url
        fdtotallist = []  #formdata{}
        for i in range(1,page_num+1):
            temp = copy.deepcopy(final_param)  #深拷贝
            temp.update({page_params:i})
            fdtotallist.append(temp)
        try:
            for call in urllist:
                temp = V2_make_request_json(call,fdtotallist,u_headers,patt,lang_code)
                total_url.extend(temp)
        except Exception as e:
            logger.warn(e)
        return total_url,{}

    else:
        # 关键词在formdata中，表单同时有关键词和翻页
        # 此时be_url只有一个
        total_url = []; fdtotallist = []  #formdata{}
        for word in corelist:
            for num in range(1,page_num+1):
                temp = final_param
                temp.update({page_params:num,key_param:word})
                fdtotallist.append(temp)
        try:
            total_url.extend(V2_make_request_json(be_url,fdtotallist,u_headers,patt,lang_code))
        except Exception as e:
            logger.warn(e)
        return total_url,{}


def get_formdata(form_dict={},**kwargs):
    for k,v in form_dict.items():
        default_logger.debug("格式化前<<<<"+str(form_dict[k]))
        form_dict[k] = format_date(datetime.datetime.now(),v,**kwargs)
        default_logger.debug("结果是啥<<<<"+str(form_dict[k]))
        
    return form_dict




def get_start_requests_params(dt,case,logger=default_logger,**kwargs):
    '''
    for start request

    @return: start_urls(list),start_urls_dict(dict)
    '''
    if case==1:
        try:
            return REQUESTSONE(dt,logger,**kwargs)
        except Exception as e:
            logger.warn("case 1 出错")
            logger.warn(e)
    elif case==2:
        try:
            return REQUESTTWO(dt,logger,**kwargs)
        except Exception as e:
            logger.warn("case 2 出错")
            logger.warn(e)
    elif case ==3:
        try:
            return REQUESTThree(dt,logger,**kwargs)
        except Exception as e:
            logger.warn("case 3 出错")
            logger.warn(e)

    else:
        return [],{}
    return [],{}


# ---------------------------------------------
# rym:
# JCMS
# back track 3 months
def back_process(year,month):
    if month<=3:
        back_year,back_month = year-1,12
    else:
        back_year,back_month = year,month-3
    if back_month%2 == 0:
        odd_month = back_month-1
    return back_year,odd_month

def prod_vol(year):
    base_vol = 57
    base_year = 2019
    if year>=2019:
        vol = base_vol+abs(year-base_year)
        return vol
    elif year<2019:
        vol = base_vol-abs(year-base_year)
        return vol