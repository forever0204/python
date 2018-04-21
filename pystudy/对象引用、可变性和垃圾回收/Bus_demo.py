# 使用copy探讨浅复制和深复制
import copy
class Bus:
    '''正常的列车'''
    def __init__(self,passengers =None):
        if passengers is None:
            self.passengers =[]
        else:
            self.passengers = list(passengers)

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

bus1 = Bus(['a','b','c','d'])
bus2 = copy.copy(bus1)
# 浅拷贝
bus3 = copy.deepcopy(bus1)
# 深拷贝
print(id(bus1),id(bus2),id(bus3))
bus1.drop('b')
print(bus2.passengers)
# b在bus1中下了车，发现也在bus2中下了车
print(bus3.passengers)
print(id(bus1.passengers),id(bus2.passengers),id(bus3.passengers))
# bus1和bus2中的乘客引用的是同一地址值
print('---------------分隔符---------------')
class HauntedBus:
    '''幽灵乘客列车'''

    def __init__ (self,passengers=[]):
        self.passengers=passengers

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

haubus1 = HauntedBus(['a','b'])
haubus1.pick('c')
haubus1.drop('a')
print(haubus1.passengers)
haubus2 = HauntedBus()
haubus2.pick('carrie')
print(haubus2.passengers)
haubus3 = HauntedBus()
# 3车是刚初始化的，但是输出时出现了乘客
print(haubus3.passengers)
haubus3.pick('Dave')
print(haubus3.passengers)
print(haubus2.passengers)
print(haubus2.passengers is haubus3.passengers)
# bus2 和bus3 共用了一辆车
# 没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列表
print('---------------分隔符---------------')
class TwilightBus:
    '''可以杀人的列车'''
    def __init__(self,passengers= None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
    #         此处与Bus不同
    # ，这个赋值语句把 self.passengers 变成 passengers 的别名，而后者是传给
    # __init__ 方法的实参（即示例 8-14 中的 basketball_team）的别名。
    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

ABC_team = ['a','b','c','d','e','f']
tw_bus = TwilightBus(ABC_team)
tw_bus.drop('a')
tw_bus.drop('e')
print(tw_bus.passengers)
print(ABC_team)
# 在tw_bus下车的乘客也在ABC_team消失了

