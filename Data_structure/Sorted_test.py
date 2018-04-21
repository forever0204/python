# 使用python学习数据结构
# 排序
# 先写内循环，再写外循环

lst = [100,101,10,20,40,33]#一个待排序的数组


pos = len(lst)/2
def quick_sort_2(lst):
#     另一种快排的实现方式
    def qsort(lst,begin,end):
        if begin >= end:
            return
        pivot = lst[begin]
        i=begin
        for j in range(begin+1,end+1):
            if lst[j]<pivot:
                i+=1
                lst[i],lst[j]=lst[j],lst[i]
        lst[begin],lst[i]=lst[i],lst[begin]
        qsort(lst,begin,i-1)
        qsort(lst,i+1,end)
    qsort(lst,0,len(lst)-1)
    return lst
print(quick_sort_2(lst))


def quick_sort_1(lst):
    # 快速排序
    qsort_rec(lst,0,len(lst)-1)
    return lst
def qsort_rec(lst,pos,r):
    # lst 列表，pos 位置值，r
    if pos>= r :
        return
    i=pos
    j=r
    pivot = lst[i]
    while i<j:
        while i<j and lst[j] >=pivot:
            j -=1
        if i<j:
            lst[i] = lst[j]
            i+=1
        while i<j and lst[i]<=pivot:
            i+=1
        if i<j:
            lst[j] = lst[i]
            j-=1
    lst[i] = pivot
    qsort_rec(lst,pos,i-1)
    qsort_rec(lst,i+pos,r)
    return lst
# print(quick_sort(lst))


# lst = [6,5,4,3,2,1]
#       0   1   2  3  4  5   len(lst)=6
# print(range(len(lst)))
# (0,6)  0<=  <6
# for i in range(len(lst)):
#     print(i)
#    0,1,2,3,4,5
def dubble_sorted_4(lst):
#     最优冒泡算法，左右双向排序，同时进行
    for j in range(len(lst)):
        flag = False
        for i in range(j+1,len(lst)-j):
            if lst[i-1]>lst[i]:#正向选择最大，前一位比后一位大
                lst[i-1],lst[i] = lst[i],lst[i-1]
                flag = True
            if lst[len(lst)-i-1]>lst[len(lst)-i]:#反向选择最小，前一位比后一位小
                lst[len(lst) - i - 1],lst[len(lst)-i]=lst[len(lst)-i],lst[len(lst)-i-1]
                flag = True
            else:
                flag =True
                pass
        if not flag:
            break
        print(j,lst)
# dubble_sorted_4(lst)
def dubble_sorted_3(lst):
#     优化后的冒泡排序，可进行左右双向排序，交替进行
    for j in range(len(lst)):
        flag = False
        if j%2==0:
            for i in range(1,len(lst)-int(j/2)):
                    if lst[i-1]>lst[i]:
                        lst[i-1],lst[i]=lst[i],lst[i-1]
                    flag=True
        else:
            for i in range(int((j-1)/2),len(lst)-1):
                # range的范围看出最后一位是len(lst)-2,
                if lst[len(lst)-i-2]>lst[len(lst)-i-1]:
                    lst[len(lst) - i - 2],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[len(lst)-i-2]
                    flag = True
        if not flag:
            break
        print(lst)
    return lst
# print(dubble_sorted_3([100,10,101,111,33,3,44]))
# for j in range(max):
def bubble_sorted_1(lst):
#     未优化的冒泡排序
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if lst[i-1]>lst[i]:
                lst[i-1],lst[i]=lst[i],lst[i-1]
    return lst
# bubble_sorted_1(lst)
def bubble_sorted_2(lst):
    # 半优化后的冒泡排序
    for j in range(len(lst)):
        flag = False
        for i in range(1,len(lst)-j):# 内循环 从1位置开始到第len（lst）-j位置，将最大的放到j位
            if lst[i-1]>lst[i]:    #两两比较找到当前最大的
                lst[i-1],lst[i] = lst[i],lst[i-1]  #如果它的前一位大于当前位置则互换
                flag = True
        if not flag:
            break
    return lst
# print(lst)
# bubble_sorted_2(lst)
# def bubble_sorted_3(lst):
#     左右交替的冒泡

# for i in range(1,len(lst)):#从第二个开始取值
#     x=lst[i]
#     j=i
#     while j>0 and lst[j-1]>x:
#         lst[j]=lst[j-1]
#         # lst_2.append(lst[j-1])
#         j=j-1
#     lst[j] = x
#     print(lst)
# print(lst)
def insert_sort(lst):#插入排序
    for i in range(1,len(lst)): #开始片段[0,1]已排序
        x = lst[i]
        j = i
        # while j>0 and lst[j-1].key > x.key:
        while j>0 and lst[j-1] > x:
            lst[j] = lst[j-1] # 反序逐个后移元素，确定插入位置
            j=j-1 #j自减，从当前位置向下比较
        lst[j] =x  #将i位置的值与j位置值
    return lst
# print(insert_sort(lst))
# 选择排序
# for j in range(len(lst)-1):
#     k=j
#     for i in range(j+1,len(lst)):
#         if lst[i]<lst[k]:
#             k=i
#     if j!=k:
#         lst[j],lst[k]= lst[k],lst[j]
# print(lst)
# for i in range(len(lst)-1): #总循环次数len(lst)-1
#     k=i
#     for j in range(i,len(lst)):
#         if lst[j] < lst[k]:
#             k=j #选出最小的值的位置k
#     # print(j)
#     if i != k:
#         lst[i],lst[k] = lst[k],lst[i] #交换数据
#         print(lst)
# print(lst)
# 选择排序
def select_sort(lst):
    for i in range(len(lst)-1):
        k=i
        for j in range(i,len(lst)):
            if lst[j] < lst[k]:
                k=j  #选出最小的值的位置k
        if i != k:
            lst[i],lst[k] =lst[k],lst[i] #交换数据
    return lst
# print(select_sort(lst))
