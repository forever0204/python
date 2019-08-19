# 查看何时使用装饰器
registry = []
# 用来保存@ewgoster装饰的函数
def register(func):
    print('running register(%s)' % func)
    # 显示被装饰的函数
    registry.append(func)
    # 将函数加入到registy
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()
if __name__=='__main__':
    main()

# running register(<function f1 at 0x000001695C13C620>)
# running register(<function f2 at 0x000001695C13C6A8>)
# running main()
# registry -> [<function f1 at 0x000001695C13C620>, <function f2 at 0x000001695C13C6A8>]
# running f1()
# running f2()
# running f3()
# 注意，register 在模块中其他函数之前运行（两次）。调用 register 时，传给它的参
# 数是被装饰的函数，例如 <function f1 at 0x100631bf8>。
# 加载模块后，registry 中有两个被装饰函数的引用：f1 和 f2。这两个函数，以及 f3，
# 只在 main 明确调用它们时才执行。