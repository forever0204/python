from wxpy import *
#http://wxpy.readthedocs.io

bot = Bot(cache_path=True)
q1 = '你好？'
a1 = '我不好'
@bot.register()
def print_messages(q1):
    print(a1)
# 打印所有*群聊*对象中的*文本*消息
@bot.register(Group, TEXT)
def print_group_msg(msg):
    print(msg)
# 堵塞线程，并进入 Python 命令行
embed()