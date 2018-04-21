# 调用 BingoCage 实例，从打乱的列表中取出一个元素
import random
class BingoCage:

    def __init__(self,items):
        self.items = list(items)
        # __init__ 接受任何可迭代对象；在本地构建一个副本，防止列表参数的意外副作用
        print(self.items)
        random.shuffle(self.items)
        # 随机抽取
    def pick(self):
        try:
            return  self.items.pop()
        # 随机抽出一个
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    def __call__(self):
        return self.pick()
    # bingo.pick() 的快捷方式是 bingo()。

bingo =  BingoCage(range(4))

print(bingo.pick())
print(bingo())

print(callable(bingo))
# callable 查看函数对象能否调用