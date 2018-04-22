#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/21 0021.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
mysql驱动
pip install mysql-connector

如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4
utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。

执行INSERT等操作后要调用commit()提交事务；
MySQL的SQL占位符是%s
"""
# 导入MySQL驱动
import pymysql

# 连接数据库
conn = pymysql.Connect(user="root", password="root", database="py_study")
# .connect()
cursor = conn.cursor()

# 建表
# cursor.execute("create table user (id varchar(20) primary key , name varchar(20))")
# 添加数据
for x in range(3):
    cursor.execute("insert into user (id, name) values (%s, %s)", [str(x+1), "TaoYuan"+str(x)])
print(cursor.rowcount)


# 提交事务
conn.commit()
cursor.close()

# 查询
cursor = conn.cursor()
cursor.execute("select * from user")

values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
