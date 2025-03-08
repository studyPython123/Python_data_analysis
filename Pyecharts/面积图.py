# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 面积图
import os
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.faker import Faker
#%%普通面积图
line =(
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "图例",
        Faker.values(),
        areastyle_opts=opts.AreaStyleOpts(#画面积需要
            opacity=0.5  # 透明度，必须设置
        ),
        itemstyle_opts=opts.ItemStyleOpts(color="orange")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="面积图"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(type_="category",boundary_gap=False)
    )
)
line.render("面积图.html")
os.system("面积图.html")
#%%堆叠面积图
line =(
    Line(init_opts=opts.InitOpts(theme="DARK", width="1200px", height="400px"))
    .add_xaxis(Faker.choose())
    .add_yaxis(
        "图例1",
        Faker.values(),
        areastyle_opts=opts.AreaStyleOpts(
            opacity=0.5  # 透明度
        ),
        itemstyle_opts=opts.ItemStyleOpts(color="orange"),
        stack="堆叠"
    )
    .add_yaxis(
        "图例2",
        Faker.values(),
        areastyle_opts=opts.AreaStyleOpts(
            opacity=0.5  # 透明度
        ),
        itemstyle_opts=opts.ItemStyleOpts(color="pink"),
        stack="堆叠"
    )
    .add_yaxis(
        "图例3",
        Faker.values(),
        areastyle_opts=opts.AreaStyleOpts(
            opacity=0.5  # 透明度
        ),
        itemstyle_opts=opts.ItemStyleOpts(color="red"),
        stack="堆叠"
    )
    .add_yaxis(
        "图例4",
        Faker.values(),
        areastyle_opts=opts.AreaStyleOpts(
            opacity=0.5  # 透明度
        ),
        itemstyle_opts=opts.ItemStyleOpts(color="purple"),
        stack="堆叠"
    )
    .add_yaxis(
        "图例5",
        Faker.values(),
        areastyle_opts=opts.AreaStyleOpts(
            opacity=0.5  # 透明度
        ),
        itemstyle_opts=opts.ItemStyleOpts(color="green"),
        stack="堆叠"
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="堆叠面积图"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(type_="category",boundary_gap=False),#去除边界间隙
        datazoom_opts=opts.DataZoomOpts()
    )
)
line.render("堆叠面积图.html")
os.system("堆叠面积图.html")