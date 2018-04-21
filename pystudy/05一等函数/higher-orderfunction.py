fruits = ['fig','b','strawberry','apple','cherry','banana','orange']
print(sorted(fruits,key=len))
# 调用sorted函数，并根据字段的长度进行排序

def reverse(word):
    return word[::-1]
# 反向输出
print(reverse('hello'))
print(sorted(fruits,key=reverse))
# 根据末尾单词从a-z排序
print(sorted(fruits,key = lambda word:word[::-1]))
# 匿名函数
print('---------------分隔符---------------')

