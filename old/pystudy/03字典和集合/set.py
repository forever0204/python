l1 = ['apple','apple','banana','orange']
l2 = ['ora','orange','apple']
print(set(l1))
print(list(set(l1)))
found1 = len (set(l2) & set(l1))
print(found1)
# 统计l2里的元素在l1出现的次数
found2 = len(set(l1).intersection(l2))
print(found2)
# 另一种写法
found3 = 0
for n in l2:
    if n in l1:
        found3+=1
print(found3)
# 其他方式的实现
s = set()
print(s)
# 空集的创建