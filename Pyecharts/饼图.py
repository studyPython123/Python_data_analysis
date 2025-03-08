# Author: 邵世昌
# CreatTime: 2024/11/12
# FileName: 饼图
#%%导入库
import os
from pyecharts.charts import Pie,Page
import pyecharts.options as opts
from pyecharts.faker import Faker
#%%生成数据
x = Faker.choose()
y = Faker.values()
#%%绘图
pie =(
    Pie(init_opts=opts.InitOpts(theme="withe", width="800px", height="400px"))
    .add("饼图",[list(x) for x in zip(x,y)],
         label_opts=opts.LabelOpts(is_show=True,
            position="outside",
            formatter="{b}-{c}({d}%)"#设置数值标签
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True,
            title="这是一个饼图",
            subtitle="副标题"
        )
    )
    .set_series_opts(#设置标签
        label_opts=opts.LabelOpts(formatter="{b}-{c}-{d}%")
    )
)
pie.render("饼图.html")
os.system("饼图.html")
page = Page(layout=Page.SimplePageLayout)
page.add(pie)
page.render("饼图居中.html")
os.system("饼图居中.html")