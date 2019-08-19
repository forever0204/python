# 对numpy的使用和介绍
# NumPy 实现了多维同质数组（homogeneous array）和矩阵，这些数据结构不但能处理数字，
# 还能存放其他由用户定义的记录。通过 NumPy，用户能对这些数据结构里的元素进行高效的操作
# NumPy数组的维数称为秩（rank），一维数组的秩为1，二维数组的秩为2，以此类推。在NumPy中，
# 每一个线性的数组称为是一个轴（axes），秩其实是描述轴的数量。比如说，二维数组相当于是一个一维数组，
# 而这个一维数组中每个元素又是一个一维数组。所以这个一维数组就是NumPy中的轴（axes），而轴的数量——秩，就是数组的维数。
import numpy
a= numpy.arange(12)
print(a)
print('%r' % a)# 命令行模式下的输出
# 新建以恶搞0-11的整数的numpy。ndarry，然后打印出来
print(type(a))
# 查看a的数据类型
print(a.shape)
# 查看数组的（行数，列数） (12,) 一个一维的、有12个元素的数组
a.shape=3,4
print(a)
# 把数组变成2维的
print(a.ndim)
# 打印数组的维度
print(a[2])
print(a[2,1])
# 打印二维数组的值
print(a[:,1])
# 打印第1列
print(a.transpose())
# 打印行和列互换的新数组
print('---------------分隔符---------------')
a2 = numpy.ones((2,3,4), dtype=numpy.int16)
print(a2)
# 创造一个全是1的三维数组
