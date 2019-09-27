from sqlalchemy import create_engine
import pandas as pd
import sys
from icecream import ic
import traceback

pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)
# 显示所有列
# pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option("display.max_rows", None)
# 设置value的显示长度为100，默认为50
pd.set_option("max_colwidth", 60)

if __name__ == "__main__":
    # 设置连接
    engine = create_engine("mysql+pymysql://root:root@59.213.89.54:3306/wisdom-dossier")
    while True:
        # 输入要更新的文件档号前缀,输出文件名称,若前缀为0则退出
        search = input("输入文件档号前缀,0退出：")
        if search == "0":
            engine.dispose()
            sys.exit(-1)
        else:
            sql = (
                "SELECT project,number,person_liable,start_time,end_time FROM record where number like '%%"
                + search
                + "%%' order by number"
            )
            # df = pd.read_sql_query(sql, engine)
            # ic(df)

        # 如果文件号和文件名对应就输入责任者,否则输入0重新输入档号前缀|person_liable
        zrz = input("输入责任者,0返回:")
        if zrz == "0":
            continue

        # 输入日期,格式化日期|start_time,end_time|xxxx-xx-xx
        start_end_time = input("输入时间:")
        if not start_end_time.isdigit() or len(start_end_time) < 8:
            start_end_time = "2018-09-27"
        else:
            start_end_time = (
                start_end_time[:4]
                + "-"
                + start_end_time[4:6]
                + "-"
                + start_end_time[6:8]
            )
        # ic(zrz,start_end_time)

        # 更新责任者和日期
        update_sql = "update record set person_liable='{}',start_time='{}',end_time='{}' where number like '%%{}%%'".format(
            zrz, start_end_time, start_end_time, search
        )
        # ic(update_sql)
        # print(update_sql)
        try:
            df1 = pd.read_sql_query(update_sql, engine)
            ic(df1)
        except:
            df = pd.read_sql_query(sql, engine)
            ic(df)
            engine.dispose()
            # traceback.print_exc()
