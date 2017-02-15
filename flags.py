# -*- coding:utf-8 -*- 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import MySQLdb as db



#conn = db.connect(host = "127.0.0.1", port = 3306, user = 'root', passwd = '', db = 'analyze')
def getFlags(conn):
    res = []
    flagSql = "select flag from word_attr where flag like 'n%' group by flag"
    cursor = conn.cursor()
    cursor.execute(flagSql)
    flagData = cursor.fetchall()
    for val in flagData:
        res.append(val[0])
    return res 
