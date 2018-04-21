import re
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
# 字符串类型
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')
# 字节序列类型
text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef" #泰米尔数字
" as 1729 = 1³ + 12³ = 9³ + 10³.")
text_bytes = text_str.encode('utf_8')
# 字节序列只能用字节序列正则表达式搜索
print('Text', repr(text_str), sep='\n ')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str))
print(' bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print(' str :', re_words_str.findall(text_str))
print(' bytes:', re_words_bytes.findall(text_bytes))