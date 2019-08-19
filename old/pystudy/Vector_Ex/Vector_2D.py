from math import hypot
class Vector:
    # 第一章数据模型
    def __init__(self,x=0,y=0):
        # x=0,y=0?
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x,self.y)
    def __bool__(self):
        # 判断向量的模是否为0 ，0为False，其他为True
        return bool(abs(self))
    def __abs__(self):
        # 根号下x平方加y平方
        return hypot(self.x,self.y)
    def __add__(self, other):
        # 加法
        x = self.x+other.x
        y = self.y+other.y
        return Vector(x,y)
    def __mul__(self, scalar):
        # 乘法
        return Vector(self.x*scalar,self.y*scalar)

if __name__ == '__main__':
    v1 = Vector(2,3)
    v2 = Vector(0,0)#零向量？
    v3 = Vector(3,4)
    # x,y =v1
    # print(x,y)
    print(v1)#向量的打印
    print(bool(v2),bool(v3))#向量的判断
    print(v1+v3)#向量的加法
    print(abs(v3))#向量的求模
    print(v3*3)#向量的乘法