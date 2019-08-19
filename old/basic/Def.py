import math
def quadratic(a, b, c):
   v=b**2-4*a*c
   if v<0:
       return('no data')
   elif a==0:
       return('a=0,error')
   else:
       x1=(-b+math.sqrt(v))/(2*a)
       x2=(-b-math.sqrt(v))/(2*a)
       print('x1=%.2f,x2=%.2f' % (x1, x2))
       return 'end'

def power(x, n):#x的n次方
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#a=float(input('a='))
#b=float(input('b='))
#c=float(input('c='))
#print(power(2,4))


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
'''汉诺塔问题'''