from wxpy import *
#小I机器人
bot = Bot()
my_friend = bot.friends().search('独年')[0]
my_friend.send('hello wechat')
xiaoi = XiaoI('Wl7IdKmooH58', 'UHMa7iJ0yz9M5PHK0jTJ')
#Key：Wl7IdKmooH58
#Secret：UHMa7iJ0yz9M5PHK0jTJ
# 使用小 i 机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    xiaoi.do_reply(msg)


@bot.register(Group)
def auto_reply(msg):
    # 如果是群聊，但没有被 @，则不回复
#    if isinstance(msg.chat, Group) and not msg.is_at:
#       return
#   else:
        # 回复消息内容和类型
    return reply_my_friend(msg)

# 进入 Python 命令行、让程序保持运行
embed()