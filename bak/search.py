import pandas as pd
from sqlalchemy import create_engine
import sys
#import traceback

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
# 显示所有列
# pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option("display.max_rows", None)
# 设置value的显示长度为100，默认为50
pd.set_option("max_colwidth", 60)


def search_xm():
    sql_xm = (
        "SELECT name,id FROM `project` where name like '" + search + "'"
    )
    try:
        df_xm = pd.read_sql_query(sql_xm, engine)
        print(df_xm)
    except:
        print("超时！未连接网络?")
        sys.exit(-1)
        #traceback.print_exc()


def search_gc():
    sql_gc = (
        "select name,number,id from single_project where name like '"
        + search
        + "'"
    )
    try:
        df_gc = pd.read_sql_query(sql_gc, engine)
        print(df_gc)
    except:
        print("超时！未连接网络?")
        sys.exit(-1)


def search_file():
    sql_file = (
        "SELECT name,num FROM `file` where name like '"
        + search
        + "'"
        + " and num <> ''"
    )
    try:
        df_file = pd.read_sql_query(sql_file, engine)
        print(df_file)
    except:
        print("超时！未连接网络?")
        sys.exit(-1)


def search_all():
    sql_xm = (
        "SELECT name,id FROM `project` where name like '" + search + "'"
    )
    sql_gc = (
        "select name,number,id from single_project where name like '"
        + search
        + "'"
    )
    sql_file = (
        "SELECT name,num FROM `file` where name like '"
        + search
        + "'"
        + " and num <> ''"
    )
    try:
        df_xm = pd.read_sql_query(sql_xm, engine)
        df_gc = pd.read_sql_query(sql_gc, engine)
        df_file = pd.read_sql_query(sql_file, engine)
    except:
        print("超时！未连接网络?")
        sys.exit(-1)

    print(">" * 200)
    print(df_xm)
    print(">" * 200)
    print(df_gc)
    print(">" * 200)
    print(df_file)


if __name__ == "__main__":
    engine = create_engine("mysql+pymysql://root:root@59.213.89.54:3306/wisdom-dossier")
    search = input("请输入要查找的关键字：")

    while True:
        if search == "exit":
            sys.exit(-1)
        elif search != "":
            search = "%%" + search + "%%"
            which = input("请输入要查找的层级（1.项目，2.单体，3.案卷,0.返回上一级）")
            if which == "1":
                search_xm()
            elif which == "2":
                search_gc()
            elif which == "3":
                search_file()
            elif which == "0":
                search = ""
            elif which == "exit":
                sys.exit(-1)
            else:
                search_all()
        else:
            search = input("输入为空!请输入关键字：")
