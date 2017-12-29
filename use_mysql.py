import pymysql
conn = pymysql.connect('localhost','root','root','test')
# 配置链接数据库
cursor = conn.cursor()
# 创建游标
# cursor.execute('select * from pic')
# # 执行语句
# v = cursor.fetchall()
# print( v)
# sql = "insert into pic values(%s,%s,%s)"
v1 = 'testdasdas dad'
cursor.execute("insert into pic VALUES (%s)",v1)
# sqli="insert into pic values(%s)"
# cursor.execute(sqli,('2 year 1 class'))
v = cursor.fetchone()
print(v)
# 获取数据并打印
cursor.close()
# 关闭游标
conn.close()
# 关闭链接