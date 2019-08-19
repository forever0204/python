# 创建字典的一般方法
a = dict(one=1,two=2,three=3)
b = {'one':1,'two':2,'three':3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a==b==c==d==e)
# True
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
# 承载成对数据的列表，可直接用在字典的构造方法中
country_code={country: code for code, country in DIAL_CODES}
print(country_code)
# 将区域码最为值，国家名称作为键（key：value）
country_code={code:country.upper() for country,code in country_code.items()}
print(country_code)
# 将区域码作为键，国家作为值并改为大写
print(country_code.items())
# 返回键值对