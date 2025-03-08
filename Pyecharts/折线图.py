# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 折线图
import os
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.faker import Faker

line = (
    Line(init_opts=opts.InitOpts(theme="DARK"))
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "图例1",
        Faker.values(),
        # is_smooth=True,
        #点属性
        itemstyle_opts=opts.ItemStyleOpts(#点的类型
            color="purple",
            border_color="green",
            border_width=2,
        ),
        symbol="triangle",#点的符号
        symbol_size=10,#点的大小
        #线属性
        linestyle_opts=opts.LineStyleOpts(
            color="red",
            type_="dashed",#线条类型
        )
    )
    .add_yaxis(
        "图例2",
        Faker.values(),
        # is_smooth=True,
        itemstyle_opts=opts.ItemStyleOpts(color="blue")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="折线图"),
        tooltip_opts=opts.TooltipOpts(trigger="axis")
    )
    .set_series_opts(
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
                    itemstyle_opts=opts.ItemStyleOpts(color="orange")
                )
            ]
        ),
        # 标记线
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average",
                                  name="平均线")
            ],
            label_opts=opts.LabelOpts(color="purple"),
            linestyle_opts=opts.LineStyleOpts(
                # color="pink",
                type_="dashed"
            ),
        )
    )
)
line.render("折线图.html")
os.system("折线图.html")