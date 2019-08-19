IND = 'ON'
# 未使用静态方法实现的方式
def checkind():
    return (IND =='ON')
class Kls(object):
    def __init__(self,data):
        self.data = data
    def do_reset(self):
        if checkind():
            print('reset done fror:',self.data)
    def set_db(self):
        if checkind():
            self.db = 'new db connection'
            print('DB connection made for:',self.data)
ik1 = Kls(12)
ik1.do_reset()
ik1.set_db()
# 使用静态方法实现的方式
class kls(object):
    def __init__(self,data):
        self.data =data
    @staticmethod
    def checkind():
        return (IND == 'ON')
    def do_reset(self):
        if checkind():
            print('reset done fror:',self.data)
    def set_db(self):
        if checkind():
            self.db = 'new db connection'
            print('DB connection made for:',self.data)

ik2 = kls(10)
ik2.do_reset()
ik2.set_db()
