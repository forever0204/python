def insert_sort(lst):#插入排序
    #
    for i in range(1,len(lst)): #开始片段[0,1]已排序
        x = lst[i]
        j = i
        while j>0 and lst[j-1] > x:
            lst[j] = lst[j-1] # 反序逐个后移元素，确定插入位置
            j=j-1 #j自减，从当前位置向下比较
        lst[j] =x  #将i位置的值与j位置值
    return lst

def select_sort(lst):# 选择排序
    # 每一次内循环选出最小的值，外循环控制次数
    for i in range(len(lst)-1):#总循环次数len(num)-1
        k=i
        for j in range(i,len(lst)):
            if lst[j] < lst[k]:
                k=j #选出最小的值的位置k
        if i != k:
            lst[i],lst[k] =lst[k],lst[i] #交换数据
    return lst

def bubble_sort_1(lst):#冒泡排序
    # 未优化的冒泡排序
    for i in range(len(lst)-1): #外循环
        for j in range(1,len(lst)-i):# 内循环
            if lst[j-1] >lst[j]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
        print(lst)
    return lst

def bubble_sort_2(lst):#冒泡改进版
    # 加入found判断内循环是正序，则置1退出循环
    # 可使用一个排序好的进行比较
    for i in range(len(lst)-1):
        found =False
        for j in range(1,len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
                found=True
        if not found:
            break
        print(lst)
    return lst
def bubble_sort_3(lst):#冒泡再改进版
#     可进行左右双向排序
    for j in range(len(lst)):
        flag = False
        if j%2==0:
            for i in range(1,len(lst)-int(j/2)):
                    if lst[i-1]>lst[i]:
                        lst[i-1],lst[i]=lst[i],lst[i-1]
                    flag=True
        else:
            for i in range(int((j-1)/2),len(lst)-1):
                # range的范围看出最后一位是len(num)-2,
                if lst[len(lst)-i-2]>lst[len(lst)-i-1]:
                    lst[len(lst) - i - 2],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[len(lst)-i-2]
                    flag = True
        if not flag:
            break
        print(lst)
    return lst
def bubble_sort_4(lst):#冒泡再再改进版
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
        print(lst)
    return lst

if __name__ == '__main__':
    print(bubble_sort_1([100,10,101,111,33,3,44]))
    print('---------------分隔符---------------')
    print(bubble_sort_2([100,10,101,111,33,3,44]))
    print('---------------分隔符---------------')
    print(bubble_sort_3([100,10,101,111,33,3,44]))
    print('---------------分隔符---------------')
    print(bubble_sort_4([100,10,101,111,33,3,44]))