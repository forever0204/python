# -*- coding: utf-8 -*-
##基础

print("hello world!")
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))  # 打印长度
print(classmates[1])  # 取值
##if
# height=float(input('请输入你的身高：'))
# weight=float(input('请输入你的体重：'))
height = 175
weight = 80.5
dmi = height / (weight * weight)
if dmi < 18.5:
    print("过轻")
elif dmi < 25:
    print("正常")
elif dmi < 28:
    print("过重")
elif dmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
##循环(for while)
for name in classmates:
    print(name)
sum = 0
for x in range(101):
    sum = sum + x
    if x < 100:
        continue
    print(sum)
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
    if n != 100:
        continue
    print(sum)
##dict set
# dict的key必须是不可变对象
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d.pop('Michael')
print('Michael' in d)
# set 是不可重复的集合
s = set([1, 2, 3, 4, 5, 1])
print(s)
s.add(6)#添加
s.remove(1)#删除
print(s)
