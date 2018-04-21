class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s:%s' %(self.__name,self.__score))


    def get_grade(self):
        if self.__score>= 90:
            return  'A'
        elif self.__score>=60:
            return  'B'
        else:
            return 'C'

a = Student('a',70)
a.print_score()
a.set_score(98)
print('Grade of a:',a.get_grade())
#print(a.__class__name)