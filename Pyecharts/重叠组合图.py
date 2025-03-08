# Author: 邵世昌
# CreatTime: 2024/11/15
# FileName: 重叠组合图
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker
import os

# 数据
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

# 条形图
bar = (
    Bar()
    .add_xaxis(Faker.months)  # ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    # 默认轴索引都为0
    .add_yaxis("蒸发量", v1)
    .add_yaxis("降水量", v2)

    # 提前配置 折线图 的 y 轴
    .extend_axis(
        # 对新增y轴设置，轴标签为 摄氏度 间隔为5°C
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5
        )
    )

    # 系列配置项   不显示标签
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    # 全局配置项
    .set_global_opts(
        # 标题
        title_opts=opts.TitleOpts(title="Overlap-bar+line"),
        # 对条形图的 y 轴进行设置
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} ml")),
    )
)

# 折线图
line = (
    Line()
    .add_xaxis(Faker.months)  # x轴
    .add_yaxis(
        "平均温度",
        v3,
        yaxis_index=1  # 上面的条形图默认索引为0，这里设置折线图y 轴索引为1
    )
    .set_series_opts(
        # 标记点
        markpoint_opts=opts.MarkPointOpts(
            data=[  # 特殊标记值,min,max,mean
                opts.MarkPointItem(
                    type_="max",
                    symbol="pin",  # 标记的图形
                    symbol_size=50,  # 标记点的大小
                    itemstyle_opts=opts.ItemStyleOpts(color="green")
                ),
                opts.MarkPointItem(
                    type_="min",
                    symbol="pin",
                    symbol_size=50,
                    itemstyle_opts=opts.ItemStyleOpts(color="red")
                )
            ]
        )
    )
)

bar.overlap(line)  # 将折线图重叠到条形图
bar.render("重叠组合图.html")
os.system("重叠组合图.html")
