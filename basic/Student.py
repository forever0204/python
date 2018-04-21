# 使用students类对python中面向对象的思考
class student:
    __slots__ = ('name','age','score')
    # 当把此处的age取消掉后，下面的age就会报错
    # 'student' object has no attribute 'age'
    def __init__(self,name,score):
        self.name = name
        self.score  = score

    def print_info(self):
        print('Name:%s,Score:%d' % (self.name,self.score))



if __name__ == '__main__':
    bart = student('bart simpo',85)
    bart.print_info()
    bart.age = 8
    print(bart.age)
    # 如何打印出bart 的所有信息，包括age
    print(dir(bart))
    print(hasattr(bart,'age'))#True
    print(getattr(bart,'age'))#8
    print(setattr(bart,'age',18))#None
    print(bart.age)#18

