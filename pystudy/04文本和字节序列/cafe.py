import os
fp = open('cafe.txt','w',encoding='utf-8')
print(fp)
print(fp.write('café'))
# 通过给定encoding的方式输出为4
fp.close()
print(os.stat('cafe.txt').st_size)
# os.stat 报告文件中有 5 个字节；UTF-8 编码的 'é' 占两个字节，0xc3 和 0xa9。
fp2 = open('cafe.txt')
print(fp2.read())
# 出现乱码
fp3 = open('cafe.txt',encoding='utf-8')
print(fp3.read())
# 可以正确的打开
fp4 = open('cafe.txt', 'rb')
# 'rb' 标志指明在二进制模式中读取文件。
print(fp4.read())
