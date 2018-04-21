#encoding=UTF-8
#!/usr/bin/env python
from wxpy import *
#图灵机器人
#http://www.tuling123.com/member/robot/881179/center/index.jhtml
#api_key='80c8c54829fd4d8fbb5702056c409b84'
bot = Bot(cache_path=True)
#Bot(console_qr =2) 用于终端界面
my_friend = bot.friends().search('独年')[0]
my_friend.send('hello wechat')
tuling = Tuling(api_key='80c8c54829fd4d8fbb5702056c409b84')
#日志
logger = get_wechat_logger(my_friend)

logger.error('打扰大家了，但这是一条重要的错误日志...')
#与朋友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
#群组聊天
@bot.register(Group)
def reply_group_friend(msg):
    return  reply_my_friend(msg)

embed()