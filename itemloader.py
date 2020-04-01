#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   itemloader.py
@Time    :   2019/03/23 19:02:24
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   for item;customize loader
'''

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose,Identity
import re


class BaikeShort(object):
    '''

    for short URL of baidu baike
    '''
    def __call__(self, values):
        if re.search(r'.*\?',values):
            return re.search(r'.*\?',values).group().replace("?","")
        else:
            return values

class ESCAPE(object):
    '''

    for debug
    '''
    def __call__(self,values):
        if isinstance(values,str):
            print("是字符串啊")
        return values

class BasicLoader(ItemLoader):
    default_output_processor = TakeFirst()

class ChinaLoader(BasicLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())

class BaikeLoader(BasicLoader):
    text_out = Compose(Join(),lambda s: s.strip())
    title_out = Compose(Join(),lambda s: s.strip())
    url_out = Compose(Join(), BaikeShort())

# class NewsLoader(BasicLoader):
#     text_out = Compose(Join(), lambda s: s.strip(), lambda s: s.replace("\u3000\u3000",""), lambda s: s.replace("\xa0",""), lambda s: s.replace(r"\r\n","<br>"))
#     source_out = Compose(Join(), lambda s: s.strip())
#     # category_out = Compose(Join(),lambda s: s.strip(),lambda s: s.split('.')[0],lambda s: s.split('http://')[-1],lambda s: s.split('https://')[-1])

class NewsLoader(BasicLoader):
    '''

    itemname_in     : 
    itemname_out    : 
    '''
    text_out = Compose(Join(), lambda s: s.strip(),
        lambda s: s.replace("\u3000\u3000",""),
        lambda s: s.replace("\xa0",""),
        lambda s: s.replace(r"\r\n","<br>"))

    source_out = Compose(Join(), lambda s: s.strip())


    #貌似不需要
    # def add_html(self, field_name, xpath, *processors, **kw):
    #     '''must use xpath to extract

    #     '''
    #     values = self._get_htmlvalues(xpath, **kw):
    #     self.add_value(field_name, values, *processors, **kw)

    # def _get_htmlvalues(self,xpaths, **kw):
    #     self._check_selector_method()
    #     xpaths = arg_to_iter(xpaths)
    #     '''重写selector太麻烦在这定义吧'''
    #     return None

def replace_xml_space(xml_string):
    # pattern = re.compile(r"(?<=&gt;)[\s\n\t]+|(?=&lt;/)[\s\n\t]+")
    pattern = re.compile(r"(?<=>)[\s\n\t]+|(?=</)[\s\n\t]+")
    return pattern.sub("",xml_string)

#-----------------version 3
class NewsLoaderV3(BasicLoader):
    # 3是针对channel = 1新闻的
    #title default
    #dateissued default
    dateissued_out = Compose(TakeFirst(), lambda s:s.strip(), lambda s:s.replace(r"\n",""))
    subject_out = Compose(Join())
    text_out = Compose(Join(), lambda s: s.strip(),
        lambda s: s.replace("\u3000\u3000",""),
        lambda s: s.replace("\xa0",""),
        lambda s: s.replace(r"\r\n","<br>"))
    description_out = Compose(Join(), lambda s: s.strip(), replace_xml_space)
    source_out = Compose(Join(), lambda s: s.strip())
    author_out = Compose(Join())
    #url default

#-----------------version 4
class NewsLoaderV4(BasicLoader):

    # 维普，4是针对channel=2论文的
    title_out = Compose(Join(), lambda s: s.strip())
    text_out = Compose(Join(), lambda s: s.strip(),
    lambda s: s.replace("\u3000\u3000",""),
    lambda s: s.replace("\xa0",""),
    lambda s: s.replace(r"\r\n","<br>"))
    description_out = Compose(Join(),replace_xml_space)
    author_out = Identity()
    # dateissued default
    organ_out = Identity()
    source_out = Identity()
    # start default
    # num default
    # url default
    subject_out = Identity()
    _class_out= Compose(Join(), lambda s: s.strip(),
    lambda s: s.replace("\u3000\u3000",""),
    lambda s: s.replace("\xa0",""),
    lambda s: s.replace(r"\r\n","").replace(r"\n","").replace(r" ",""))


if __name__ == "__main__":
    teststr = """&lt;div class=\"abstract\"&gt;\n
                            &lt;span class=\"label\"&gt;摘要&lt;/span&gt;\n
                            &lt;span class=\"abstract\"&gt;\n
                                &lt;span class=\"\"&gt;2017年12月2日至3日，“德国的中国能力与中国的德国能力”国际研讨会在同济大学四平路校区中德大楼成功举办。此次会议由同济大学中德人文交流研究中心、德国研究中心和中德学院联合主办，德国汉诺威莱布尼茨大学职业教育与成人教育系和德国汉诺威莱布尼茨孔子学院协办。&lt;/span&gt;\n
                            &lt;/span&gt;\n
                            &lt;em&gt;&lt;span&gt;&lt;/span&gt;&lt;/em&gt;\n
            \n
                &lt;/div&gt;</field>\n
              <field name=\"description\">&lt;div class=\"abstract\"&gt;\n
                            &lt;span class=\"label\"&gt;摘要&lt;/span&gt;\n
                            &lt;span class=\"abstract\"&gt;\n
                                &lt;span class=\"\"&gt;2017年12月2日至3日，“德国的中国能力与中国的德国能力”国际研讨会在同济大学四平路校区中德大楼成功举办。此次会议由同济大学中德人文交流研究中心、德国研究中心和中德学院联合主办，德国汉诺威莱布尼茨大学职业教育与成人教育系和德国汉诺威莱布尼茨孔子学院协办。&lt;/span&gt;\n
                            &lt;/span&gt;\n
                            &lt;em&gt;&lt;span&gt;&lt;/span&gt;&lt;/em&gt;\n
            \n
                &lt;/div&gt;</field>\n
              <field name=\"description_ss\">&lt;div class=\"abstract\"&gt;\n
                            &lt;span class=\"label\"&gt;摘要&lt;/span&gt;\n
                            &lt;span class=\"abstract\"&gt;\n
                                &lt;span class=\"\"&gt;2017年12月2日至3日，“德国的中国能力与中国的德国能力”国际研讨会在同济大学四平路校区中德大楼成功举办。此次会议由同济大学中德人文交流研究中心、德国研究中心和中德学院联合主办，德国汉诺威莱布尼茨大学职业教育与成人教育系和德国汉诺威莱布尼茨孔子学院协办。&lt;/span&gt;\n
                            &lt;/span&gt;\n
                            &lt;em&gt;&lt;span&gt;&lt;/span&gt;&lt;/em&gt;\n
            \n
                &lt;/div&gt;
            """
    
    result = replace_xml_space(teststr)
    print(result)