from datetime import datetime, timedelta, timezone

import re

now = datetime.now()
print(now)
print(type(now))
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())
# timestamp 和 datetime 的互相转换
t = dt.timestamp()
print(datetime.fromtimestamp(t))
#当前时间就是相对于epoch time的秒数，称为timestamp。

#str 到datetime 的转换
today = datetime.strptime('2017-7-8 13:27:12','%Y-%m-%d %H:%M:%S')
today1 = datetime.strptime('20170708 12:12:12','%Y%m%d %H:%M:%S')
print('测试 %s'% today1)

#datetime 加减
'''
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
'''
print(now+timedelta(hours=10))
print(now-timedelta(days=1))

#本地时间转换为utc时间
'''
一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
'''
tz_utc_8 = timezone(timedelta(hours=8))
dt1 = now.replace(tzinfo=tz_utc_8)
print(dt1)

#时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc 0 时区：',utc_dt)
#北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间：',bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt ,tokyo_dt2 )#结果是相同的

def to_timestamp(dt_str,tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz = re.split(r'[UTC\:]+',tz_str)
    tz_h = int(tz[1])
    #print(tz_h)
    dt = dt.replace(tzinfo=timezone(timedelta(hours=tz_h)))
    return dt.timestamp()
print(to_timestamp('2015-6-1 08:10:30','UTC+7:00'))
print(to_timestamp('2015-5-31 16:10:30','UTC-09:00'))