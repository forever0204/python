# 格式化打印
# 与awk进行比较
print("I'm %s. I'm %d year old" % ('Vamei', 99))
'''
%s      优先使用str()进行字符串转换
%r      优先使用repr()进行字符串转换
%d/%i   转成有符号十进制数
%u      转成无符号十进制数
'''
string = "Hello\tWill\n"
print("%s" %string)
print("%r" %string)
# %s 和 %r 的区别
print("%c" % '!')
'''
* 定义宽度或者小数点精度
- 用来左对齐
+ 显示加号
# 在八进制数前面显示零(0)，在十六进制前面显示"0x"或者"0X"（取决于用的是"x"还是"X"）
0 在显示的数字前填充0
(var) 映射变量
m.n m 是显示的最小总宽度，n 是小数点后的位数（如果可用的话）
'''
print('---------------分隔符---------------')
num = 100

print("%d to hex is %x" %(num, num))
print("%d to hex is %X" %(num, num))
print("%d to hex is %#x" %(num, num))
print("%d to hex is %#X" %(num, num))

# 浮点数
f = 3.1415926
print("value of f is: %.4f" %f)

# 指定宽度和对齐
students = [{"name":"Wilber", "age":27}, {"name":"Will", "age":28}, {"name":"June", "age":27}]
print("name: %10s, age: %10d" %(students[0]["name"], students[0]["age"]))
print("name: %-10s, age: %-10d" %(students[1]["name"], students[1]["age"]))
print("name: %*s, age: %0*d" %(10, students[2]["name"], 10, students[2]["age"]))

# dict参数
for student in students:
    print("%(name)s is %(age)d years old" % student)

# 字符串模板


# format（）