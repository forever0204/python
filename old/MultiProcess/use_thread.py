import time,threading
def loop():# loop线程
    print('thread %s is running..' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name , n))
        time.sleep(0.1) #控制线程间隔时间
print('thread %s is runing..'% threading.current_thread().name)  #主线程
t = threading.Thread(target = loop ,name = 'LoopThread')
t.start()
t.join()
print('thread %s ended ' % threading.current_thread().name)
'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例
的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在
打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)