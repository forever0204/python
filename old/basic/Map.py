#map 和 reduce
#将输入的名称格式化
from functools import reduce
def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
# -*- coding: utf-8 -*-
#list 求积
def prod(L):
    def mul(a,b):
        return a*b
    return reduce(mul,L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#*********************#
def str2float(s):
    def f(x,y):
        return x*10+y
    def g(s):
        if s!='.':
            return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}[s]
    l=list(map(g,s))
    B=len(l[(l.index(None)+1):])
    l.pop(l.index(None))
    return reduce(f,l) / 10**B
print('str2float(\'123.456\') =', str2float('123.456'))

# 1-10000计算0 的个数
print(sum(map(lambda x: str(x).count('0'),range(10000+1))))