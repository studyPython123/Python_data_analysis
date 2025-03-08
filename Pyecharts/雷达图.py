# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 雷达图
import os
from pyecharts.charts import Radar
from pyecharts import options as opts

v1 = [[4300,10000,28000,35000,50000,19000]]#二维列表
v2 = [[5000,14000,28000,31000,42000,21000]]#二维列表

radar = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="项目一",max_ = 6000),
            opts.RadarIndicatorItem(name="项目二",max_ = 16000),
            opts.RadarIndicatorItem(name="项目三",max_ = 30000),
            opts.RadarIndicatorItem(name="项目四",max_ = 38000),
            opts.RadarIndicatorItem(name="项目五",max_ = 60000),
            opts.RadarIndicatorItem(name="项目六",max_ = 22000)
        ]
    )
    .add("数据v1",v1,color="blue")
    .add("数据2",v2,color="red")
)
radar.render("雷达图.html")
os.system("雷达图.html")
