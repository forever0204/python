##切片 L[起始:结束:方向]
L = list(range(100))
str='abcdefghijklmn'
A=[1,2,3,4,5]
print(L[0:3])#从0开始到3结束，不包括3
print(L[:3])#0开始，0可以不用写
#print(L[:])#取所有值
print(L[:10:2])#取前10个，每两个取一次
print(str[:5:-1])
print(str[:5:1])
print(A[::-1])
print(A[-1:-6:-1])