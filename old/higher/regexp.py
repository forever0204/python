import re
re.match(r'^\d{3}\-\d{3,8}$','010-12345')
#判断是否匹配
test= '010-12345'
if re.match(r'^\d{3}\-\d{3,8}$',test):
    print('sucess')
else:
    print('failed')
def catch(reg,str):
    if re.match(reg,str):
        print('sucess')
    else:
        print('failed')
#切分字符串


catch(r'[conmrg]','com')
print('-------------------')
print(re.split(r'[\s\,]+','a, b,,,  c'))

#分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')#较上面的添加了括号
print(m.group(0))
print(m.group(1))
'''
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
'''
#email 验证
email = '1033096826@qq.cn'
reg2 = r'^(.+)\@(\[?[a-zA-Z0-9\-\.]+)\.([a-zA-Z]{2,3}|[0-9]{1,3}\]?)$'
reg = r'^(.+)\@(\w+)\.([conmrg]+)$'
def isEmail(email):
    return True if re.match(reg, email) else False
def splitEmail(email):
    return re.match(reg, email)
print('%s is email : %s' % (email, isEmail(email)))
print('%s split to groups : %s' % (email, splitEmail(email).groups()))