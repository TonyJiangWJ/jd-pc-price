import sqlalchemy
import codecs
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_CONNECT = "mysql+pymysql://root:fixture@localhost/jd_price?charset=UTF8"
engine = create_engine(DB_CONNECT, echo=True)
Db_session = sessionmaker(bind=engine)
session = Db_session()
Base = declarative_base()


# show listInfo
def show_list(list: list):
    for var in list:
        print(var.suit, var.create_time, var.price, var.name)


# 套餐历史价格
class SuitHisPrice(Base):
    __tablename__ = 'suit_his_price'
    id = Column('id', Integer, primary_key=True)
    suit = Column('套装', String(100), nullable=False)
    type = Column('类型', String(10), nullable=False)
    name = Column('品名', String(100), nullable=False)
    price = Column('价格', DECIMAL(10), nullable=False)
    create_time = Column('时间', DateTime, nullable=False)


# 设备信息
class Object(Base):
    __tablename__ = "t_object"
    tid = Column('tid', Integer, primary_key=True, nullable=False)
    jkuid = Column('jkuid', String(20), nullable=False)
    obj_name = Column('obj_name', String(100), nullable=False)
    type_id = Column('type_id', Integer, nullable=False)
    type_name = Column('type_name', String(10), nullable=False)


query = session.query(SuitHisPrice).all()
print("类型", type(query))

for var in query:
    print(var.suit, var.price, var.create_time, var.type, var.name)

suit1070Pro = list()
suit1050Evo = list()
suit1060Pro = list()
suit1060Evo = list()
for var in query:
    if var.suit == "1070Pro":
        suit1070Pro.append(var)
    if var.suit == "1060Pro":
        suit1060Pro.append(var)
    if var.suit == "1060Evo":
        suit1060Evo.append(var)
    if var.suit == "1050Evo":
        suit1050Evo.append(var)

show_list(suit1050Evo)
show_list(suit1060Evo)
show_list(suit1060Pro)
show_list(suit1070Pro)


# 转换list到字典list
def convert_to_dict(suit: list) -> list:
    for v in suit:
        # 将时间转换成String类型
        v.create_time = str(v.create_time)[0:10]

    suit_list = list()
    suit_time_list = list()
    for v in suit:
        if suit_time_list.__contains__(v.create_time) is False:
            suit_time_list.append(v.create_time)

    # print(suit_time_list)

    title = "套装信息"
    for time in suit_time_list:
        time_dict = dict()
        time_dict['更新时间'] = time
        time_dict[title] = dict()
        total_price = 0
        for v in suit:
            if v.create_time == time:
                time_dict["套装名称"] = v.suit
                time_dict[title][v.type] = dict()
                time_dict[title][v.type]["名称"] = v.name
                time_dict[title][v.type]["价格"] = float(v.price)
                total_price += float(v.price)
        time_dict["总价格"] = total_price
        suit_list.append(time_dict)

    print(suit_list)
    return suit_list


suit1050List = convert_to_dict(suit1050Evo)
suit1060EvoList = convert_to_dict(suit1060Evo)
suit1060ProList = convert_to_dict(suit1060Pro)
suit1070ProList = convert_to_dict(suit1070Pro)


def convert2markdown(suit_list: list, fd):
    for var in suit_list:
        str2write = "###" + var["更新时间"] + " " + var["套装名称"]
        print(str2write)
        fd.write(str2write + "\n")
        # print("=======")
        print("|类型|名称|价格|")
        fd.write("|类型|名称|价格|\n")
        print("|:--------:|:------|: ------ :|")
        fd.write("|:--------:|:------|: ------ :|\n")
        suit_info = var["套装信息"]
        for key in suit_info:
            str2write = "|" + key + "|" + suit_info[key]["名称"] + "|" + str(suit_info[key]["价格"]) + "|"
            print(str2write)
            fd.write(str2write + "\n")
        str2write = "|||" + str(var["总价格"]) + "|"
        print(str2write)
        fd.write(str2write + "\n")


def writeHisSuit2md(suit_list: list, fd,first=None):
    if first is not None:
        fd.write("|更新时间|名称|价格|\n")
        fd.write("|:--------:|:------|: ------ :|\n")
    for var in suit_list:
        str2write = "|" + var["更新时间"] + " |" + var["套装名称"] + "| " + str(var["总价格"]) + "|\n"
        fd.write(str2write)


fd = codecs.open("jd_price.md", 'w', "utf-8-sig")
writeHisSuit2md(suit1050List,fd,first=True)
writeHisSuit2md(suit1060EvoList, fd)
writeHisSuit2md(suit1060ProList, fd)
writeHisSuit2md(suit1070ProList, fd)

convert2markdown(suit1050List, fd)
convert2markdown(suit1060EvoList, fd)
convert2markdown(suit1060ProList, fd)
convert2markdown(suit1070ProList, fd)
fd.close()

#
# query2 = session.query(Object).all()
# i=0
# for var in query2:
#     i+=1
#     print(i,var.obj_name)
