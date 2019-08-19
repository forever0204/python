class Animal(object):
    def run(self):
        print('Animal is running...')

def run_twice(animal):
    animal.run()
    animal.run()

class Dog(Animal):
    pass
class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Timer(object):
    # 按照鸭子类型的说法，无需继承animal就可以使用run-twice方法
    def run(self):
        print('start...')

if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    run_twice(cat)
    # 调用方式与cat.run不同
    time = Timer()
    run_twice(time)
