#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rules.py
@Time    :   2019/03/23 19:03:07
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   None
'''

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
#日后建议作为废弃方式


rules = {
    #baidu bake
    # 'forbes':(
    #     Rule(LinkExtractor(allow=r'/item/.*', restrict_xpaths='//ul[@class="polysemantList-wrapper cmn-clearfix"]'), callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'/item/.*', restrict_xpaths='//ul[contains(@class, "custom_dot para-list")]'), callback='parse_item', follow=True)
    # ),

    # 'tongji_news':(
    #     Rule(LinkExtractor(allow=r'/classid-17-*\d*\.html', restrict_xpaths='//div[@class="pager"]//a[contains(text(), "下一页")]')),
    #     Rule(LinkExtractor(allow=r'-t-show\.html', restrict_xpaths='//div[@id="content"]//li'), callback='parse_item')
    # ),

    'people':(
        Rule(LinkExtractor(allow=r"\.html"), callback = 'parse_item'),
    ),
    #新华网
    'xinhua':(
        Rule(LinkExtractor(allow='\\d+-\\d+/\\d+/c_\\d+\\.htm', restrict_xpaths='//ul[@class="dataList"]//li'), callback='parse_item', follow=True),

    ),
    #澎湃新闻
    'thepaper':(
        Rule(LinkExtractor(allow='newsDetail_forward_\\d+', restrict_xpaths='//a'), callback='parse_item'),
    ),

    #环球网
    'huanqiu':(
        Rule(LinkExtractor(allow=r'/\d+-\d+/\d+\.html', restrict_xpaths='//div[@class="fallsFlow"]//li[@class="item"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'article/\d*\.html', restrict_xpaths='//div[@class="pageBox"]//a[contains(.,"下一页")]')),
        Rule(LinkExtractor(allow=r'roll_\d+\.html', restrict_xpaths='//div[@class="pageBox"]//a[contains(.,"下一页")]'))
    ),

    #人民日报
    'rmrb':(
        Rule(LinkExtractor(allow=r'nw\.D110000renmrb_\d+_\d+-\d+\.htm', restrict_xpaths='//div[@class="l_c"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'nbs\.D110000renmrb_\d+\.htm', restrict_xpaths='//a[@id="pageLink" and not(contains(text(),"广告"))]')),
    ),

    #社会科学报
    'cssn':(
        Rule(LinkExtractor(allow=r't\d+_\d+\.shtml', restrict_xpaths='//div[@class="f-main-left"]'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/gj/gj_\w+/gj_\w+index_\d+\.shtml', restrict_xpaths='//a[contains(text(),"下一页")]/@href'),follow=True)
    ),

    #中国网
    'china':(
        Rule(LinkExtractor(allow=r'\d+/\d+/content_\d+\.htm', restrict_xpaths='//ul[@id="c_list"]'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/node_\d+_*\d*\.htm', restrict_xpaths='//div[@id="autopage"]')),
        Rule(LinkExtractor(allow=r'\d+/\d+/content_\d+\.htm', restrict_xpaths='//div[@class="Headlines"]'), callback='parse_item')
    ),
    
    #光明日报
    'gmrb':(
        Rule(LinkExtractor(allow=r'nw\.D110000gmrb_\d+_\d+-\d+\.htm', restrict_xpaths='//div[@class="l_c"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'nbs\.D110000gmrb_\d+\.htm', restrict_xpaths='//a[@id="pageLink" and not(contains(text(),"广告"))]')),
    ),

    'fmprc':(
        Rule(LinkExtractor(allow=r'/t\d+\.shtml', restrict_xpaths='//div[@class="rebox_news"]'), callback='parse_item'),
    ),

    'most':(
        Rule(LinkExtractor(allow=r'/c.*?_\d+\.htm', restrict_xpaths='//td[@class="STYLE30"]'),callback='parse_item'),
    ),

    'miit':(
        Rule(LinkExtractor(allow=r'content\.html',restrict_xpaths='//div[@class="clist_con"]'),callback='parse_item'),
    ),

    'moe':(
        Rule(LinkExtractor(allow=r'\.html', restrict_xpaths='//div[@id="wcmpagehtml"]//a'),callback='parse_item'),
    ),

    'gmw':(
        Rule(LinkExtractor(allow=r'content_\d+\.htm',restrict_xpaths="//ul[@class='channel-newsGroup']"), callback='parse_item'),
    ),
    
    'tagess':(
        Rule(LinkExtractor(allow=r'\.html',restrict_xpaths='//div[@class="box modHeadline"]'), callback='parse_item'),
    ),

    'swp':(
        Rule(LinkExtractor(allow=r'/\d+?/.*/',restrict_xpaths='//div[@class="results_container"]'),callback='parse_item'),
        Rule(LinkExtractor(allow=r'page/\d+/', restrict_xpaths='//div[@class="browseLinksWrap"]//a[contains(text(),"Weiter")]')),
    ),

    'sueddeun':(
        Rule(LinkExtractor(allow=r'de/.*?/.*?/.*',restrict_xpaths='//div[@class="entrylist__content"]//a'),callback='parse_item'),
    ),

    'spiegel':(
        Rule(LinkExtractor(allow=r'\.html',restrict_xpaths='//div[@class="teaser"]//a'),callback='parse_item'),
    ),

    'faz':(
        Rule(LinkExtractor(allow=r'-\d+\.html',restrict_xpaths='//article//a'),callback='parse_item'),
    ),

    "handelsblatt":(
        Rule(LinkExtractor(allow=r'/\d+\.html',restrict_xpaths='//ul[@class="vhb-teaser-list"]//li'),callback='parse_item'),
        Rule(LinkExtractor(allow=r'\?p\d+=\d+', restrict_xpaths='//a[@rel="next"]')),
    ),

    'bmwi':(
        Rule(LinkExtractor(allow='\\.html',restrict_xpaths='//div[@class="container container-media-space"]//li'),callback='parse_item'),
    ),

    'euobserver':(
        Rule(LinkExtractor(allow='/\\d+'),callback='parse_item'),
    ),

    'dgap':(
        
    ),

    'kas':(
        Rule(LinkExtractor(deny='^/document',restrict_xpaths='//tbody//a'),callback='parse_item'),
        Rule(LinkExtractor(allow='_SearchPortlet_cur',restrict_xpaths='//div[@class="search-results"]')),
    ),

    'tagesspiegel':(
        Rule(LinkExtractor(allow='\\d+\\.html',restrict_xpaths='//ul[@class="hcf-teaser-list"]//li[@class="hcf-teaser "]'),callback='parse_item'),
    ),

    'huffpost':(
        Rule(LinkExtractor(restrict_xpaths='//div[@class="a-page__column a-page__column--center"]//div[@data-rapid-cpos]'),callback='parse_item'),
    ),

    'giga':(
        Rule(LinkExtractor(restrict_xpaths='//div[@class="l__content"]//div[class="list__item"]'),callback='parse_item'),
    ),

    'fes':(
        Rule(LinkExtractor(restrict_xpaths='//div[@class="news"]'),callback='parse_item'),
    ),
  
    'ecfr':(
        Rule(LinkExtractor(restrict_xpaths='//div[@class="post "]'),callback='parse_item'),
    ),

    'gmfus':(
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pane__content"]'),callback='parse_item'),
    ),


    #2019两会环球网
    # 'huanqiu':(
    #     Rule(LinkExtractor(allow=r'/\d+-\d+/\d+\.html\?agt=\d', restrict_xpaths='//div[@class="fallsFlow"]//li[@class="item"]'), callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'latest/\d*\.html\?agt=\d', restrict_xpaths='//div[@class="pageBox"]//a[contains(.,"下一页")]')),
    #     Rule(LinkExtractor(allow=r'roll_\d+\.html', restrict_xpaths='//div[@class="pageBox"]//a[contains(.,"下一页")]'))
    # ),

    #2019两会光明网
    # 'gmw':(
    #     Rule(LinkExtractor(allow=r'\d+-\d+/\d+/content_\d+\.htm', restrict_xpaths='//div[@class="channelLeftPart"]'), callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'node_\d+_*\d*\.htm', restrict_xpaths='//a[@class="ptfont" and contains(text(),"下一页")]'), follow=True)    
    # ),

    #2019两会新华网
    # 'xinhua':(
    #     Rule(LinkExtractor(allow=r'\d+-\d+/\d+/c_\d+\.htm', restrict_xpaths='//div[@class="container"]'), callback='parse_item', follow=True),
    # ),

    #2019两会澎湃新闻
    # 'thepaper':(
    #     Rule(LinkExtractor(allow=r'newsDetail_forward_\d+_\d*', restrict_xpaths='//div[@class="topic_mainlt"]'), callback='parse_item', follow=True),
    # ),

    #2019两会人民政协报
    # 'rmzxb':(
    #     Rule(LinkExtractor(allow=r'/c/\d+-\d+-\d+/\d+\.shtml', restrict_xpaths='//div[@id="content"]'), callback='parse_item', follow=True),
    # ),

    #2019两会上海观察网
    # 'shob':(
    #     Rule(LinkExtractor(allow=r'/news/detail\?id=\d+', restrict_xpaths='//div[@class="center"]//div[@class="left"]'), callback='parse_item'),
    # ),

    #维普期刊
    'weipu':(
        Rule(LinkExtractor(allow='Qikan/Article/Detail.*',restrict_xpaths='//span[@class="title"]'),
             callback='parse_item'),
    ),

    'void':(
        
    )
    
}