# 根据classmethod 的使用，给学生类增加一个类属性，没创建一个实例，该属性自动增加
class Student:
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count +=1

    @classmethod
    def counter(cls):
        return cls.count


if __name__ == '__main__':
    a = Student('a')
    b = Student('b')
    c = Student('a')
    print(a.counter())