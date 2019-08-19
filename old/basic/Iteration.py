# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
print('--------------')
for k, v in d.items():
    print(k + ':' + str(v))

a = ('甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸')
b = ('子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥')

c = []
for i in range(60):
    # print(i%len(a))
    # print(a[i%len(a)]+b[i%len(b)])
    c.append(a[i % len(a)] + b[i % len(b)])
print(len(c))
print('--------我是分割线-------------')
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2 ==0])
print([m+n for m in 'ABC' for n in 'XYZ'])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)