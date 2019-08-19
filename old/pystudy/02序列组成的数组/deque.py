# 介绍collections 的deque类（双向队列）
from collections import deque
dq = deque(range(10),maxlen=10)
# maxlen 是一个可选参数，代表这个队列看容纳的元素数量，且一旦设定不可更改
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
# 队列的旋转操作接受一个参数 n，当 n > 0 时，队列的最右边的 n 个元素会被移动到
# 队列的左边。当 n < 0 时，最左边的 n 个元素会被移动到右边。
dq.appendleft(-1)
print(dq)
dq.append(-1)
print(dq)
# 当试图对一个已满（len(d) == d.maxlen）的队列做尾部添加操作的时候，它头部
# 的元素会被删除掉。注意在下一行里，元素 0 被删除了。
dq.extend([11, 22, 33])
print(dq)
# 在尾部添加3个元素挤掉了头部的3个元素
print('---------------分隔符---------------')
# ？把 .append和 .pop(0) 合起来用，就能模拟栈的“先进先出”的特点
''''
堆栈：
堆栈是一个后进先出(LIFO)的数据结构。
在栈上"push"元素是个常用术语，意思是把一个对象添加到堆栈中。
删除一个元素，可以把它"pop"出堆栈。
队列：
队列是一种先进先出(FIFO)的数据类型。
新的元素通过"入队"的方式添加进队列的末尾，
"出对"就是从队列的头部删除。
'''
L= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L.append(-1)
# 尾部添加元素-1
L.pop(0)
# 删除头部
print(L)