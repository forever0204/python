b = 6
def f1(a):
    print(a)
    print(b)
    # b=9

def f2(a):
    global b
    print(a)
    print(b)
    b = 9

f2(3)
# print(b)
b=30
f2(3)
print('---------------分隔符---------------')
from dis import dis
print(dis(f1))