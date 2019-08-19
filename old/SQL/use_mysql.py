import pymysql
conn = pymysql.connect('localhost','bt31User','bt31User','bt31db')
# 配置链接数据库
cursor = conn.cursor()
# 创建游标
# cursor.execute('select * from pic')
# # 执行语句
# v = cursor.fetchall()
# print( v)
# sql = "insert into pic values(%s,%s,%s)"
v1 = 'testdasdas dad'
cursor.execute("select xb,count(1) from app_assetcustominfo200 where xb in ('','男','女')  group by xb")
# sqli="insert into pic values(%s)"
# cursor.execute(sqli,('2 year 1 class'))
v = cursor.fetchall()
# print(v)
# (('', 60), ('男', 15691), ('女', 17527))
# 将值拆包
L1=[]
L2=[]
for sex,num in v:
    L1.append(sex)
    L2.append(num)
print(L1,L2)
# 获取数据并打印
cursor.close()
# 关闭游标
conn.close()
# 关闭链接