#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   compile_config_rulesV3.py
@Time    :   2019/08/30 10:41:24
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''


# here put the import lib
import pymssql
import json
import os
import datetime

SQL_SERVER="localhost"
SQL_PORT=1433,
SQL_DB = "Vip_TongjiEU"
SQL_USER = "EU_DATABASE"
SQL_PSWD = "tongji1907"
SQL_CONFIG_TABLE = "SPIDER_Config"
SQL_ITEM_TABLE = "SPIDER_Item"

current_path = os.getcwd()#当前文件夹

cnx = pymssql.connect(host=SQL_SERVER, user=SQL_USER,
    password=SQL_PSWD,database=SQL_DB)
cur = cnx.cursor()


def insert(name="all", creator="BWM",path = current_path):
    
    result = get_result(name,path)
    
    #数据准备
    value_item = {
        "create":datetime.datetime.now(),
        "creator":creator
    }
    #sql语句
    #config
    sql_item = "INSERT INTO " + SQL_ITEM_TABLE + \
        " (Name,ConfigId,IsOpen,Status,Creator,Type,Interval,CreateTime,ModifyTime) "+\
        " VALUES (%(name)s,1,1,0,%(creator)s,0,%(interval)s,%(create)s,%(create)s)"
    sql_config = "INSERT INTO " + SQL_CONFIG_TABLE +\
        " (Name,Configs,Rules,Project,Spider,Creator,CreateTime,ModifyTime)"+\
        " VALUES (%(name)s,%(configs)s,%(rules)s,'universalspider',%(name)s,%(creator)s,%(create)s,%(create)s)"
    #item
    #存储进数据库
    for k,v in result.items():
        value_item.update(v)
        try:
            cur.execute(sql_config,value_item)
            cur.execute(sql_item,value_item)
            cnx.commit()
        except Exception as e:
            print(e)
        else:
            print("成功插入",k)




def delete(name='all',creator='BWM',path=current_path):
    
    pass





def update(name='all',creator='BWM',path=current_path,**kwargs):
    
    result = get_result(name,path)
    
    #数据准备
    value_item = {
        "create":datetime.datetime.now(),
        "creator":creator
    }
    value_item.update(kwargs)

    #其他参数
    special_item=""
    for k,v in kwargs.get('item',{}).keys():
        special_item += " ,"+k+"=%("+k+")s "

    special_config = ""
    for k,v in kwargs.get('config',{}).keys():
        special_config += " ,"+k+"=%("+k+")s "


    #sql语句
    #item
    sql_item = "UPDATE " + SQL_ITEM_TABLE + " SET " +\
        "Interval=%(interval)s,ModifyTime=%(create)s" + \
        special_item +\
        " WHERE Name=%(name)s"
    #config
    sql_config = "UPDATE " + SQL_CONFIG_TABLE +" SET " +\
        "Configs=%(configs)s,Rules=%(rules)s,ModifyTime=%(create)s" + \
        special_config + \
        " WHERE Name=%(name)s"
    
    #存储进数据库
    for k,v in result.items():
        value_item.update(v)
        try:
            cur.execute(sql_config,value_item)
            cur.execute(sql_item,value_item)
            cnx.commit()
        except Exception as e:
            print(e)
        else:
            print("成功更新",k)


def select():
    pass

def get_result(name,path):
        #result存储需要更新的结果
    result={}

    #获取path下所有文件名称
    files_li = os.listdir(path)

    #
    if name!='all':

        if (name+'.json') in files_li and (name+'_rules.json') in files_li:
            item ={}
            item['name']=name
            with open(path+"/"+name+".json","r",encoding="utf-8") as ff:
                item['configs'] = ff.read()
            with open(path+'/'+name+"_rules.json","r",encoding="utf-8") as ff:
                item['rules'] =ff.read()

            item_config = json.loads(item['configs'])
            item.update({
                "interval":item_config.get("INTERVAL",1)
            })
            result.setdefault(name,item)

        else:
            print(name,"该文件夹不存在")

    else:


        #遍历所有文件
        for ffl in files_li:
            
            #

            #判断是否是文件夹
            if not os.path.isdir(ffl):
                fl = ffl.split("_")
                if fl[-1] == "rules.json":
                    name = fl[0]
                    with open(path+"/"+ffl,"r",encoding="utf-8") as ff:
                        item = {
                            "name":name,
                            "rules":ff.read()
                        }
                    if name not in result.keys():
                        result.setdefault(name,item)
                    else:
                        result[name].update(item)
                else:
                    fm = ffl.split(".")
                    if fm[-1] == "json":
                        name = fm[0]
                        with open(path + "/" +ffl,"r",encoding="utf-8") as ff:
                            item = {
                                "name":name,
                                "configs":ff.read()
                            }
                        
                        item_config = json.loads(item['configs'])

                        #此处获取爬取周期
                        item.update({
                            "interval":item_config.get("INTERVAL",1)
                        })

                        if name not in result.keys():
                            result.setdefault(name,item)
                        else:
                            result[name].update(item)
                    else:
                        print(ffl,"文件格式不符！")
    return result

if __name__ == "__main__":
    # update("guancha")
    insert("bergha")