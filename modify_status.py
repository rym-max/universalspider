import pymssql
from .config_INFO import *

# 设置爬虫status为2

def set_status(name="JCMS"):
    conn = pymssql.connect(host=DATA_HOST,user=DATA_USER,password=DATA_PSWD,database=DATA_DB)
    cur = conn.cursor()

    sql_item = "update SPIDER_Item set Status=2 where Name=%(name)s"
    value_item = {"name":name}
    cur.execute(sql_item,value_item)
    conn.commit()
    conn.close()

if __name__=="__main__":
    set_status()