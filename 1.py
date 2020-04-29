#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 3.6
@author: rym
@file: 1.py
@time: 2020/3/17 16:47
@Email:rym606713@163.com
"""
# import pymssql
#
# conn = pymssql.connect(host="localhost:1433", user='EU_DATABASE', password="tongji1907", database="Vip_TongjiEU")
# cur = conn.cursor()
# sql = "set identity_insert Log_AccessLog ON;insert into Log_AccessLog(Id,IPAddress,CreateTime,ModifyTime) values (2,'192.168.101.221','2017-09-20 16:26:36.993','2017-09-20 16:26:36.993')"
# cur.execute(sql)
# conn.commit()
import copy

import requests
import logging
logger = logging.getLogger("test")

def trycrawl():

    url = "https://user.guancha.cn/main/search?click=news&keyword=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92"
    headers = {"X-Requested-With": "XMLHttpRequest"}
    form = {"page":1,"addMore":"search-news-list"}
    response = requests.post(url,form,headers=headers)
    response.encoding = "utf-8"

    print(response.status_code)
    print("<<<<<<<")
    print(response.text)

def log_test():
    logger.debug("test the log module")
    x = [1,3,4]
    logger.debug("test the list"+str(x))
    y = {"a":1}
    logger.debug("test the dict"+str(y))
    print("test log")

def bug_test():
    final_param = {"rym": 1}
    page_params = "page_num"
    page_num = 10
    fdtotallist = []
    for i in range(1, page_num + 1):
        temp = copy.deepcopy(final_param)
        temp.update({page_params: i})
        # print(temp)
        fdtotallist.append(temp)
    print(fdtotallist)

def symboltran(wordstr):
    symbol_dict = {"+": "%2B", ",": "%2C", "ß": "%C3%9F", "ö": "%C3%B6", "ä": "%C3%A4"}
    for k in symbol_dict.keys():
        wordstr = wordstr.replace(k,symbol_dict[k])
    return wordstr

def test_json():
    url1 = "https://www.institutmontaigne.org/json/recherche_globale/type=article&tri=created&index=recherche&ordre=DESC&selection=tout&categorie=&page=1&langue=fr"
    headers1 = {"Referer": "https://www.institutmontaigne.org/blog?recherche=Silk%20Road%20Economic%20Belt&tri=created&ordre=DESC"}
    response1 = requests.get(url1,headers1)
    response1.encoding = "UTF-8"
    print(response1.status_code)
    temp1 = response1.text
    # print(response1.text)

    url2 = "https://www.institutmontaigne.org/json/recherche_globale/type=article&tri=created&index=recherche&ordre=DESC&selection=tout&categorie=&page=1&langue=fr"
    # headers2 = {"Referer": "https://www.institutmontaigne.org/blog?recherche=China&tri=created&ordre=DESC"}
    response2 = requests.get(url2)
    response2.encoding = "UTF-8"
    print(response2.status_code)
    temp2 = response2.text
    # print(response2.text)

    print(temp1==temp2)



if __name__=="__main__":
    # log_test()
    # # bug_test()
    # result = symboltran("17 + 1")
    # print(result)
    test_json()
