#!/usr/bin/python

import sqlite3
from prettytable import PrettyTable
import traceback

'''
print ('所有已开发票：')
table = PrettyTable(['id', '开票单位', '项目名称', '金额', '开票日期', '发票号码', '备注'])
conn = sqlite3.connect('xx.db')
c = conn.cursor()
cursor = c.execute('SELECT * FROM cjda_fapiao')
for row in cursor:
    table.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
table.align = 'l'
print(table)
'''

print ('\n以下项目已开发票款未到账：')
table = PrettyTable(['id', '开票单位', '项目名称', '金额', '开票日期', '发票号码', '备注'])
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
cursor = c.execute('SELECT * FROM cjda_fapiao WHERE 备注 IS NULL ')
for row in cursor:
    table.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
table.align = 'l'
print(table)

cursor = c.execute('SELECT SUM(金额) FROM cjda_fapiao WHERE 备注 IS NULL')
print('\n总计已开票未收回的金额为：',end='')
for row in cursor:
    print(str(row[0])+'元')
print('\n')

while True:
    sear=input('请输入要查找的单位或者工程名称：')
    if sear == 'exit' or sear == 'quit':
        break
    #table = PrettyTable(['id', '开票单位', '项目名称', '金额', '开票日期', '发票号码', '备注'])
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    sql = 'SELECT * FROM cjda_fapiao WHERE 开票单位 LIKE "%'+sear+'%" OR 项目名称 LIKE "%'+sear+'%"'
    try:
        if sear == '':
            sql = 'SELECT 开票单位, 项目名称, 金额, 开票日期, 备注 FROM cjda_fapiao WHERE 开票单位 LIKE "%'+sear+'%" OR 项目名称 LIKE "%'+sear+'%"'
            table = PrettyTable(['开票单位', '项目名称', '金额', '开票日期', '备注'])
        elif sear[0] == '.':
            sql = sear[1:]
            table = PrettyTable(['id', '开票单位', '项目名称', '金额', '开票日期', '发票号码', '备注'])
        else:
            sql = 'SELECT 开票单位, 项目名称, 金额, 开票日期, 备注 FROM cjda_fapiao WHERE 开票单位 LIKE "%'+sear+'%" OR 项目名称 LIKE "%'+sear+'%"'
            table = PrettyTable(['开票单位', '项目名称', '金额', '开票日期', '备注'])
    except:
        print ('traceback.format_exc():\n%s' % traceback.format_exc())

    print (sql)
    try:
        cursor = c.execute(sql)
        for row in cursor:
            table.add_row([row[i] for i in range(len(row))])
    except:
        pass
    table.align = 'l'
    print(table)
    print('\n')
    

conn.close()
