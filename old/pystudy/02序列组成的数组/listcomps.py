# 列表推导（list comprehension）简称为 listcomps
# ord 一个字符串变成 Unicode 码位的列表
# 利用for循环添加
symbols = '$¢£¥€¤'
codes = []
for symbol in  symbols:
    codes.append(ord(symbol))
print(codes)
# *列表推导
codes = [ord(symbol) for symbol in symbols]
print(codes)
# filter
beyond_ascii1 = [ord(s) for s in symbols if ord(s) > 1]
print(beyond_ascii1)
# map
beyond_ascii2 = list(filter(lambda c: c>1,map(ord,symbols)) )
print(beyond_ascii2)
# 使用生成器表达式生成元组数据
print(tuple(ord(symbol) for symbol in symbols))
# [36, 162, 163, 165, 8364, 164]
# [36, 162, 163, 165, 8364, 164]
# [36, 162, 163, 165, 8364, 164]
# [36, 162, 163, 165, 8364, 164]
# (36, 162, 163, 165, 8364, 164)

