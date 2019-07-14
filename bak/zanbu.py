import random
from icecream import ic
import sqlite3
import stackprinter

# 0为阴,1为阳
# —为阴 ——为阳 X为老阴 O为老阳


def 抽签():
    签 = ""
    备选字符 = [0, 1]
    三枚铜钱 = []
    爻序 = 1
    爻列表 = []
    变爻序号 = []
    变爻次数 = 0
    变卦 = ""
    for i in range(6):
        for j in range(3):
            摇卦 = random.choice(备选字符)
            三枚铜钱.append(摇卦)

        if 三枚铜钱.count(0) == 3:
            爻列表.append("X")
            变爻序号.append(i + 1)
            变爻次数 += 1
            爻 = 0
            变卦 += "1"
        elif 三枚铜钱.count(1) == 3:
            爻列表.append("O")
            变爻序号.append(i + 1)
            变爻次数 += 1
            爻 = 1
            变卦 += "0"
        elif 三枚铜钱.count(1) == 2:
            爻列表.append("—")
            爻 = 1
            变卦 += str(爻)
        elif 三枚铜钱.count(0) == 2:
            爻列表.append("--")
            爻 = 0
            变卦 += str(爻)
        else:
            stackprinter.show()

        爻序 += 1
        签 += str(爻)
        三枚铜钱.clear()

    if 变爻次数 == 0:
        变卦 = "静卦"
    # 爻列表.reverse()
    ic(爻列表)
    ic(变爻次数)
    ic(变爻序号)
    ic(变卦)
    return 签, 变卦, 变爻次数, 变爻序号


def 解签(待解的签, 变卦="", 变爻次数="0", 变爻序号=[]):
    待解的签 = 待解的签
    变卦 = 变卦
    变爻次数 = 变爻次数
    变爻序号 = 变爻序号
    原始爻 = {1: "初", 2: "二", 3: "三", 4: "四", 5: "五", 6: "上"}
    解签用变爻序号 = ""

    connect = sqlite3.connect("zanbu.db")
    cursor = connect.cursor()

    # 测试变爻次数
    # 根据变爻次数按顺序取解签序号，这里会根据变爻次数确定取值及顺序
    # 六爻不变为静卦，用本卦卦辞解卦
    # 变爻次数=1，就用这个变爻的爻辞解卦
    # 变爻次数=2，就用这两个变爻的爻辞解卦，以上爻为主（上爻在前）
    # 变爻次数=3，用本卦卦辞结合变卦卦辞作综合考虑
    # 变爻次数=4，用另外两个静爻的爻辞解卦，并以下爻爻辞为主（原始爻和变爻序号的差集，余二，下爻在前）
    # 变爻次数=5，用变卦的静爻爻辞解卦
    # 变爻次数=6，乾、坤用用九，用六爻辞解卦，其它卦则用变卦的卦辞解卦
    if 变爻次数 == 1:
        for i in 变爻序号:
            解签用变爻序号 += 原始爻[i]

        sql = "SELECT " + 解签用变爻序号 + " FROM zanbu WHERE 符号=" + '"' + 待解的签 + '"'
        ic(sql)
        cursor.execute(sql)
        ic(cursor.fetchall())

    elif 变爻次数 == 2:
        for i in 变爻序号:
            解签用变爻序号 += 原始爻[i]
            解签用变爻序号 += ","

        # 去掉最后的逗号
        解签用变爻序号 = 解签用变爻序号[:-1]
        # 倒序
        解签用变爻序号 = 解签用变爻序号[::-1]
        sql = "SELECT " + 解签用变爻序号 + " FROM zanbu WHERE 符号=" + '"' + 待解的签 + '"'
        ic(sql)
        cursor.execute(sql)
        ic(cursor.fetchall())

    elif 变爻次数 == 3:
        sql = "SELECT 初,二,三,四,五,上 FROM zanbu WHERE 符号=" + '"' + 待解的签 + '"'
        sql_bg = "SELECT 初,二,三,四,五,上 FROM zanbu WHERE 符号=" + '"' + 变卦 + '"'
        ic(sql, sql_bg)
        cursor.execute(sql)
        ic(cursor.fetchall())
        cursor.execute(sql_bg)
        ic(cursor.fetchall())

    elif 变爻次数 == 4:
        # 求差集得到两个静爻
        解签用变爻序号1 = ""
        b = {1: "初", 2: "二", 3: "三", 4: "四", 5: "五", 6: "上"}
        for i in 变爻序号:
            # ic(i)
            b.pop(i)
            #ic(b)
        for i in b:
            解签用变爻序号1 += b[i]
            解签用变爻序号1 += ","
            #ic(解签用变爻序号1)
        # 去掉最后的逗号
        解签用变爻序号1 = 解签用变爻序号1[:-1]
        sql = "SELECT " + 解签用变爻序号1 + " FROM zanbu WHERE 符号=" + '"' + 待解的签 + '"'
        ic(sql)
        try:
            cursor.execute(sql)
            ic(cursor.fetchall())
        except:
            stackprinter.show()

    elif 变爻次数 == 5:
        # 求差集得到一个静爻
        解签用变爻序号1 = ""
        b = {1: "初", 2: "二", 3: "三", 4: "四", 5: "五", 6: "上"}
        for i in 变爻序号:
            # ic(i)
            b.pop(i)
            #ic(b)
        for i in b:
            解签用变爻序号1 += b[i]
            解签用变爻序号1 += ","
            ic(解签用变爻序号1)
        # 去掉最后的逗号
        解签用变爻序号1 = 解签用变爻序号1[:-1]
        sql = "SELECT " + 解签用变爻序号1 + " FROM zanbu WHERE 符号=" + '"' + 变卦 + '"'
        ic(sql)
        try:
            cursor.execute(sql)
            ic(cursor.fetchall())
        except:
            stackprinter.show()

    elif 变爻次数 == 6:
        if 待解的签 == "111111" or 待解的签 == "000000":
            sql = "SELECT 用九 FROM zanbu WHERE 符号=" + '"' + 待解的签 + '"'
            cursor.execute(sql)
            ic(cursor.fetchall())
        else:
            sql = "SELECT 初,二,三,四,五,上 FROM zanbu WHERE 符号=" + '"' + 变卦 + '"'
            cursor.execute(sql)
            ic(cursor.fetchall())
    else:
        # 为0的情况
        sql = "SELECT 初,二,三,四,五,上 FROM zanbu WHERE 符号=" + '"' + 待解的签 + '"'
        cursor.execute(sql)
        ic(cursor.fetchall())

    cursor.close()
    # connect.commit()


if __name__ == "__main__":
    stackprinter.set_excepthook(style="color")
    所抽的签, 变卦, 变爻次数, 变爻序号 = 抽签()
    ic(所抽的签)
    解签(所抽的签, 变卦, 变爻次数, 变爻序号)
