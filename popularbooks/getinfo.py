#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import spider
import config as cg
def get_JD_Top20(item='nbs',category='internet',effectivetime='day',):
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
        #top20只需要返回第一个页面就可以了
        Spider = spider.webSpider(cg.JD_BOOK_URL%(cg.ITEM[item],cg.CATEGORY[category],cg.ITEM[item],cg.EFFECTIVE_TIME[effectivetime],'1'))
        return Spider.getTop20book(cg.REGEX)



def get_JD_Top(item='nbs',category='internet',effectivetime='day',topnumber=20):
    '''
    返回的TOP数量可以自己定义1--100
    
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
    if topnumber <= 0:
        raise TypeError('input topnumber error')
    elif topnumber <= 20:
        pagenumber = 1
    elif topnumber <= 40:
        pagenumber = 2
    elif topnumber <= 60:
        pagenumber = 3
    elif topnumber <= 80:
        pagenumber = 4
    elif topnumber <= 100:
        pagenumber = 5
    else:
        raise TypeError('input topnumber error')
    
    pagelist = []
    for i in range(1,pagenumber + 1):
        pagelist.append(cg.JD_BOOK_URL%(cg.ITEM[item],cg.CATEGORY[category],cg.ITEM[item],cg.EFFECTIVE_TIME[effectivetime],str(i)))
    
    if item not in cg.ITEM.keys() or category not in cg.CATEGORY.keys() or effectivetime not in cg.EFFECTIVE_TIME.keys():
        raise TypeError('input parameters error')
    else: 
        if effectivetime != 'day' and (item == 'bc' or item == 'nbc'):
            effectivetime='day'
            print '热评榜只有24小时内的'
        Spider = spider.webSpiderList(pagelist,topnumber)
        return Spider.getTopbook(cg.REGEX)

#print get_JD_Top('bs','jitang','week',22)