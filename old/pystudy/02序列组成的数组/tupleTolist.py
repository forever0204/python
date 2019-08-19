v=(('', 60), ('男', 15691), ('女', 17527))
l1=[]
l2=[]
my_list=list(v)
print(my_list)
print(my_list[0])
for x,y in v:
    l1.append(x)
    l2.append(y)
print(l1,l2)
for sex,num in my_list:
    print(sex,num)