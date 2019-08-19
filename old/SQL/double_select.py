import pymysql
bt31db = pymysql.connect('localhost','bt31User','bt31User','bt31db')
bt32db = pymysql.connect('localhost','bt31User','bt31User','bt32db')
# 配置链接数据库
cursor31 = bt31db.cursor()
# 创建游标
cursor31.execute('select id,archiveid,title from app_assetbasicinfo')
# # 执行语句
v31 = cursor31.fetchone()
print(v31)
cursor31.close()
# 关闭游标
bt31db.close()
# 关闭链接