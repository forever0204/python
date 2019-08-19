import itertools
#count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来
natuals = itertools.count(1)
for n in natuals:#导致1被break了
    #print(n)
    break

ns = itertools.repeat('a',3)
for n in ns:
    print(n)
nc = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(nc))
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))