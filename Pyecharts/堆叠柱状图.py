# Author: 邵世昌
# CreatTime: 2024/11/12
# FileName: 堆叠柱状图
import os

from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.faker import Faker
#%%
bar = (
    Bar()
    .add_xaxis(Faker.clothes)
    .add_yaxis("商家A", Faker.values(),
               stack="abc",
               itemstyle_opts=opts.ItemStyleOpts(color="yellow"),
               label_opts=opts.LabelOpts(
                   is_show=True,position="inside",formatter="{c}"
               )
    )#stack堆叠效果
    .add_yaxis("商家B", Faker.values(),
               stack="abc",
               itemstyle_opts=opts.ItemStyleOpts(color="pink"),
               label_opts=opts.LabelOpts(
                   is_show=True,position="inside",formatter="{c}"
               )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title = "堆叠柱状图",
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
bar.render("堆叠柱状图.html")
os.system("堆叠柱状图.html")