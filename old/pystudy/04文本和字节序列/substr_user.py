# 元组中的每个元素的字段截取
sfz=(('32118319940412031X',), ('321183199111211330',), ('32118319931028003X',))
my_list=list(sfz)
for x in my_list:
    print(x[0][6:10])
print(my_list)