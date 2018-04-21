# 一个简单的装饰器输出函数的运行时间
import time

def clock(func):
    def clocked(*args):
        # 定义内部函数clocked，它接受任意个定位参数
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.process_time()-t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed,name,arg_str,result))
        return result
    return clocked
        # 返回内部函数，取代被装饰的函数
# clock的功能：
# 1.输出函数调用时，经过的时间、传入的参数和调用的结果打印出来

@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n<2 else n*factorial(n-1)
# 等价于
'''
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
    factorial = clock(factorial)
'''
def factory(n):
    return 1 if n < 2 else n * factory(n - 1)


if __name__ == '__main__':
    print('*' * 40,'Calling snooze(.123)')
    snooze(.123)
    print('*'*40,'Call factorial(6)')
    print('6!=',factorial(6))
    print('---------------分隔符---------------')
    print(factory(6))
#     使用factory同样功能的函数与factorial进行对比
# clock 在factorial函数中做了什么？
'''
1.factorial会作为func参数传给clock
2.clock函数会返回clocked函数
每次调用factorial(n)时会执行clocked(n):
clocked大致做了如下的几件事：
1.记录初始时间t0
2.调用原来的factorial函数，保存结果
3.计算经过的时间
4.格式化手机的数据，打印出来
5.返回第2步保存的结果
'''
'''
**************************************** Calling snooze(.123)
[0.06250000s] snooze(0.123) -> None
**************************************** Call factorial(6)
[-0.06791508s] factorial(1) -> 1
[-0.06791311s] factorial(2) -> 2
[-0.06791113s] factorial(3) -> 6
[-0.06790876s] factorial(4) -> 24
[-0.06790719s] factorial(5) -> 120
[-0.06790126s] factorial(6) -> 720
6!= 720
---------------分隔符---------------
720
'''
