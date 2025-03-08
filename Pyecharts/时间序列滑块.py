# Author: 邵世昌
# CreatTime: 2024/11/11
# FileName: 时间序列滑块
import os
from pyecharts.charts import Line, Timeline
from pyecharts.options import LabelOpts
timeline = Timeline()
data_by_year = {
    2020: {"北京": 21893095, "上海": 25000000, "广州": 18810647, "深圳": 17681682},
    2021: {"北京": 21900000, "上海": 25100000, "广州": 18900000, "深圳": 17700000},
    2022: {"北京": 21950000, "上海": 25200000, "广州": 19000000, "深圳": 17800000},
    2023: {"北京": 21893095, "上海": 25000000, "广州": 18810647, "深圳": 17681682},
    2024: {"北京": 21900000, "上海": 25100000, "广州": 18900000, "深圳": 17700000},
    2025: {"北京": 21950000, "上海": 25200000, "广州": 19000000, "深圳": 17800000},
    2026: {"北京": 21893095, "上海": 25000000, "广州": 18810647, "深圳": 17681682},
    2027: {"北京": 21900000, "上海": 25100000, "广州": 18900000, "深圳": 17700000},
    2028: {"北京": 21950000, "上海": 25200000, "广州": 19000000, "深圳": 17800000}
}
for year, data in data_by_year.items(): #用for循环
    bar = Line()
    cities = list(data.keys())
    populations = list(data.values())
    bar.add_xaxis(cities)
    bar.add_yaxis("人口数量", populations, label_opts = LabelOpts(position="right"))
    timeline.add(bar, str(year))#
timeline.add_schema(
    pos_left="5%",  # 时间轴左边距图表左边框为5%的宽度
    play_interval=1000,#每秒改变一次
    is_auto_play=False
)
timeline.render("population_change_with_custom_timeline_position.html")
os.system("population_change_with_custom_timeline_position.html")