import functools
# functools函数
def log(methon_name = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(methon_name, str):
                print('%s %s()' % (methon_name, func.__name__ ))
                s = func(*args, **kw)
                print('%s %s()' % (methon_name, func.__name__ ))
            else:
                print('begin call %s()' % func.__name__)
                s = func(*args, **kw)
                print('end call %s()' % func.__name__)
            return s
        return wrapper
    return decorator

@log()
def time():
    print('2017-06-19')

time()