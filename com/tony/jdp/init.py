# encoding:"utf-8"
import urllib3
from bs4 import BeautifulSoup
from operator import itemgetter
import json
import datetime
import codecs
import certifi

getPrice = "https://p.3.cn/prices/mgets?skuIds=J_"
filePath = "/home/tony-jiang/Desktop/jdprice.md"

def function_get_price(jkuid):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    respPrice = http.request("GET", getPrice + jkuid)
    priceJsonStr = respPrice.data.decode('utf8')
    priceJson = json.loads(priceJsonStr)
    return {"id": priceJson[0]['id'], "price": priceJson[0]['p']}


def function_get_value_name(jkUid):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    resp = http.request("GET", "https://item.jd.com/" + jkUid + ".html")
    htmlStr = resp.data
    soup = BeautifulSoup(htmlStr, "html.parser")
    tempStr = soup.select('.sku-name')[0]
    return {"商品名称": tempStr.text}


dict1070Pro = {"显卡": "3237242", "内存": "2551276", "CPU": "1748176", "主板": "1791949", "机箱": "2065352", "电源": "2249598",
               "固态": "3739093", "机械": "746691", "散热器": "689273"}
dict1060Pro = {"显卡": "2983765", "内存": "2121097", "CPU": "1748177", "主板": "1760572", "机箱": "3317529", "电源": "840370",
               "固态": "3739097", "机械": "746691", "散热器": "689273"}
dict1060Evo = {"显卡": "3281156", "内存": "1945472", "CPU": "11075508070", "主板": "1853383", "机箱": "3303012", "电源": "251340",
               "固态": "2639360", "机械": "1540142634", "散热器": "2771147"}
dict1050Evo = {"显卡": "3528459", "内存": "1945472", "CPU": "3701943", "主板": "3775065", "机箱": "3303012", "电源": "251340",
               "固态": "2639360", "机械": "1540142634", "散热器": "2771147"}


def function_generate_markdown(dict, desc):
    fd = codecs.open(filePath, "a", "utf-8-sig")
    mdict = {}
    print("\n" + desc + " " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n==========\n|类型|名称|价格|")
    fd.write("\n\n" + desc + " " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n==========\n|类型|名称|价格|\n")
    print("|:--------:|:------|: ------ :|")
    fd.write("|:--------:|:------|: ------ :|\n")
    items = sorted(dict.keys())
    for key in items:
        tempDict = function_get_price(dict[key])
        tempDict["商品名称"] = function_get_value_name(dict[key])["商品名称"]
        mdict[key] = tempDict
        print("|" + key + " |" + tempDict['商品名称'] + " |" + tempDict['price'] + "|")
        fd.write("|" + key + " |" + tempDict['商品名称'] + " |" + tempDict['price'] + "|\n")
    total = 0
    for item in mdict:
        p = mdict[item]
        total += float(p["price"])
    print("|||" + str(total) + "|")
    fd.write("|||" + str(total) + "|\n")
    fd.close()


function_generate_markdown(dict1070Pro, "1070主机豪华")
function_generate_markdown(dict1060Pro, "1060主机豪华")
function_generate_markdown(dict1060Evo, "1060主机保底")
function_generate_markdown(dict1050Evo, "1050主机保底")