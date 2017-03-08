# -*- coding: UTF-8 -*-
import pymysql
import urllib3
from bs4 import BeautifulSoup
from operator import itemgetter
import json
import datetime
import codecs
import certifi


class Object:
    def __init__(self):
        self.jkuid = ""
        self.tid = 0
        self.obj_name = ""
        self.type_id = -1
        self.type_name = ""


class ObjectHisPrice:
    tid = 0
    price = 0
    suit_history_id = ""
    create_time = ""


class Suit:
    tid = 0
    suit_name = ""
    cpu = 0
    gpu = 0
    ram = 0
    power = 0
    box = 0
    main_board = 0
    ssd = 0
    hddk = 0
    cooler = 0


class SuitHistory:
    tid = 0
    suit_id = 0
    price = 0
    date = ""


class test:
    def __init__(self):
        self.ni = "your"
        self.ma = "mother"
        print("ni ma jiao ni hui jia chi fan")


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


def get_connected():
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='fixture', db='jd_price', charset='UTF8')
    return conn


def close_connection(connect):
    connect.cursor().close()
    connect.close()


def execute_sql(sql):
    print(sql)
    connect = get_connected()
    try:
        connect.cursor().execute(sql)
        connect.commit()
        print("success")
    except ValueError as e:
        connect.rollback()
        print("fail", e)
    finally:
        close_connection(connect)


def execute_query_sql(sql: str):
    print("query sql:", sql)
    connect = get_connected()
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    close_connection(connect)
    return result[0]


def save_suit(suit):
    sql = "insert into t_suit (suit_name,cpu_id,gpu_id,ram_id,ram_id,power_id,box_id,main_board_id,ssd_id," + \
          "hddk_id,coller_id) values('" + suit.suit_name + "','" + suit.cpu + "','" + suit.gpu + "','" + suit.ram + "','" + suit.power + "','" + \
          suit.box + "','" + suit.main_board + "','" + suit.ssd + "','" + suit.hddk + "','" + suit.cooler + "')"
    execute_sql(sql)


def save_object_his_price(object_his_price):
    sql = "insert into t_object_history_price (price,t_suit_history_id) values(" + object_his_price.price + "," + \
          object_his_price.suit_history_id + ")"
    execute_sql(sql)


def save_suit_history(suit_history):
    sql = "insert into t_suit_history (price,suit_id,date) values(" + suit_history.price + "," + suit_history.suit_id + \
          "," + suit_history.date + ")"
    execute_sql(sql)


def save_object(arg: Object):
    arg.type_id = get_type_id_by_type_name(arg.type_name)
    arg.obj_name = get_good_name(arg.jkuid)
    sql = "insert into t_object (jkuid,obj_name,type_id,type_name) values('" \
          + arg.jkuid + "','" + arg.obj_name + "','" + str(arg.type_id) + \
          "','" + arg.type_name + "')"
    execute_sql(sql)


## test functions
#
# obj = Object()
# obj.obj_name = "testObject"
# obj.jkuid = "123456"
# print(obj.obj_name + "," + obj.jkuid)
#
# # sql = "insert into t_object (jkuid,obj_name) values( '"+obj.jkuid+"','"+obj.obj_name+"')"
# # sql2 = "insert into t_object (jkuid,obj_name) values( 123456,test)"
# # try:
# # 	cursor = connect.cursor();
# # 	cursor.execute(sql)
# # 	connect.commit()
# # 	print("success")
# # except:
# # 	print("fail")
# # 	connect.rollback()
#
# # connect.close()
#
# test = test()
# print(test.ni + " " + test.ma)
# # saveObject(obj,connect)
# ## end test





def get_good_name(jkUid):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    resp = http.request("GET", "https://item.jd.com/" + jkUid + ".html")
    htmlStr = resp.data
    soup = BeautifulSoup(htmlStr, "html.parser")
    tempStr = soup.select('.sku-name')[0]
    return tempStr.text


def get_type_id_by_type_name(type_name):
    sql = "select tid from t_type where type_desc='" + type_name + "'"
    return execute_query_sql(sql)


#
for a in dict1070Pro:
    print(dict1070Pro[a])
    obj = Object()
    obj.jkuid = dict1070Pro[a]
    obj.type_name = a
    save_object(obj)
# print(type(get_type_id_by_type_name("内存")))

# print(numbers_to_strings(2))

# # Switcher Example
#
# def zero(v):
#     return "zero" + v
#
#
# def one(v):
#     print("one" + v)
#     return "one" + v
#
#
# def numbers_to_functions_to_strings(argument, v):
#     switcher = {
#         0: zero,
#         1: one,
#         2: lambda: "two",
#     }
#     # Get the function from switcher dictionary
#     func = switcher[argument]
#     # Execute the function
#     return func(v)
#
#
# print(numbers_to_functions_to_strings(1, "test"))
