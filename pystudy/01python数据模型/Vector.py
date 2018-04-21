from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    #     初始化
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    # 字符串表示形式
    def __abs__(self):
        return  hypot(self.x, self.y)
    # 取绝对值
    def __bool__(self):
        return bool(abs(self))
    # 自定义的布尔值
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    # 加
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    # 乘

v1 = Vector(3,4)
v2 = Vector(2,1)
print(abs(v1))
print(v1+v2)
print(abs(v1*3))
if(abs(v1)):
    print(v1)

print(bool(Vector(1,0)))