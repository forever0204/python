# 使用列表推导计算笛卡儿积
colors = ['black','white']
sizes = ['s','m','l']
tshirts = [(color,size) for color in colors
                        for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color,size))


L1 = [1,2]
L2 = [3,4]
L = [(x*y) for x in L1
            for y in L2]
print(L)