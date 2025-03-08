# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 象形柱状图
import os
from pyecharts.charts import PictorialBar
from pyecharts import options as opts
from pyecharts.globals import SymbolType
from pyecharts.faker import Faker

pictionbar = (
    PictorialBar()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "图例",
       Faker.values(),
       label_opts=opts.LabelOpts(is_show=False),
        symbol=SymbolType.ROUND_RECT, #符号类型
        symbol_repeat="fixed",#重复方式
        symbol_size= 16,
        is_symbol_clip=True, #符号裁剪
        itemstyle_opts=opts.ItemStyleOpts(
            color="orange"
        )
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="象形柱状图"
        ),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),#不显示y轴刻度
            axisline_opts=opts.AxisLineOpts(is_show=False)#不显示y轴的线
        )
    )
)
pictionbar.render("象形柱状图.html")
os.system("象形柱状图.html")