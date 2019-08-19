from collections import  namedtuple,deque,defaultdict, Counter
# namedtuple
Point = namedtuple('Point',['x', 'y'])
p = Point(1,2)
print( p.x, p.y)

# deque

q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

#defaultdict

dd = defaultdict(lambda :'N/A')#设置不存在的默认值
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#Counter
c = Counter()
for i in 'programming' :
    c[i] = c[i] +1
print(c)