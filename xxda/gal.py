#!/usr/bin/python

import sqlite3
import pygal
from pygal.style import LightSolarizedStyle, DarkGreenBlueStyle

# import traceback
# import pysnooper


# @pysnooper.snoop()
def summ(year1):
    year1 = year1
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    sql = """SELECT
    strftime( '%Y-%m', "开票日期" ) AS 年月,
    SUM( "金额" ) 
FROM
    "cjda_fapiao" 
WHERE
    "金额" IS NOT NULL 
GROUP BY
    strftime( '%Y-%m', "开票日期" ) 
ORDER BY
    strftime(
    '%Y-%m',
    "开票日期")"""
    cursor = c.execute(sql)
    rowcount = len(cursor.fetchall())

    cursor = c.execute(sql)

    dated = [0] * 12
    k = 0
    for i in range(rowcount):

        for row in cursor:
            year = row[0][:4]
            month = row[0][5:7]
            # print (row)
            # print(year,month)
            if year == str(year1):
                for j in range(int(month) - i):
                    if not k == 0:
                        break
                    else:
                        dated.append(0)
                # print(i,month)
                dated[int(month) - 1] = row[1]
            else:
                break
            k += 1
    # print(year1,dated)
    return str(year1), dated


# @pysnooper.snoop()
def testyear():
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    sql = """SELECT
    strftime( '%Y-%m', "开票日期" ) AS 年月,
    SUM( "金额" ) 
FROM
    "cjda_fapiao" 
WHERE
    "金额" IS NOT NULL
GROUP BY
    strftime( '%Y-%m', "开票日期" ) 
ORDER BY
    strftime(
    '%Y-%m',
    "开票日期")"""
    cursor = c.execute(sql)

    dated = [0] * 12
    y = []
    k = 0
    for i in range(1, 13):
        for row in cursor:
            year = row[0][:4]
            month = row[0][5:7]
            y.append(year)
            # print(year1,dated)
    y = sorted(list(set(y)))
    # print(y)
    return y


line_chart_dot = pygal.Dot(
    x_label_rotation=30,
    width=1200,
    height=600,
    spacing=50,
    margin=50,
    style=DarkGreenBlueStyle,
)
line_chart = pygal.Bar(
    width=1200, height=600, spacing=50, margin=50, style=DarkGreenBlueStyle
)
line_chart.title = "Invoicing details (yuan)"
line_chart_dot.title = "Invoicing details (yuan)"
line_chart.x_labels = map(str, range(1, 13))
line_chart_dot.x_labels = map(str, range(1, 13))
z = testyear()
for i in range(len(z)):
    x, y = summ(z[i])
    line_chart.add(x, y)
    line_chart_dot.add(x, y)
line_chart_dot.render_in_browser()
# line_chart.render_in_browser()
