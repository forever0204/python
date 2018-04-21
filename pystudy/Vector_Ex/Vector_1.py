# 三维甚至多维的vector
# 1.兼容2维的第一版内容
from array import  array
import reprlib
import math

class Vector:
    typecode = 'd'

    def __init__(self, components):
        # 此处注意穿进去的是个array
        self._components = array(self.typecode,components)
    #    受保护的实例属性_

    def __iter__(self):
        return iter(self._components)
    # iter（）未说明
    # def __repr__(self):
    #     class_name = type(self).__name__
    #     return '{}({!r},{!r})'.format(class_name, *self)
    def __repr__(self):
        reprlib.aRepr.maxarray = 3
        componets = reprlib.repr(self._components)
        componets = componets[componets.find('['):-1]
        # 去掉d之前和尾部的）
        return 'Vector({})'.format(componets)
    # 使用reprlib获取有限长度的打印
    # def __str__(self):
    #     return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])+
                    bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))
    def __len__(self):
        return  len(self._components)
    def __getitem__(self, item):
        return self._components[item]

    @classmethod
    def frombytes(cls,octets):
        typecode  = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

if __name__ == '__main__':

    V1 = Vector([3.1,4.1])
    v2 = Vector(range(10))
    print(V1)
    print(Vector((3,4,5)))
    print(v2)
    print(len(v2))
    print(v2[1:3])