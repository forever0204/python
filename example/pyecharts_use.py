# python操作图表可视化
import pyecharts
# 1
# bar=pyecharts.Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.show_config()
# bar.render()

# 2 热度图
# Geodata=[ ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15), ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21), ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25)]
# geo=pyecharts.Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",width=1200, height=600, background_color='#404a59')
# attr,value =geo.cast(Geodata)
# geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
# geo.show_config()
# geo.render()

# Radarschema =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
# v1 =[[4300, 10000, 28000, 35000, 50000, 19000]]
# v2 =[[5000, 14000, 28000, 31000, 42000, 21000]]
# radar =pyecharts.Radar()
# radar.config(Radarschema)
# radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
# radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
# radar.show_config()
# radar.render()

# 折线图
date = ["2017-11-15","2017-11-16","2017-11-17","2017-11-18","2017-11-19","2017-11-20"]
wendu1 = [17.4,18.8,20.2,23.3,19.0,18.8]
wendu2 = [18.3,19.2,21.1,22.3,17.0,19.8]
wendu3 = [17.2,18.0,22.1,23.0,19.0,18.7]
wendu4 = [18.0,19.1,20.1,22.1,18.8,19.1]
chart = pyecharts.Line ("温湿度图表")
chart.add("采集点1",date,wendu1,mark_point=["average"])
chart.add("采集点2",date,wendu2,mark_point=["average"])
chart.add("采集点3",date,wendu3,mark_point=["average"])
chart.add("采集点4",date,wendu4,mark_point=["average"])
chart.show_config()
chart.render()