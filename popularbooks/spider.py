#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import urllib,urllib2,re
import config as cg
from collections import OrderedDict
import json
class webSpider:
    def __init__(self,url):
        self.url=url
        
    def getPage(self):
        req = urllib2.Request(self.url)
        resp = urllib2.urlopen(req)
        return resp.read().decode('gbk')

    def getTop20book(self,rex):
        self.rex = rex
        page = self.getPage()
        pattern = re.compile(self.rex)
        items = re.findall(pattern,page)
        bookdict = OrderedDict()
        for i in items:
            tmpdict = OrderedDict()
            tmpdict['name'] = i[0]
            tmpdict['pic'] = i[1]
            bookdict['top' + str(items.index(i) + 1)] = tmpdict
        return json.dumps(bookdict,encoding="UTF-8", ensure_ascii=False)
    
#spider = webSpider(cg.JD_BOOK_URL%(cg.ITEM['newbookssales'],cg.CATEGORY['internet'],cg.ITEM['newbookssales']))
#spider = webSpider('http://book.jd.com/booktop/0-1-0.html?category=3287-0-1-0-10001-1')
#spider.getTop20book('<a href="//item.jd.com/\d{8}.html" target="_blank" title="(.*?)".*<img data-lazy-img="(.*?)".*></a>')
#spider.getTop20book('<a href="//item.jd.com/\d{8}.html" target="_blank" title=".*<img data-lazy-img=.*></a>')

