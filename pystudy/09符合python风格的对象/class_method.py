# 类方法
# 未使用类方法的实现方式
def iget_no_of_instance(ins_obj):
    return ins_obj.__class__.no_inst
class Kls(object):
    no_inst = 0
    def __init__(self):
        Kls.no_inst  = Kls.no_inst+1
#         调用的次数
ik1 = Kls()
ik2 = Kls()
print(iget_no_of_instance(ik1))
# 使用类方法的实现方式
class kls(object):
    no_inst = 0
    def __init__(self):
        kls.no_inst = kls.no_inst+1
    @classmethod
    def get_of_instance(cls_obj):
        return cls_obj.no_inst

ik3 = kls()
ik4 = kls()
ik5 = kls()
print(ik3.get_of_instance())
print(kls.get_of_instance())