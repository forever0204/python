#闭包
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return  fs
f1,f2,f3 =count()
print('f1:',f1(),'f2:',f2(),'f3:',f3())

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs

f4,f5,f6 = count2()
print("f4:", f4(), 'f5:', f5(), 'f6:', f6())
