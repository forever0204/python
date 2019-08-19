# 关于字节编码中的错误
city  = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
# 'utf_?' 编码能处理任何字符串。
# print(city.encode('gbk'))
# UnicodeEncodeError: 'gbk' codec can't encode character '\xe3' in position 1: illegal multibyte sequence
# print(city.encode('cp437'))
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
print(city.encode('gbk',errors='ignore'))
# 忽略
print(city.encode('gbk',errors='replace'))
# 使用？替换
print(city.encode('gbk',errors='xmlcharrefreplace'))
# 把无法编码的字符替换成 XML 实体
print('---------------分隔符---------------')
octets = b'Montr\xe9al'
# 这些字节序列是使用 latin1 编码的“Montréal”；'\xe9' 字节对应“é”
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
# print(octets.decode('utf_8'))
print(octets.decode('utf_8', errors='replace'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
# utf_8' 编解码器检测到 octets 不是有效的 UTF-8 字符串，抛出UnicodeDecodeError
print(octets.decode('gbk'))
# Montr閍l
s = 'Olá, Mundo!'
print(s)
# SyntaxError 未实现错误
print('---------------分隔符---------------')
u16 = 'El Niño'.encode('utf_16')
print(u16)
# b'\xff\xfe' 是BOM 即 字节序标记（byte-order mark），指明编码时使
# 用 Intel CPU 的小字节序
print(list(u16))
