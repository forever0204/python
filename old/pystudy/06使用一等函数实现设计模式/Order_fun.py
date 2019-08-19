# 使用函数实现的策咯模式
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')
class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product#商品名称
        self.quantity = quantity#商品重量
        self.price = price#商品价格
    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self,customer,cart,promotion=None):
        self.customer= customer
        self.cart = cart
        self.promotion = promotion
        # customer 客户 cart 购物车 promotion 策略接口，即使用某种付款方式

    def total(self):
        if not hasattr(self,'__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    # 计算总价
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    #计算折扣
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return  fmt.format(self.total(),self.due())
    # 格式化输出

def fidelity_promo(order):
    '''为积分1000或以上的顾客提供5%折扣'''
    return  order.total()*.05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    '''单个商品为20个或以上时提供10%折扣'''
    discount = 0
    for item in order.cart:
        if item.quantity >=20:
            discount += item.total()*.1
    return discount
def large_order_promo(order):
    '''订单中的不同商品达到10个或以上时提供7%的折扣'''
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >=10:
        return order.total()*.07
    return 0
# def null_order_promo(order):
#     return 0
# 测试内省模块的全局命名空间，构建 promos 列表是否可以读取到

# 1.手动添加
# promos = [fidelity_promo, bulk_item_promo, large_order_promo]
# 2.全局变量
promos = [globals()[name] for name in globals()# 迭代globals（）返回字典的各个name
          if name.endswith('_promo')# 选择以——promo结尾的名称
          and name != 'best_promo']# 过滤掉best_promo自身
# 3.导入 promotions 模块，以及提供高阶内省函数的 inspect 模块
# promos = [func for name,func in
#                 inspect.getmembers(promotions,inspect.isfunction)]

print(promos)
def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)


joe = Customer('john Doe', 0)#无积分
ann = Customer('Ann Smith', 1100)#过千积分A

cart1 = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5), LineItem('water', 5, 5.0)]
# 购物车1
cart2 = [LineItem('banana', 30, .8), LineItem('apple', 10, 1.5)]
# 购物车2 超过20件
cart3 = [LineItem(str(item_code), 1, 1.0)
         for item_code in range(10)]
# 购物车3 生成10种商品类型
print(Order(joe,cart1,fidelity_promo))
# 无积分订单 无折扣42.0
print(Order(ann,cart1,fidelity_promo))
# 过千积分5%折扣，42-2.1=39.9
print(Order(joe,cart2,bulk_item_promo))
print(Order(joe,cart2,large_order_promo))
# 有超过20数量的订单
print(Order(joe,cart3,large_order_promo))

# 思考：√1.如何自动选择模式
#      2.多种折扣如何选择
#      √3.新增策略如何添加
print('---------------分隔符---------------')
print(Order(joe,cart1,best_promo))
print(Order(joe,cart2,best_promo))
print(Order(ann,cart2,best_promo))
print(Order(joe,cart3,best_promo))