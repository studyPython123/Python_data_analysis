# Author: 邵世昌
# CreatTime: 2024/11/12
# FileName: 玫瑰图
#%%导入库
import os
from pyecharts.charts import Pie
import pyecharts.options as opts
from pyecharts.faker import Faker
#%%生成数据
key = Faker.choose()
value = Faker.values()
#%%绘图
pie =(
    Pie(init_opts=opts.InitOpts(theme="dark", width="1200px", height="800px"))
    .add("饼图",
         [list(x) for x in zip(key,Faker.values())],
         label_opts=opts.LabelOpts(
             is_show=True,
            position="outside",
            formatter="{b}-{c}（{d}%）"#设置数值标签
        ),
         radius=["10%","30%"],#设置图的内半径和外半径
         center=["25%","25%"],#设置左右上下位置
         rosetype="radius"
    )
    .add("饼图",
         [list(x) for x in zip(key, Faker.values())],
         label_opts=opts.LabelOpts(
             is_show=True,
             position="outside",
             formatter="{b}-{c}（{d}%）"  # 设置数值标签
         ),
         radius=["10%","30%"],
         center=["75%", "25%"],
         rosetype="radius"
    )
    .add("饼图",
         [list(x) for x in zip(key, Faker.values())],
         label_opts=opts.LabelOpts(
             is_show=True,
             position="outside",
             formatter="{b}-{c}（{d}%）"  # 设置数值标签
         ),
         radius=["10%","30%"],
         center=["25%", "75%"],
         rosetype="radius"
    )
    .add("饼图",
         [list(x) for x in zip(key, Faker.values())],
         label_opts=opts.LabelOpts(
             is_show=True,
             position="outside",
             formatter="{b}-{c}（{d}%）"  # 设置数值标签
         ),
         radius=["10%","30%"],
         center=["75%", "75%"],
         rosetype="radius"
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True,
            title="这是一个玫瑰图",
            subtitle="副标题"
        )
    )
    # .set_series_opts(#设置标签
    #     label_opts=opts.LabelOpts(formatter="{b}-{c}")
    # )
)
pie.render("玫瑰图.html")
os.system("玫瑰图.html")
