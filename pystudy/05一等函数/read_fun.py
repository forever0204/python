def factorial(n):
    ''':returns n!'''
    return 1 if n<2 else n*factorial(n-1)
# 阶乘函数
print(factorial(4))
# 24 4*3*2*1
print(factorial.__doc__)
# 打印了说明
print(type(factorial))
# <class 'function'>
# factorial 是 function 类的实例。
print('---------------分隔符---------------')
fact  = factorial
print(fact)
print(fact(5))
# 通过别的名称使用函数，再把函数作为参数传递

print(list(map(fact,range(6))))
# 使用map函数求0-5的阶乘
print([fact(n) for n in range(6)])
# 使用函数列表推导计算
print(list(map(factorial,filter(lambda n:n%2,range(6)))))
# 使用filter求到5的奇数阶乘
# lambda 匿名函数
print([factorial(n) for n  in range(6) if n%2])
# 使用列表推导