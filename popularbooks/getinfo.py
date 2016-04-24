#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import spider
import config as cg
def get_JD_ItTop20(item='nbs',category='internet',effectivetime='day',):
    '''
    item  str  default 新书销量榜  nbs  
    新书销量榜    nbs  
    图书热评榜    bc
    新书热评榜    nbc
    图书销量榜    bs
    ----------------------------------
    category str default 计算机与互联网  internet
    少儿                       children
    教育                        edu
    小说文学                 novel
    经管                        manage
    励志与成功            jitang
    人文社科                socialscience
    生活                        life
    艺术、摄影            art
    科技                        science
    计算机与互联网       internet
    英文书、港台书        en
    杂志期刊                  magazine
    ----------------------------------
    effectivetime str default 最近24小时 day
    最近24小时  day
    最近一周     week
    最近30天     month
    '''
    if item not in cg.ITEM.keys() or category not in cg.CATEGORY.keys() or effectivetime not in cg.EFFECTIVE_TIME.keys():
        raise TypeError('input parameters error')
    else: 
        if effectivetime != 'day' and (item == 'bc' or item == 'nbc'):
            effectivetime='day'
            print '热评榜只有24小时内的'
        Spider = spider.webSpider(cg.JD_BOOK_URL%(cg.ITEM[item],cg.CATEGORY[category],cg.ITEM[item],cg.EFFECTIVE_TIME[effectivetime]))
        return Spider.getTop20book(cg.REGEX)

