##定制类，##############

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
'''这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的'''
s = Student('s')

#print(s)
class Chain(object):

    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path): #__getattr 调用不存在的类和方法 如user,hello,repos
        return Chain('%s/%s' % (self._path, path))

    def __call__(self,path):   # __call__ 对实例本身的方法进行调用如lidu，hi
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):      # __str__ 改变打印方法 repos
        return self._path

    __repr__ = __str__

print(Chain().users('lidu').hello.repos)