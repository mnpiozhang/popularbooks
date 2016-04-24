#!/usr/bin/env python
#_*_ coding:utf-8 _*_
JD_BOOK_URL = 'http://book.jd.com/booktop/%s.html?category=%s-%s-%s-%s'
REGEX = '<a href="//item.jd.com/\d{8}.html" target="_blank" title="(.*?)".*<img data-lazy-img="(.*?)".*></a>'
ITEM = { 
         'nbs':'0-1-0',
         'bs':'0-0-0',
         'bc':'0-0-1',
         'nbc':'0-1-1',
        }

CATEGORY = {
            'children':'3263',
            'internet':'3287',
            'edu':'20001',
            'novel':'20002',
            'manage':'20003',
            'jitang':'3267',
            'socialscience':'20004',
            'life':'20005',
            'art':'20006',
            'science':'20007',
            'en':'20008',
            'magazine':'4758',
            }

EFFECTIVE_TIME = {
                  'day':'10001',
                  'week':'10002',
                  'month':'10003',
                  }