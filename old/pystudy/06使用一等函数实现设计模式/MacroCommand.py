class MacroCommand:
    '''执行一组命令的命令'''
    def __init__(self,commands):
        self.commands = list(commands)
    # 使用 commands 参数构建一个列表，这样能确保参数是可迭代对象，还能在各个MacroCommand 实例中保存各个命令引用的副本。
    def __call__(self):
        for command in self.commands:
            command()
    # 调用 MacroCommand 实例时，self.commands 中的各个命令依序执行。


