# -*- coding: UTF-8 -*-
# pymysql Framework
import pymysql
conn = pymysql.connect(host='localhost',port=3306,
           user='root',passwd='fixture',db='jd_price',charset='UTF8')
cur = conn.cursor()
cur.execute("select version()")
print(cur.data)
cur.close();
conn.close();


