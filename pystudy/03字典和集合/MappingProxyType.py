# 不可变映射类型
from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
# d_proxy[2] = 'B'
# TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'
print(d_proxy[2])
# 待完善