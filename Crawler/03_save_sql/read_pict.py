import pymysql as mysql
import sys
# import chardet
import os
try:
    conn = mysql.connect('localhost', 'root', 'root', 'test')
    cursor = conn.cursor()
    # sql = 'insert into pic VALUES (%s,%s,%s)'
    # cursor.executemany(sql,[
    #     ('2','test',img)
    # ])
    cursor.execute("select img from pic")
    # 存储成功
    i = 1
    for img in cursor.fetchall():
        # for i  in range(cursor.fetchall().__len__()):
        # print(img)
        i = i+1
        if not isinstance(img, bytearray):
            filename ="test"+str(i)+".png"
            print(filename)
            fp = open(filename,'wb')
            fp.writelines(img)
            fp.close()

    cursor.close()
    conn.close()
except mysql.Error as e:
    print('error %d %s' % (e.args[0], e.args[1]))
    sys.exit(1)

