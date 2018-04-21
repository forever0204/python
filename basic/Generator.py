#生成器 一边循环一边计算
def fib(max):#fibonacci 斐波那契数列
    n, a, b = 0, 0, 1
    while n < max:
        yield  b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(10):
    print(n)

def triangles(max):
    L=[1]
    i=0;
    while i< max:
        yield L
        L1=[0]+L
        L2=L+[0]
        L= [ L1[j] + L2[j] for j in range(0,len(L1))]
        i=i+1
for t in triangles(2):
    print(t)

