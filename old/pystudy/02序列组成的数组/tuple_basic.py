import os
lax_coordinates= (33.9425,-118.408)

traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA105856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country,_ in traveler_ids:
    print(country)
# 将不需要的值用占位符”_“代替
city,year,pop,chg,area=('Tokyo',2003,32450,0.66,8014)
print(city)
# 元组拆包
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)
a, b, *rest = range(5)
print(a,b,rest)
print(a,b,*rest)
# 用*来处理剩下的元素
a = 1
b = 2
b,a = a,b
print(a,b)
# 不使用中间变量交换两个变量的值
print('-----------------')
# 使用嵌套元组获取经纬度
metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
