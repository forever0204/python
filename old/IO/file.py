#读写文件
import  os
import time
import shutil
def xx():
    with open('D:\\pyworkspaces\\test.txt', 'w') as f:
        f.write('Hello, world!')

    with open('D:\\pyworkspaces\\test.txt', 'r') as f:
            print(f.read())

    print(os.path.splitext('D:\\pyworkspaces\\test.txt'))
    print(os.path.abspath('.'))
    #新建文件夹
    #os.mkdir('D:\\pyworkspaces\\testdir')
    #删除文件夹
    #os.rmdir('D:\\pyworkspaces\\testdir')
    # 对文件重命名:
    os.rename('D:\\pyworkspaces\\test.txt', 'D:\\pyworkspaces\\test.py')
    # 删掉文件:
    os.remove('D:\\pyworkspaces\\test.py')

print('列举文件夹',os.listdir('D:\\pyworkspaces'))
print('列举文件',[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

def searchfile(dir,text):
    for x in os.listdir(dir): # 文件所在文件夹
        if os.path.isfile(os.path.join(dir, x)): #判断是不是文件
            if text in os.path.splitext(x)[0]: #判断text 是不是在所列的文件名中
                print('%s, %s' % (dir, x))
        if os.path.isdir(os.path.join(dir, x)): #递归进去
            searchfile(os.path.join(dir, x), text)

print('查找文件--------------')
#searchfile('D:\\pyworkspaces','cl')

def serchsuffix(dir,suffix):
    for x in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,x)):
            if suffix in os.path.splitext(x)[1]:
                print('%s\%s' %(dir,x))
        if os.path.isdir(os.path.join(dir,x)):
            serchsuffix(os.path.join(dir,x),suffix)
print('根据后缀名查找。。。')
#serchsuffix('D:\\pyworkspaces','py')


