# 排序可以使用list.sort方法和sorted函数，前者会就地排序列表，而后者是生成一个新的列表
fruits = ['grape','raspberry','apple','banana']
print(sorted(fruits))#产生了新的列表
print(fruits)#原列表无影响
print(sorted(fruits,reverse=True))
#按照字母降序排列
print(sorted(fruits, key=len))
# 按照字母长度的排序
print(sorted(fruits,key=len,reverse=True))
# 按照长度降序排序的结果。结果并不是上面那个结果的完全翻转，因为用到的排序算
# 法是稳定的，也就是说在长度一样时，grape 和 apple 的相对位置不会改变。
#到此位置fruits是没有改变的
fruits.sort()
print(fruits)# fruits本身被排序
# bisect 模块包含两个主要函数，bisect 和 insort，两个函数都利用二分查找算法来在有序序列中查找或插入元素
import bisect
import sys
HAYSTACK = [1,3,5,6,9]
NEEDLES = [0,2,4,6,8]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'
def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        # 用特定的bisect函数计算元素出现的位置
        offset = position * '  |'
        # 计算分割符号
        print(ROW_FMT.format(needle, position, offset))
         # 把元素和其一个出现的位置打印出来
if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        # 根据命令上最后一个参数选用bisect函数
        # 如何使用：在运行出点击edit configuration 后在script parameters处输入最后一个值输入为left即可
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    # 打印选用的函数
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)
# 运行demo方法
for i in NEEDLES:
    bisect.insort(HAYSTACK,i)
#   insort(seq, item) 把变量 item 插入到序列 seq 中
print(HAYSTACK)
# 如何去重？加入判断
HAYSTACK1 = [1,3,5,6,9]
for i in NEEDLES:
    if i in HAYSTACK1:
        pass
    else:
        bisect.insort(HAYSTACK1,i)
print(HAYSTACK1)

def grade(score, breakpoints=[60, 70,80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])
# 根据一个分数，找到它所对应的成绩
print('---------------分隔符---------------')
# 自写的冒泡排序法
array = [1, 2, 5, 3, 6, 8, 4]
for i in range(len(array)-1):
    # print('i: ',i)
    for j in range(len(array)-i-1):
        # print('j: ',j)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)