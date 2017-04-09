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
    jkuid = ""
    tid = 0
    obj_name = ""
    type_id = -1
    type_name = ""

    def __init__(self):
        self.jkuid = ""
        self.tid = 0
        self.obj_name = ""
        self.type_id = -1
        self.type_name = ""

    def __init__(self, t: tuple):
        self.jkuid = t[1]
        self.tid = t[0]
        self.obj_name = t[2]
        self.type_id = t[3]
        self.type_name = t[4]

    def to_string(self):
        return self.jkuid + str(self.tid) + self.obj_name + self.type_name + str(self.type_id)


class ObjectHisPrice:
    tid = 0
    price = 0.0
    suit_history_id = ""
    create_time = ""
    obj_id = 0


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

    def print(self):
        print(self.tid, self.suit_name, self.gpu, self.cpu, self.ram, self.power,
              self.box, self.main_board, self.ssd, self.hddk, self.cooler)


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
    if result is not None:
        return result[0]
    else:
        return "-1"


def execute_query_list_sql(sql: str):
    print("query list sql:", sql)
    connect = get_connected()
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def save_suit(suit):
    sql = "insert into t_suit (suit_name,cpu_id,gpu_id,ram_id,power_id,box_id,main_board_id,ssd_id," + \
          "hddk_id,cooler_id) values('" + str(suit.suit_name) + "','" + str(suit.cpu) + "','" + str(
        suit.gpu) + "','" + str(suit.ram) + "','" + str(suit.power) + "','" + \
          str(suit.box) + "','" + str(suit.main_board) + "','" + str(suit.ssd) + "','" + str(suit.hddk) + "','" + str(
        suit.cooler) + "')"
    execute_sql(sql)


def save_object_his_price(object_his_price: ObjectHisPrice):
    sql = "insert into t_object_history_price (price,t_suit_history_id,obj_id) values('" + str(
        object_his_price.price) + "','" + \
          str(object_his_price.suit_history_id) + "','" + str(object_his_price.obj_id) + "')"
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


def get_price(jkuid: str):
    get_price_url = "https://p.3.cn/prices/mgets?skuIds=J_"
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    resp_price = http.request("GET", get_price_url + jkuid)
    price_json_str = resp_price.data.decode('utf8')
    try:
        price_json = json.loads(price_json_str)
        return price_json[0]['p']
    except:
        return None


def get_good_name(jkUid):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    resp = http.request("GET", "https://item.jd.com/" + jkUid + ".html")
    htmlStr = resp.data
    soup = BeautifulSoup(htmlStr, "html.parser")
    tempStr = soup.select('.sku-name')[0]
    return tempStr.text


def get_type_id_by_type_name(type_name):
    sql = "SELECT tid FROM t_type WHERE type_desc='" + type_name + "'"
    return execute_query_sql(sql)


def temp_query_list():
    sql = "SELECT * FROM t_object"
    return execute_query_list_sql(sql)


# 从数据库提取数据，并从京东获取价格信息
def parse_to_obj():
    obj_list = [Object]
    tuple_obj = temp_query_list()
    for tup in tuple_obj:
        obj = Object(tup)
        # print(obj.to_string())
        obj_list.append(obj)
        # print(type(tup))

    i = 0
    for obj in obj_list:
        if (obj.jkuid != ""):
            obj_his = ObjectHisPrice()
            print(obj.jkuid)
            obj_his.obj_id = obj.tid
            try:
                obj_his.price = float(get_price(str(obj.jkuid)))
                obj_his.suit_history_id = -1
                save_object_his_price(obj_his)
            except:
                print("error")


# print(type(get_price("689273")))
# print(get_price("689273"))
parse_to_obj()


# {"显卡": "3528459", "内存": "1945472", "CPU": "3701943", "主板": "3775065", "机箱": "3303012", "电源": "251340",
#               "固态": "2639360", "机械": "1540142634", "散热器": "2771147"}

def get_tid_by_jkuid(jkuid):
    sql = "select tid from t_object where jkuid='" + jkuid + "'"
    return execute_query_sql(sql)


def convert_suit_object(suit: dict, suit_name):
    suit_obj = Suit()
    suit_obj.suit_name = suit_name
    for key in suit:
        val = get_tid_by_jkuid(suit[key])
        if key == "显卡":
            suit_obj.gpu = val
        else:
            if key == "内存":
                suit_obj.ram = val
            else:
                if key == "CPU":
                    suit_obj.cpu = val
                else:
                    if key == "主板":
                        suit_obj.main_board = val
                    else:
                        if key == "机箱":
                            suit_obj.box = val
                        else:
                            if key == "电源":
                                suit_obj.power = val
                            else:
                                if key == "固态":
                                    suit_obj.ssd = val
                                else:
                                    if key == "机械":
                                        suit_obj.hddk = val
                                    else:
                                        if key == "散热器":
                                            suit_obj.cooler = val

    suit_obj.print()
    save_suit(suit_obj)


    # convert_suit_object(dict1050Evo,"1050Evo")
    # convert_suit_object(dict1060Evo,"1060Evo")
