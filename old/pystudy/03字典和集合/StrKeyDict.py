import collections
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return  self[str(key)]
    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return  default
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()
# 基于dict的strkeydict实现方法
class StrKeyDict(collections.UserDict):
    # strkeydict是对userdict的扩展
    def __missing__(self, key):
        if isinstance(key,str):
            raise KeyError(key)
        return  self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)]  = value

d = StrKeyDict([('2','two'),('4','four')])
print(d['2'])
print(d[4])

# print(d[1])