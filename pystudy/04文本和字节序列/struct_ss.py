# 使用memoryview和struct查看gif图片的宽度和高度
import struct
fmt = '<3s3sHH'
# 结构体的格式：< 是小字节序，3s3s 是两个 3 字节序列，HH 是两个 16 位二进制整数。
with open('test.gif','rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(header)
print(bytes(header))
print(struct.unpack(fmt,header))
del header