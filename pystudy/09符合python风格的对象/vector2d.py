from array import array
import math


class Vector2d:
    typecode = 'd'
    # tyepcode 是类属性
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    #     将x/y 转换成浮点数
    def __iter__(self):
        return (i for i in (self.x, self.y))
    # 将vector2d实例变成可迭代的对象

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)
    # __repr__ 方法使用 {!r} 获取各个分量的表示形式，然后插值，构成一个字符串
    def __str__(self):
        return str(tuple(self))
    # 中可以轻松地得到一个元组，显示为一个有序对
    def __bytes__(self):
        return (bytes([ord(self.typecode)])+
                bytes(array(self.typecode,self)))
    # 生成字节序列，我们把 typecode 转换成字节序列，
    # 迭代 Vector2d 实例，得到一个数组，再把数组转换成字节序列
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x,self.y)
    # 模是 x 和 y 分量构成的直角三角形的斜边长
    def __bool__(self):
        return  bool(abs(self))
    # abs(self) 计算模，然后把结果转换成布尔值，因此，0.0 是False，非零值是 True

v1 = Vector2d(3,4)
v2 = Vector2d(2,1)
print(v1.x,v1.y)
print(v1)
print(abs(v1))
print(bool(v1))
print(bool(Vector2d(0,0)))