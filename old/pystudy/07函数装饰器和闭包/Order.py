# 优化第6章中的订单
# 使用装饰器可解决新增策略自动加入best方法
promos = []
def promotion(promo_func):
    promos.append(promo_func)
    return  promo_func

@promotion
def fidelity_promo(order):
    '''为积分1000或以上的顾客提供5%折扣'''
    return  order.total()*.05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item_promo(order):
    '''单个商品为20个或以上时提供10%折扣'''
    discount = 0
    for item in order.cart:
        if item.quantity >=20:
            discount += item.total()*.1
    return discount
@promotion
def large_order_promo(order):
    '''订单中的不同商品达到10个或以上时提供7%的折扣'''
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >=10:
        return order.total()*.07
    return 0

# @promotion
# def test_order_promo(order):
#     return 0
# 新增测试策略可直接输出到promos列表中
# 可与order_fun进行对比

def best_promo(order):
    '''选择可用的最佳折扣'''
    return max(promo(order) for promo in promos)

print(promos)