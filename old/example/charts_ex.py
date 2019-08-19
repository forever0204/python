# 使用句容的毕业生档案和pycharts进行可视化分析
from pyecharts import Pie
from pyecharts import Bar
'''
年龄分布  身份证
毕业院校
专业
性别
学历
'''
# 数据库取值
import pymysql
conn = pymysql.connect('localhost','bt31User','bt31User','bt31db')
# 配置链接数据库
cursor = conn.cursor()
sex = []
sex_value = []
# 创建游标
# cursor.execute('select * from pic')
# # 执行语句
# cursor.execute("select xb,count(1) from app_assetcustominfo200 where xb in ('','男','女')  group by xb")
cursor.execute("select sfz from app_assetcustominfo200 where sfz!='' ")
# sqli="insert into pic values(%s)"
# cursor.execute(sqli,('2 year 1 class'))
v = cursor.fetchall()
# 性别比例
# for k,num in v:
#     sex.append(k)
#     sex_value.append(num)
# # print(sex,sex_value)
# sex_pie = Pie('性别比例')
# sex_pie.add("", sex, sex_value, is_label_show=True)
# sex_pie.show_config()
# sex_pie.render()
# 获取数据并打印
# 年龄:使用柱状图进行展示
sfz=[]
num=[]
age=[]
#
for x in list(v):
    sfz.append(x[0][6:10])
print(sfz)
sfzset = set(sfz)
# print(ageset)
for year in sfzset:
    if year.isdigit():
        # 判断count是不是字符即是否可被int
        if int(year)>1990 and int(year)<2000:
        # 判断count的值的区间
            num.append(sfz.count(year))
            age.append(str(year))
            # print(year,sfz.count(year))
        else:
            pass
    else:
        pass
print(age)
print(num)
bar = Bar("年龄统计")
bar.add("年龄",age,num)
bar.show_config()
bar.render()
    # if int(count)>1990 and int(count)<2000:
    #     print(count,age.count(count))
    # else:
    #     pass
cursor.close()
# 关闭游标
conn.close()
# 关闭链接
# 使用饼图进行性别分析
