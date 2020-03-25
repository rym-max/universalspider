#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   AllSpiders.py
@Time    :   2019/03/23 18:46:16
@Author  :   Hzx 
@Version :   1.0
@Contact :   hzxstarcloud@hotmail.com
@Desc    :   ALL need to run spiders are here
'''
import warnings

from scrapy.http import Request
from scrapy.utils.deprecate import method_is_overridden

from .templateDrei import TemplatedreiSpider
from .templateVier import TemplatevierSpider


class RmrbSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "rmrb"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class GmrbSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "gmrb"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class GmwSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "gmw"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class CssnSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "cssn"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class ChinaSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "china"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class FmprcSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "fmprc"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class HuanqiuSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "huanqiu"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class SpiegelSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "spiegel"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1,
        "REDIRECT_MAX_TIMES": 3
    }


class SueddeutscheSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "sueddeutsche"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1,
        "REDIRECT_MAX_TIMES": 2

    }


class TagesschauSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "tagesschau"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class ThepaperSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "thepaper"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class FazSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "faz"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class BmwiSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "bmwi"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class EuobserverSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "euobserver"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 543
        },
        "DOWNLOAD_DELAY": 1
    }


class DgapSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "dgap"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class MiitSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "miit"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class SwpSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "swp"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


##new
class WeltSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "welt"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class TagesspiegelSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "tagesspiegel"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class HuffpostSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "huffpost"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class DiplomatSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "thediplomat"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class EuparliamentSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "euparliament"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class EucommissionSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "eucommission"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class DiploSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "diplo"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class BotschaftSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "botschaft"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class FesSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "fes"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class GmfusSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "gmfus"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class EuunionSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "euunion"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 10,
        "CONCURRENT_REQUESTS": 1,
    }


class MoeSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "moe"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1,
        "DEFAULT_REQUEST_HEADERS": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "_gscu_2078282679=45030693d4cjhk18; wdcid=66e67c496e718aff; gwdshare_firstime=1545030696847; _va_ref=%5B%22%22%2C%22%22%2C1545274901%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DnvhnwoveTsHXQNqhRpyh09lrIqmOTdbjqRX2EjVAisK%26wd%3D%26eqid%3Dc03f117500014551000000035c1afafa%22%5D; _va_id=05d435cacd4a6eaf.1545030693.4.1545274901.1545272780.; wdlast=1555005139",
            "Host": "www.moe.gov.cn",
            "Upgrade-Insecure-Requests": 1,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
    }


# new
class GigaSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "giga"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 10,
        "CONCURRENT_REQUESTS": 1,
        # "DEFAULT_REQUEST_HEADERS":{
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Cookie": "_gscu_2078282679=45030693d4cjhk18; wdcid=66e67c496e718aff; gwdshare_firstime=1545030696847; _va_ref=%5B%22%22%2C%22%22%2C1545274901%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DnvhnwoveTsHXQNqhRpyh09lrIqmOTdbjqRX2EjVAisK%26wd%3D%26eqid%3Dc03f117500014551000000035c1afafa%22%5D; _va_id=05d435cacd4a6eaf.1545030693.4.1545274901.1545272780.; wdlast=1555005139",
        #     "Host": "www.moe.gov.cn",
        #     "Upgrade-Insecure-Requests": 1,
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        # }
    }


'''
以下爬虫为特例
'''
# api接口类需要对start_urls 去重
# 改写start_request方法，dont_filter=False
import re


class PeopleSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "people"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

    def start_requests(self):

        for url in self.start_urls:
            for allowdomain in self.allowed_domains:
                if re.search(allowdomain, url):
                    yield Request(url, dont_filter=False)


class XinhuaSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "xinhua"

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

    def start_requests(self):
        cls = self.__class__
        if method_is_overridden(cls, PeopleSpider, 'make_requests_from_url'):
            warnings.warn(
                "Spider.make_requests_from_url method is deprecated; it "
                "won't be called in future Scrapy releases. Please "
                "override Spider.start_requests method instead (see %s.%s)." % (
                    cls.__module__, cls.__name__
                ),
            )
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        else:
            for url in self.start_urls:
                yield Request(url, dont_filter=False)


class KasSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "kas"

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

    def start_requests(self):
        cls = self.__class__
        if method_is_overridden(cls, PeopleSpider, 'make_requests_from_url'):
            warnings.warn(
                "Spider.make_requests_from_url method is deprecated; it "
                "won't be called in future Scrapy releases. Please "
                "override Spider.start_requests method instead (see %s.%s)." % (
                    cls.__module__, cls.__name__
                ),
            )
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        else:
            for url in self.start_urls:
                yield Request(url, dont_filter=False)


class MostSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "most"

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

    def start_requests(self):
        cls = self.__class__
        if method_is_overridden(cls, PeopleSpider, 'make_requests_from_url'):
            warnings.warn(
                "Spider.make_requests_from_url method is deprecated; it "
                "won't be called in future Scrapy releases. Please "
                "override Spider.start_requests method instead (see %s.%s)." % (
                    cls.__module__, cls.__name__
                ),
            )
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        else:
            for url in self.start_urls:
                yield Request(url, dont_filter=False)


class EcfrSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "ecfr"

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

    def start_requests(self):

        for i in range(0, len(self.start_urls)):
            if i == 0 or (i - 1) % 8 == 0:
                yield Request(self.start_urls[i], dont_filter=False)


# 网址无前缀需要加一下
class AuswaertigesSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "auswaertiges"

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

    def __init__(self, *args, **kwargs):
        super(AuswaertigesSpider, self).__init__(*args, **kwargs)
        results = []
        for url in self.start_urls:
            results.append("https://www.auswaertiges-amt.de" + url)
        self.logger.debug(results)
        self.start_urls = results


# 重定向循环

class HandelsblattSpider(TemplatedreiSpider):
    '''production scene need exclusive class now

    due to main problem above, should customize custom_settings as attributes and declare its own name
    '''

    name = "handelsblatt"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1,
        "DOWNLOADER_MIDDLEWARES": {
            'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
            'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,
        },
        "HTTPERROR_ALLOWED_CODES": [302]
        # "REDIRECT_ENABLED": False
        # "DEFAULT_REQUEST_HEADERS":{
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Accept-Language': 'zh-CN,zh;q=0.9',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        # }
    }


class ZEITSpider(TemplatedreiSpider):
    name = "ZEIT"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


class boellSpider(TemplatedreiSpider):
    name = "boell"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


# ---------------version 4-----------journal
class EuropeanstudiesSpider(TemplatevierSpider):
    name = "europeanstudies"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class ContempinterrelationsSpider(TemplatevierSpider):
    name = "contempinterrelations"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class InternationalforumSpider(TemplatevierSpider):
    name = "internationalforum"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class DeutschlandstudienSpider(TemplatevierSpider):
    name = "deutschlandstudien"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class EtudesfrancaisesSpider(TemplatevierSpider):
    name = "etudesfrancaises"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class JinternationalstudiesSpider(TemplatevierSpider):
    name = "jinternationalstudies"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class GlobalreviewSpider(TemplatevierSpider):
    name = "globalreview"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class ForumworldeconopolitSpider(TemplatevierSpider):
    name = "forumworldeconopolit"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class ForeignaffairsreviewSpider(TemplatevierSpider):
    name = "foreignaffairsreview"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class InternationalstudiesSpider(TemplatevierSpider):
    name = "internationalstudies"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class ContemworldsocialismSpider(TemplatevierSpider):
    name = "contemworldsocialism"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class WorldeconoandpolitSpider(TemplatevierSpider):
    name = "worldeconoandpolit"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 3
    }


class JCMSSpider(TemplatedreiSpider):
    name = 'JCMS'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.JournalMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }


# -----------------not journal,but Templatevier----------------------------
class guanchaSpider(TemplatevierSpider):
    name = 'guancha'
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300
        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

class ifriSpider(TemplatevierSpider):
    name = "ifri"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "ITEM_PIPELINES": {
            "universalspider.pipelines.NewsMetaPipeline": 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            "universalspider.middlewares.BloomFilterMiddlewares": 300
        },
        "DOWNLOAD_DELAY": 1
    }

