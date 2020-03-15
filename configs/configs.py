configs = {
    "people":
    {
        "spider": "people",
        "website": "人民网",
        "type": "新闻",
        "index": "http://news.people.com.cn",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "dynamic",
            "method": "fromjson",
            "need_process": 1,
            "args":{
                "url":"http://news.people.com.cn",
                "pattern":"initPagination().+url: \"(.+?)\"",
                "group_num":2,
                "code1":"gbk",
                "re_mode":"re.DOTALL",
                "formatter":"http://news.people.com.cn%s?_%d",
                "code2":"utf-8",
                "key1":"items",
                "key2":"url",
                "need_unix":1
            }
        },
        "allowed_domains": [
            "people.com.cn"
        ],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "void",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    # {
                    #     "method": "xpath",
                    #     "args": [
                    #         "//div[contains(@class,'text_title')]/h1//text()"
                    #     ]
                    # },
                    # {
                    #     "method": "xpath",
                    #     "args": [
                    #         "//h1[@id='p_title']/text()"
                    #     ]
                    # },
                    # {
                    #     "method": "xpath",
                    #     "args": [
                    #         "//div[@class='title']/h2/text()"
                    #     ],
                    #     "re":"[\u4e00-\u9fa5a-zA-Z0-9《》：，。；？、（）() ]{1,}"
                    # },
                    # {
                    #     "method": "xpath",
                    #     "args": [
                    #         "//div[@class='text_c']/h1/text()"
                    #     ]
                    # }
                    {
                        "method" : "xpath",
                        "args" : [
                            "//title/text()"
                        ],
                        "re" : "(.*)--"
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "text":[
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='box_con']//p//text()"
                            
                        ]
                    },
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@id='p_content']//p//text()"
                            
                        ]
                    },
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='artDet']//p//text()"
                            
                        ]
                    },
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='show_text']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    # {
                    #     "method": "xpath",
                    #     "args":[
                    #         "//div[contains(@class,'text_title')]/div[@class='box01']/div[@class='fl']/text()"
                    #     ],
                    #     "re":"\\d+年\\d+月\\d+日\\d:\\d"
                    # },
                    # {
                    #     "method": "xpath",
                    #     "args":[
                    #         "//i[@id='p_publishtime']/text()"
                    #     ],
                    #     "re":"\\d+年\\d+月\\d+日\\d:\\d"
                    # },
                    # {
                    #     "method": "xpath",
                    #     "args":[
                    #         "//div[@class='artOri']/text()"
                    #     ],
                    #     "re":"\\d+年\\d+月\\d+日\\d:\\d"
                    # },
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='publishdate']/@content"
                        ]
                    }
                ],
                "source":[
                    # {
                    #     "method":"xpath",
                    #     "args":[
                    #         "//div[contains(@class,'text_title')]/div[@class='box01']/div[@class='fl']/a/text()"
                    #     ]
                    # },
                    # {
                    #     "method":"xpath",
                    #     "args":[
                    #         "//i[@id='p_origin']/a/text()"
                    #     ]
                    # },
                    # {
                    #     "method":"xpath",
                    #     "args":[
                    #         "//div[@class='artOri']/a/text()"
                    #     ]
                    # }
                    {
                        "method": "xpath",
                        "args": [
                            "//meta[@name='source']/@content"
                        ],
                        
                    }
                ],
                "author":[
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='edit']//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='p_editor']/text()"
                        ]
                    },
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='editor']/text()"
                        ]
                    },
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='title']/p/text()"
                        ]
                    },
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='show_text']/p[last()]/text()"
                        ]
                    }
                ],
                "category":[
                    # {
                    #     "method":"attr",
                    #     "args":[
                    #         "url"
                    #     ]
                    # }
                    {
                        "method" : "xpath",
                        "args" : [
                            "//title/text()"
                        ],
                        "re" : "--(.*)--"
                    }
                ]
            }
        }
    },
    "rmrb":
    {
        "spider": "rmrb",
        "website": "人民日报",
        "type": "新闻",
        "index": "http://paper.people.com.cn",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "dynamic",
            "method": "fromdate",
            "args":{
                "website":"rmrb",
                "formatters":[
                    "http://paper.people.com.cn/rmrb/html/%(YYYY)s-%(mm)s/%(dd)s/nbs.D110000renmrb_01.htm"
                ]
            }
        },
        "allowed_domains": [
            "paper.people.com.cn"
        ],
        "core_words":["中德","德国"],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "rmrb",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    {
                        "method": "xpath",
                        "args": [
                            "//title/text()"
                        ]
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "keywords":[
                    {
                        "method": "xpath",
                        "args":[
                            "//meta[@name='keywords']/@content"
                        ]
                    }
                ],
                "text":[
                    {
                        "method":"xpath",
                        "args": [
                            "//div[@class='text_c']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    {
                        "method": "func",
                        "args":[
                            "getdate"
                        ]
                    }
                ],
                "source":[
                    {
                        "method": "value",
                        "args": [
                            "人民日报"
                        ]
                    }
                ],
                "author":[
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='text_c']/h4/text()"
                        ],
                        "re":"本报记者\\s+(.+)"
                    }
                ]
            }
        }
    },
    "china":
    {
        "spider": "china",
        "website": "中国网",
        "type": "新闻",
        "index": "http://www.china.com.cn",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "static",
            "value": [
                "http://news.china.com.cn/world/node_7208703.htm","http://news.china.com.cn/world/node_7208704.htm","http://news.china.com.cn/world/node_7239403.htm",
                "http://news.china.com.cn/node_7247300.htm","http://military.china.com.cn/node_7252588.htm","http://military.china.com.cn/node_7252587.htm",
                "http://news.china.com.cn/politics/node_7184914.htm","http://news.china.com.cn/node_7183303.htm","http://shehui.china.com.cn/"
            ]
        },
        "allowed_domains": [
            "china.com.cn"
        ],
        "core_words":[""],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "china",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    {
                        "method": "xpath",
                        "args": [
                            "//title/text()"
                        ],
                        "re":"(.*)\r*\n*_"
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "text":[
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@id='articleBody']//p//text()"
                        ]
                    },
                    {
                        "method": "xpath",
                        "args":[
                            "//div[@id='bigpic']//p[@style]//text()"   
                        ]
                    },
                    {
                        "method" : "xpath",
                        "args":[
                            "//div[@class='cBody']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='publishdate']/@content"
                        ]
                    }
                ],
                "source":[
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@id='webdig_source']//text()"
                        ]
                    }
                ],
                "author":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='author']/@content"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//span[@id='author_baidu']/text()"
                        ],
                        "re":"作者： (.*)"
                    }
                ],
                "category":[
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='crumbs']/a[2]/text()"
                        ]
                    }
                ],
                "keywords":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='keywords']/@content"   
                        ]
                    }
                ]
            }
        }
    },
    "huanqiu":
    {
        "spider": "huanqiu",
        "website": "环球网",
        "type": "新闻",
        "index": "http://www.huanqiu.com",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "static",
            "value": ["http://world.huanqiu.com/article/","http://oversea.huanqiu.com/article/","http://china.huanqiu.com/article/","http://opinion.huanqiu.com/roll.html"]
        },
        "allowed_domains": [
            "huanqiu.com"
        ],
        "core_words":["中德","德国"],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "huanqiu",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    {
                        "method": "xpath",
                        "args": [
                            "//title/text()"
                        ],
                        "re" : "(.*)_"
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "keywords":[
                    {
                        "method": "xpath",
                        "args":[
                            "//meta[@name='keywords']/@content"
                        ]
                    }
                ],
                "text":[
                    {
                        "method":"xpath",
                        "args": [
                            "//div[@class='la_con']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    {
                        "method": "xpath",
                        "args":[
                            "//meta[@name='publishdate']/@content"
                        ]
                    }
                ],
                "source":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='source']/@content"
                        ]
                    }
                ],
                "author":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='author']/@content"
                        ]
                    }
                ],
                "category":[
                    {
                        "method" : "xpath",
                        "args" : [
                            "//title/text()"
                        ],
                        "re" : "_(.*)_"
                    }
                ]
            }
        }
    },
    "cssn":    
    {
        "spider": "cssn",
        "website": "中国社会科学网",
        "type": "新闻",
        "index": "http://www.cssn.cn/",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "static",
            "value": [
                "http://intl.cssn.cn/gj/gj_gwshkx/gj_zz/","http://intl.cssn.cn/gj/gj_gwshkx/gj_wh/","http://intl.cssn.cn/gj/gj_gwshkx/gj_sh/","http://intl.cssn.cn/gj/gj_gwshkx/gj_jj/","http://intl.cssn.cn/gj/gj_gwshkx/gj_zhyj/",
                "http://intl.cssn.cn/gj/gj_gjwtyj/gj_oz/","http://intl.cssn.cn/gj/gj_gjwtyj/gj_gjzz/","http://intl.cssn.cn/gj/gj_gjwtyj/gj_sjjj/",
                "http://intl.cssn.cn/gj/gj_wmdh/gj_hwhx/","http://intl.cssn.cn/gj/gj_wmdh/gj_kwhyj/","http://intl.cssn.cn/gj/gj_gjzl/gj_ggzl/","http://intl.cssn.cn/gj/gj_gjzl/gj_sdgc/"
            ]
        },
        "allowed_domains": [
            "cssn.cn"
        ],
        "core_words":["中德","德国"],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "cssn",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    {
                        "method": "xpath",
                        "args": [
                            "//title/text()"
                        ],
                        "re":"(.*)-"
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "keywords":[
                    {
                        "method": "xpath",
                        "args":[
                            "//meta[@name='Keywords']/@content"
                        ]
                    }
                ],
                "text":[
                    {
                        "method":"xpath",
                        "args": [
                            "//div[@class='TRS_Editor']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    {
                        "method": "xpath",
                        "args":[
                            "//meta[@name='publishdate']/@content"
                        ]
                    }
                ],
                "source":[
                    {
                        "method": "xpath",
                        "args": [
                            "//meta[@name='source']/@content"
                        ]
                    }
                ],
                "author":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='author']/@content"
                        ]
                    }
                ],
                "category":[
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='f-main-top']/span/a[last()]/text()"
                        ]
                    }
                ]
            }
        }
    },
    "fmprc":
    {
        "spider": "fmprc",
        "website": "外交部",
        "type": "新闻",
        "index": "https://www.fmprc.gov.cn/web/",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "dynamic",
            "method": "frompage",
            "args":{
                "forma_page":[
                    ["https://www.fmprc.gov.cn/web/zyxw/default.shtml",[]],["https://www.fmprc.gov.cn/web/zyxw/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/wjbzhd/default.shtml",[]],["https://www.fmprc.gov.cn/web/wjbzhd/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/wjbxw_673019/default.shtml",[]],["https://www.fmprc.gov.cn/web/wjbxw_673019/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default.shtml",[]],["https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673027/default.shtml",[]],["https://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673027/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/dszlsjt_673036/ds_673038/default.shtml",[]],["https://www.fmprc.gov.cn/web/dszlsjt_673036/ds_673038/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/dszlsjt_673036/zls_673040/default.shtml",[]],["https://www.fmprc.gov.cn/web/dszlsjt_673036/zls_673040/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/zwbd_673032/wshd_673034/default.shtml",[]],["https://www.fmprc.gov.cn/web/zwbd_673032/wshd_673034/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/zwbd_673032/ywfc_673029/default.shtml",[]],["https://www.fmprc.gov.cn/web/zwbd_673032/ywfc_673029/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/zwbd_673032/gzhd_673042/default.shtml",[]],["https://www.fmprc.gov.cn/web/zwbd_673032/gzhd_673042/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/zwbd_673032/nbhd_673044/default.shtml",[]],["https://www.fmprc.gov.cn/web/zwbd_673032/nbhd_673044/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/zwbd_673032/jghd_673046/default.shtml",[]],["https://www.fmprc.gov.cn/web/zwbd_673032/jghd_673046/default_%d.shtml",[1,23]],
                    ["https://www.fmprc.gov.cn/web/zwbd_673032/fnhd_673048/default.shtml",[]],["https://www.fmprc.gov.cn/web/zwbd_673032/fnhd_673048/default_%d.shtml",[1,23]]
                ]
            }
        },
        "allowed_domains": [
            "fmprc.gov.cn"
        ],
        "core_words":["中德","德国"],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "fmprc",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='title']/text()"
                        ]
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "keywords":[
                    {
                        "method": "xpath",
                        "args":[
                            "//meta[@http-equiv='keywords']/@content"
                        ]
                    }
                ],
                "text":[
                    {
                        "method":"xpath",
                        "args": [
                            "//div[@class='content']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    {
                        "method": "xpath",
                        "args":[
                            "//div[@class='vibox']//div[@class='time']//span[@id='News_Body_Time']/text()"
                        ]
                    }
                ],
                "source":[
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='vibox']//div[@class='time']//span[@id='myDocsource1']/text()"
                        ]
                    }
                ],
                "author":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='author']/@content"
                        ]
                    }
                ],
                "category":[
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='nav']/a[last()]/text()"
                        ]
                    }
                ]
            }
        }
    },
    "most":
    {
        "spider": "most",
        "website": "科技部",
        "type": "新闻",
        "index": "http://www.most.gov.cn/",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "dynamic",
            "method": "frompage",
            "args":{
                "forma_page":[
                    ["http://www.most.gov.cn/yw/index_10032.htm",[]],["http://www.most.gov.cn/yw/index_10032_%d.htm",[1,2]],
                    ["http://www.most.gov.cn/kjbgz/index.htm",[]],["http://www.most.gov.cn/kjbgz/index_%d.htm",[1,2]],
                    ["http://www.most.gov.cn/gnwkjdt/index.htm",[]],["http://www.most.gov.cn/gnwkjdt/index_%d.htm",[1,2]]
                ]
            }
        },
        "allowed_domains": [
            "gov.cn","xinhuanet.com"
        ],
        "core_words":["中德","德国"],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "most",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    {
                        "method": "xpath",
                        "args": [
                            "//title/text()"
                        ],
                        "re" : "(.*?)_"
                    },
                    {
                        "method": "xpath",
                        "args": [
                            "//title/text()"
                        ],
                        "re" : "(.*?)-"
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='title']/h2/text()"
                        ]
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "keywords":[
                    {
                        "method": "xpath",
                        "args":[
                            "//meta[@name='keywords']/@content"
                        ]
                    }
                ],
                "text":[
                    {
                        "method":"xpath",
                        "args": [
                            "//div[@class='article']//p//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='pages_content']//p//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='main-aticle']//p//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@id='content']//p//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@id='p-detail']//p//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='txtcont']//p//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='content']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    {
                        "method": "xpath",
                        "args":[
                            "//span[@class='h-time']/text()"
                        ],
                        "re" : "(\\d*-\\d*-\\d*)"
                    },
                    {
                        "method" : "xpath",
                        "args":[
                            "//meta[@name='firstpublishedtime']/@content"
                        ],
                        "re":"(\\d*-\\d*-\\d*)"
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='source']//text()"
                        ],
                        "re":"(\\d*-\\d*-\\d*)"
                    }
                ],
                "source":[
                    {
                        "method": "xpath",
                        "args": [
                            "//span[@class='aticle-src']/text()"    
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='pages-date']/span/text()"
                        ],
                        "re" : "来源： (.*)"
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//em[@id='source']//text()"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='source']//span[last()]//text()"
                        ],
                        "re" : "来源：(.*)"
                    }
                ],
                "author":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='author']/@content"
                        ]
                    }
                ],
                "category":[
                    {
                        "method":"xpath",
                        "args":[
                            "//meta[@name='lanmu']/@content"
                        ]
                    },
                    {
                        "method":"xpath",
                        "args":[
                            "//div[@class='news-position']/a[last()]/text()"
                        ]
                    }
                ]
            }
        }
    },
    "miit":
    {
        "spider": "miit",
        "website": "工信部",
        "type": "新闻",
        "index": "http://www.miit.gov.cn/index.html",
        "settings": {
            "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
            "ITEM_PIPELINES":{
                "universalspider.pipelines.NewsSpiderPipeline": 300
            },
        "DOWNLOAD_DELAY": 1
        },
        "start_urls": {
            "type": "static",
            "value": [
                "http://www.miit.gov.cn/n1146290/n1146392/index.html","http://www.miit.gov.cn/n1146290/n1146397/index.html","http://www.miit.gov.cn/n1146290/n4388791/index.html",
                "http://www.miit.gov.cn/n1146290/n1146402/index.html","http://www.miit.gov.cn/n1146290/n1146407/index.html","http://www.miit.gov.cn/n1146290/n4337866/index.html"
            ]
        },
        "allowed_domains": [
            "miit.gov.cn"
        ],
        "core_words":["中德","德国"],
        "filter":["中德","德国"],
        "filter_all":0,
        "need_text":0,
        

        "table":"data",

        "rules": "miit",
        "item": {
            "class": "NewsItem",
            "loader": "NewsLoader",
            "attrs": {
                "title":[
                    {
                        "method": "xpath",
                        "args": [
                            "//title/text()"
                        ]
                    }
                ],
                "url":[
                    {
                        "method": "attr",
                        "args": [
                            "url"
                        ]
                    }
                ],
                "text":[
                    {
                        "method":"xpath",
                        "args": [
                            "//div[@id='con_con']//p//text()"
                        ]
                    }
                ],
                "datetime":[
                    {
                        "method": "xpath",
                        "args":[
                            "//div[@class='cinfo center']/span[@id='con_time']//text()"
                        ],
                        "re":"发布时间：(\\d+-\\d+-\\d)"
                    }
                ],
                "source":[
                    {
                        "method": "xpath",
                        "args": [
                            "//div[@class='cinfo center']/span[contains(text(),'来源')]//text()"
                        ],
                        "re" : "来源：(.*)"
                    }
                ],
                "category":[
                    {
                        "method":"xpath",
                        "args":[
                            "//div[contains(@class,mnav)]/span/a[3]/text()"
                        ]
                    }
                ]
            }
        }
    }


}