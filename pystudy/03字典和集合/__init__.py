tt = (1,2,(30,40))
print(hash(tt))
tl = (1,2,[30,40])
# print(hash(tl))
# TypeError: unhashable type: 'list'
tf = (1,2,frozenset([30,40]))
print(hash(tf))
# 当一个元组的所有元素都是可散列的它才是可散列的