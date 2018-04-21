# 在数据库中存储二进制文件
# 读取jpg文件
import pymysql as mysql
import sys
import os

try:
    path = 'D:\\OneDrive - Cooperative Office System\\Tupian图片\\主题设置\\NIEr'
    img_ext = ['.bmp', '.jpeg', '.gif', '.psd', '.png', '.jpg']
    count = 1
    for x in os.listdir(path):
        # print(x)
        if os.path.splitext(x)[1] in img_ext:
            count += 1
            # print(count)
            filename = os.path.basename(x)
            fp = open(path + '\\' + filename, 'rb')
            img = fp.read()
            # print(img)
            try:
                conn = mysql.connect('localhost', 'root', 'root', 'test')
                cursor = conn.cursor()
                # print(img)
                # sql = 'insert into pic VALUES (%s,%s,%s)'
                # cursor.executemany(sql,[
                #     ('2','test',img)
                # ])
                cursor.execute("insert into pict(img) VALUES (%s)",img)
                # 存储成功
                print(cursor.fetchone())
                cursor.close()
                conn.close()
            except mysql.Error as e:
                print('error %d %s' % (e.args[0], e.args[1]))
                sys.exit(1)
# 读取图片的二进制代码
except IOError as e:
    print('error %d %s' % (e.args[0],e.args[1]))
    sys.exit()
