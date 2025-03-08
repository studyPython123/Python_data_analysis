# Author: 邵世昌
# CreatTime: 2024/11/12
# FileName: 条形图
import os

from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.faker import Faker
#%%
bar = (
    Bar()
    .add_xaxis(Faker.clothes)
    .add_yaxis("商家A", Faker.values(),
               itemstyle_opts=opts.ItemStyleOpts(color="yellow"),
               label_opts=opts.LabelOpts(
                   is_show=True,position="inside",formatter="{c}"
               ),
               # gap="0%",#不同系列之间的距离变直方图
               category_gap="0%"#单个系列之间的距离
    )#stack堆叠效果
    # .add_yaxis("商家B", Faker.values(),
    #            itemstyle_opts=opts.ItemStyleOpts(color="pink"),
    #            label_opts=opts.LabelOpts(
    #                is_show=True,position="inside",formatter="{c}"
    #            ),
    #             gap="0%"#变直方图
    # )
    #交换轴
    # .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title = "条形图",
            subtitle="副标题"
        ),
        xaxis_opts=opts.AxisOpts(name="服装"),
        yaxis_opts=opts.AxisOpts(name="销量"),
        datazoom_opts=[
            opts.DataZoomOpts(),
            opts.DataZoomOpts(type_="inside")#鼠标滚轮缩放
        ]
    )
)
bar.render("条形图.html")
os.system("条形图.html")
