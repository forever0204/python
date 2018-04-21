import hashlib
#md5 加密 :生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
md5 = hashlib.md5()
md5.update('hahaha'.encode('utf-8'))
print(md5.hexdigest())

#sha1 加密:SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

def calc_md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()
print(calc_md5('hahaha'))

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user,pwd):
    if user in db:
        return db[user] == calc_md5(pwd)
    else:
        print('user not exist')
print(login('michael','123456'))