import sqlite3
conn = sqlite3.connect('test.db')
#游标
cursor = conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
#获取rowcount
print(cursor.rowcount)
#关闭cursor
#cursor.close()
#提交事物
#conn.commit()
cursor.execute('select * from user where id = ?',(1,))
v = cursor.fetchall()
print(v)
#关闭connection
conn.close()