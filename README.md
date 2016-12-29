# popularbooks
小玩意 python爬虫 返回京东各类图书排行榜top20，可以自定义top1~100
返回json格式

使用例子
import popularbooks as pb

print pb.get_JD_Top20('bs','jitang','week')
print pb.get_JD_Top('bs','jitang','week',22)

参数说明
get_JD_Top20(item='nbs',category='internet',effectivetime='day',)
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

get_JD_Top(item='nbs',category='internet',effectivetime='day',topnumber=20)
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
