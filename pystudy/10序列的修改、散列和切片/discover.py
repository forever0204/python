import functools
import numpy as np
# 对第1列的数据求和
my_list = [[1,2,3],[40,50,60],[9,8,7]]
print(list(x[1] for x in my_list))
total=0
for sub in my_list:
    total+=sub[1]
print(total)

# for循环
print(sum(sub[1] for sub in my_list))
# sum函数
print(functools.reduce(lambda a,b:a+b,[sub[1] for sub in my_list]))

print(functools.reduce(lambda a,b:a+b[1],my_list,0))
# lambda 表达式

my_array = np.array(my_list)
print(np.sum(my_array[:,1]))
# numpy多维数组求和
