# -*- coding: UTF-8 -*-
import pymysql
import urllib3
from bs4 import BeautifulSoup
from operator import itemgetter
import json
import datetime
import codecs
import certifi


getPrice = "https://p.3.cn/prices/mgets?skuIds=J_"
filePath = "/home/tony-jiang/Desktop/jdprice.md"
dict1070Pro = {"显卡": "3237242", "内存": "2551276", "CPU": "1748176", "主板": "1791949", "机箱": "2065352", "电源": "2249598",
               "固态": "3739093", "机械": "746691", "散热器": "689273"}
dict1060Pro = {"显卡": "2983765", "内存": "2121097", "CPU": "1748177", "主板": "1760572", "机箱": "3317529", "电源": "840370",
               "固态": "3739097", "机械": "746691", "散热器": "689273"}
dict1060Evo = {"显卡": "3281156", "内存": "1945472", "CPU": "11075508070", "主板": "1853383", "机箱": "3303012", "电源": "251340",
               "固态": "2639360", "机械": "1540142634", "散热器": "2771147"}
dict1050Evo = {"显卡": "3528459", "内存": "1945472", "CPU": "3701943", "主板": "3775065", "机箱": "3303012", "电源": "251340",
               "固态": "2639360", "机械": "1540142634", "散热器": "2771147"}


def getConnected():
	conn = pymysql.connect(host='localhost',port=3306,
           user='root',passwd='fixture',db='jd_price',charset='UTF8')
	return conn

def closeConnection(connect):
	connect.cursor.close()
	connect.close()

def executeSql(sql):
	try:
		connect.cursor().execute(sql)
		connect.commit()
		print("success")
	except:
		connect.rollback()
		print("fail")

def saveObject(object,connect):
	sql = "insert into t_object (jkuid,obj_name) values('"+object.jkuid+"','"+object.obj_name+"')"
	executeSql(sql)

def saveSuit(suit,connect):
	sql = "insert into t_suit (suit_name,cpu_id,gpu_id,ram_id,ram_id,power_id,box_id,main_board_id,ssd_id,"+\
		"hddk_id,coller_id) values('"+suit.suit_name+"','"+suit.cpu+"','"+suit.gpu+"','"+suit.ram+"','"+suit.power+"','"+\
		suit.box+"','"+suit.main_board+"','"+suit.ssd+"','"+suit.hddk+"','"+suit.cooler+"')"
	executeSql(sql)

def saveObjectHisPrice(objectHisPrice,connect):
	sql = "insert into t_object_history_price (price,t_suit_history_id) values("+objectHisPrice.price+","+\
	objectHisPrice.suit_history_id+")"
	executeSql(sql)


def saveSuitHistory(suitHistory,connect):
	sql = "insert into t_suit_history (price,suit_id,date) values("+suitHistory.price+","+suitHistory.suit_id+\
	","+suitHistory.date+")"
	executeSql(sql)

class Object:
	jkuid=""
	tid=0
	obj_name=""


class ObjectHisPrice:
	tid=0
	price=0
	suit_history_id=""
	create_time=""

class suit:
	tid=0
	suit_name=""
	cpu=0
	gpu=0
	ram=0
	power=0
	box=0
	main_board=0
	ssd=0
	hddk=0
	cooler=0

class suitHistory:
	tid=0
	suit_id=0
	price=0
	date=""

class test:
	def __init__(self):
		self.ni="your"
		self.ma="mother"
		print("ni ma jiao ni hui jia chi fan")




## test functions
connect = getConnected()
obj = Object()
obj.obj_name = "testObject"
obj.jkuid = "123456"
print(obj.obj_name+","+obj.jkuid)

# sql = "insert into t_object (jkuid,obj_name) values( '"+obj.jkuid+"','"+obj.obj_name+"')"
# sql2 = "insert into t_object (jkuid,obj_name) values( 123456,test)"
# try:
# 	cursor = connect.cursor();
# 	cursor.execute(sql)
# 	connect.commit()
# 	print("success")
# except:
# 	print("fail")
# 	connect.rollback()

# connect.close()

test=test()
print(test.ni+" "+test.ma)
# saveObject(obj,connect)
## end test