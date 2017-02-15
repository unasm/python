# -*- coding:utf-8 -*- 
import pandas as pd
import numpy as np
import flags 
import matplotlib.pyplot as plt
import MySQLdb as db
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

CacheMap = {}

conn = db.connect(host = "127.0.0.1", port = 3306, user = 'root', passwd = '', db = 'analyze')


def getOne(sql):
    cur = conn.cursor()
    cur.execute(sql)
    return  cur.fetchone()


def getByWhere(where, tableName):
    sql = "SELECT * FROM " + tableName + " where "
    for k in where:
        if hasattr(where[k], "encode"):
            sql = sql + "`" + k +"` = '" + where[k].encode("utf-8") + "' &&"
        else:
            sql = sql + "`" + k +"` = '" + str(where[k]) + "' &&"
    sql = sql.strip("&&")
    return getOne(sql)

def GetList(sql):
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    return data

def getByMap(key):
    global CacheMap
    #print type(CacheMap)
    if len(CacheMap) == 0:
        sql = "SELECT * from `word_attr`"
        data = GetList(sql)
        #print data
        for var in data:
            #print var[1]
            CacheMap[var[1]] = var
    #print "kongzhi"
    #print CacheMap['控制']
    if CacheMap.has_key(key):
        return CacheMap[key]
    return False


#服务于groupby ，对count进行计数
def getWordCount(group):
    count = 0
    for index,row in group.iterrows():
        count += row['count']
    return count

#查看元素是否在数组之中
def inArray(arr, data):
    for val in arr:
        if val == data:
            return True
    return False

def dispArt(data):
    artIdStr = ','.join([str(val) for val in data['article_id'].unique()])
    sql = "SELECT * FROM `article` where id in (%s)" % artIdStr
    artArr = GetList(sql)
    for val in artArr:
        print val[1], "\t\t\t\t", val[2]


def getFrameData(timeStart, timeEnd):
    sql = "SELECT id, release_time From article where release_time <= '%s' && release_time >= '%s' " % (timeEnd, timeStart)
    artList = GetList(sql)
    #print ',' . join(artList)
    artStr = ""
    idTimeMap = {}
    for val in  artList:
        idTimeMap[val[0]] = val[1]
        if artStr == "": 
            artStr = artStr + str(val[0])
        else :
            artStr = artStr + "," + str(val[0])

    sql = "select track_key.word,track_key.article_id, track_key.count, track_key.id  \
            from track_key inner join word_attr on track_key.word = word_attr.word \
            where track_key.article_id in (%s) && track_key.is_delete = 0 && word_attr.kind = 1 " % (artStr);
    data = pd.read_sql(sql, con = conn)
    for idx, val in data.iterrows():
        #print val['article_id']
        data.set_value(idx, 'release_time', idTimeMap[val['article_id']])

    #print "asdfad"
    return data.sort_values(by = 'release_time', ascending = True)
    #return data

###############################################################################

timeStart = '2015-06-30 00:00:00'
timeEnd = '2015-07-30 00:00:00'
data = getFrameData(timeStart, timeEnd)


#dispArt(data)

#print data.head()
start = data.iloc[0].release_time
day10Times = 0
#print start

flagArr = flags.getFlags(conn)

idxToDrop = []
for idx, val in data.iterrows():
    #设置flag
    row = getByMap(val.word)
    if row and inArray(flagArr, row[3]) == False:
        idxToDrop.append(idx)
    ##设置时间的阶段,或许绘图自动实现
    #print val.release_time, "_____", ((val.release_time - start).days)
    if (val.release_time - start).days >= 10:
        day10Times = day10Times + 1
        start = val.release_time
    data.set_value(idx, '10_count', day10Times)
data = data.drop(idxToDrop)
#print data
#print data.shape
#print data.head()
#
pdata = data.groupby(['10_count', 'word']).apply(getWordCount)
#
pdata = pdata.unstack('word')

#print pdata

###将控制替换成0
pdata = pdata.replace(np.nan, 0)
##print pdata.iloc[0].sort_values(ascending = False)[:10];J

#print pdata
fig,axes = plt.subplots(len(pdata), 1, figsize = (10, 6))
for i in range(0, len(pdata)):
    #top10 = pdata.iloc[i].sort_values(ascending = False)
    top10 = pdata.iloc[i].sort_values(ascending = False)[:20]
    #print top10.shape
    top10.plot(kind = 'barh', rot = 0, ax = axes[i])
    #print pdata.iloc[i].name
plt.show()
conn.close()
