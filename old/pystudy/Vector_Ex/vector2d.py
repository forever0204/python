from array import array
import math


class Vector2d:
    #第9章对Vector类更多功能的实现
    __slots__ = ('__x','__y')
    # 使用__slots__节省空间
    typecode = 'd'
    # tyepcode 是类属性
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    #     将x/y 转换成浮点数

    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    # property 特性装饰器，__x私有属性
    def __iter__(self):
        return (i for i in (self.x, self.y))
    # 将vector2d实例变成可迭代的对象

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)
    # __repr__ 方法使用 {!r} 获取各个分量的表示形式，然后插值，构成一个字符串
  #  def __str__(self):
    #    return str(tuple(self))
    # 中可以轻松地得到一个元组，显示为一个有序对
    def __bytes__(self):
        return (bytes([ord(self.typecode)])+
                bytes(array(self.typecode,self)))
    # 生成字节序列，我们把 typecode 转换成字节序列，
    # 迭代 Vector2d 实例，得到一个数组，再把数组转换成字节序列
    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x,self.y)
    # 模是 x 和 y 分量构成的直角三角形的斜边长
    def __bool__(self):
        return  bool(abs(self))
    # abs(self) 计算模，然后把结果转换成布尔值，因此，0.0 是False，非零值是 True

    def __format__(self, format_spec=''):
        # components = (format(c,format_spec) for c in self)
        # 使用内置的format函数把format_spec应用到向量的各个分量上
        # return  '({},{})'.format(*components)
        if format_spec.endswith('p'):
            # 如果代码以‘p’结尾，使用极坐标
            format_spec = format_spec[:-1]
            # 删除p后缀
            coords = (abs(self),self.angle())
            # 构建一个元组，表示极坐标（magnitude，angle）
            out_fmt = '<{},{}>'
            #外层格式化设为尖括号
        else:
            # 如果不是以p结尾的，则使用self的x和y分量构建直角坐标
            coords = self
            out_fmt = '({},{})'
            #外层设为园括号
        components = (format(c, format_spec) for c in coords)
        return out_fmt.format(*components)
    def angle(self):
        return math.atan2(self.y,self.x)
    #求向量的角度

if __name__ == '__main__':
    v1 = Vector2d(3,4)
    v2 = Vector2d(2,1)
    x,y = v1
    print('x=',x,'y=',y)
    print(v1.x,v1.y)
    print(v1)
    # 应该是Vector2D（3.0，4.0）
    # 将__str__方法关闭后可以看到
    print(abs(v1))
    print(bool(v1))
    print(bool(Vector2d(0,0)))
    v1_clone = eval(repr(v1))
    print('v1==v1_clone:',v1 == v1_clone)
    octets = bytes(v1)
    print(octets)
    print('使用类方法得到的',Vector2d.frombytes(octets))
    print('未使用极坐标--',format(Vector2d(1,1)))
    print('极坐标--',format(Vector2d(1,1),'p'))
    print(format(Vector2d(1,1),'.3ep'))
    print(v1.__eq__(v2))