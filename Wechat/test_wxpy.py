from wxpy import *
bot = Bot()
my_friend = bot.friends().search('独年')[0]
my_friend.send('hello wechat')
# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    return '{}'.format(msg.text, msg.type)

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

tuling = Tuling(api_key='80c8c54829fd4d8fbb5702056c409b84')

# 使用图灵机器人自动与指定好友聊天
@bot.register(Group)
def reply_my_friend(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        pass
    else:
        return tuling.do_reply(msg)
# 进入 Python 命令行、让程序保持运行
embed()
#
#    if isinstance(msg.chat, Group) and not msg.is_at:
#       pass
#   else: