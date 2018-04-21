import json

d = dict(name='bob', age=20, score=88)
print(json.dumps(d))
'''
上面使用json.dumps的方法将一个python对象进行了json格式的转换，这个过程就是一个序列化的过程
而要将一个json反序列化为python对象，用json.load()或者json.loads()方法
JSON类型	    Python类型
{}	            dict
[]	            list
"string"	    str
1234.56	        int或float
true/false	    True/False
null	        None
'''
json_str = json.dumps(d)
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('bob', 20, 88)
print(json.dumps(s, default=student2dict))
