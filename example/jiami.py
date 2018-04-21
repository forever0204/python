# 加密算法
'''
admin 5	0548E558C3A67BAF 16    YWRtaW4=
system	A8977580651858D0    c3lzdGVt
anonymous9  D531CDCC5557B4BEE918DF2B40C418AC 32

21232f297a57a5a743894a0e4a801fc3
d033e22ae348aeb5660fc2140aec35850c4da997
'''
import hashlib #md5()sha1()
# import pycrypto
data='admin'
admin='0548E558C3A67BAF'
md5 = hashlib.md5()
md5.update(data.encode('utf-8'))
print(md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update(data.encode('utf-8'))
print(sha1.hexdigest())
# 二进制代码
# print(bytes(data.encode('utf-8')))
# print(data^admin)
