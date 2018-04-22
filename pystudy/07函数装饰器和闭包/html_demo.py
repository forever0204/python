import html
# 介绍单分派泛函数
# def htmlize(obj):
#     content  = html.escape(repr(obj))
#     return '<pre>{}</pre>'.format(content)
#
# print(htmlize({1,2,3}))
# print(htmlize('Heimlich & Co.\n- a game'))
# print(htmlize(['alpha', 66, {3, 2, 1}]))

registry = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'
            % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate
@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')
