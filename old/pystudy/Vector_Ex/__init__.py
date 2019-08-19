#reprlib的使用
import reprlib
# reprlib.aRepr.maxset=2
s = '1234567890'
# s= set(s)
print(s)
# for i in s:
componets = reprlib.repr(s)
print(componets)
