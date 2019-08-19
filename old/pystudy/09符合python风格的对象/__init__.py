class Vector_test(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)
    def __iter__(self):
        return (i for i in (self.x,self.y))
if __name__ == '__main__':
    v1 = Vector_test(1,2)
    print(v1)