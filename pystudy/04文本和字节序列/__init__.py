s = 'café'
b = s.encode('utf-8')
print(len(s),len(b))

cafe = bytes('café',encoding='utf-8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
for code in ['latin_1','utf_8','utf-8','utf_16']:
    # print(code,'El Niño'.encode(code), sep='\t')
    print(code,'hello'.encode(code), sep='\t')
# latin1（即 iso8859_1）一种重要的编码，是其他编码的基础，例如 cp1252 和 Unicode（注意，latin1 与
# cp1252 的字节值是一样的，甚至连码位也相同）。
print('---------------分隔符---------------')
from unicodedata import normalize, name
micro = 'μ'
eszett = 'ß'
print(name(micro))
print(micro.lower())
print(micro.casefold())
print(name(eszett))
print(eszett.lower())
print(eszett.casefold())
# 对于只包含 latin1 字符的字符串 s，s.casefold() 得到的结果与 s.lower() 一样，唯
# 有两个例外：微符号 'μ' 会变成小写的希腊字母“μ”（在多数字体中二者看起来一样）；
# 德语 Eszett（“sharp s”，ß）会变成“ss”。
# NFC（Normalization Form C）使用最少的码位构成等价的字符串，而 NFD 把组合字符分
# 解成基字符和单独的组合字符
def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)
# 普通规范化比较
def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())
# 不区分大小写比较
print('---------------分隔符---------------')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1==s2)#False
print(nfc_equal(s1,s2))#True
print(nfc_equal('A','a'))#False
s3 = 'Straße'
s4 = 'strasse'
print(s3==s4)#False
print(nfc_equal(s3, s4))#False
print(fold_equal(s3, s4))#True
print(fold_equal(s1, s2))#True
print(fold_equal('A', 'a'))#True