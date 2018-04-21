#生父
class Father():

    def func(self):
        print('生父打儿子')
#隔壁老王
class LaoWang():

    def func(self):
        print('老王打儿子')
#继父
class StepFather():

    def func(self):
        print('继父打儿子')

#神秘人
class Mysterious(Father,StepFather,LaoWang):
    pass

##让我们看看到底谁打了儿子
s=Mysterious()
s.func()

#第一个继承是生父，后边的都是继父



class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 各种动物:
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Runnable):
    pass

