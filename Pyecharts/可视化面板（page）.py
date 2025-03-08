# Author: 邵世昌
# CreatTime: 2024/11/15
# FileName: 可视化面板（page）
from pyecharts.charts import Bar, Line,Pie, Page,Liquid
import pyecharts.options as opts
from pyecharts.faker import Faker
#%%柱
def bar() -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme="withe",width="1200px",height="400px"))
        .add_xaxis(Faker.choose())
        .add_yaxis("柱状图", Faker.values(),itemstyle_opts=opts.ItemStyleOpts(color="blue"))
        .set_global_opts(title_opts=opts.TitleOpts(title="柱状图",pos_left="2%",pos_top="2%"))
    )
    return  bar
import os
extra_text = '<link rel="stylesheet" type="text/css" href="styles.css">'
bar().render("test.html",extra_html_text_head = extra_text)
os.system("test.html")
#%%折线图
def line() -> Line:
    line = (
        Line(init_opts=opts.InitOpts(theme="withe",width="1200px",height="400px"))
        .add_xaxis(Faker.choose())
        .add_yaxis("折线图", Faker.values(),itemstyle_opts=opts.ItemStyleOpts(color="pink"),label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title="折线图",pos_left="2%",pos_top="2%"))
        .set_series_opts(
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(
                        type_="max",
                        symbol="pin",#标记的图形
                        symbol_size=50,#标记点的大小
                        itemstyle_opts=opts.ItemStyleOpts(color="green")
                    ),
                    opts.MarkPointItem(
                        type_="min",
                        symbol="pin",
                        symbol_size=50,
                        itemstyle_opts=opts.ItemStyleOpts(color="red")
                    )
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average",
                                      name="平均线")
                ],
                label_opts=opts.LabelOpts(color="purple")
            )
        )
    )
    return line

#%%饼图
def pie() -> Pie:
    pie = (
        Pie(init_opts=opts.InitOpts(theme="withe",width="1200px",height="400px"))
        .add("饼图", [list(x) for  x in zip(Faker.choose(),Faker.values())],
             label_opts=opts.LabelOpts(
                 is_show=True,
                 position="outside",
                 formatter="{b}-{c}（{d}%）"  # 设置数值标签
             ),
             radius=["30%", "60%"],  # 设置图的内半径和外半径
             center=["50%", "50%"],  # 设置左右上下位置
             rosetype="radius"
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="玫瑰图",pos_top="2%",pos_left="2%"),
            legend_opts=opts.LegendOpts(pos_top="5%")
        )
    )
    return pie

#%%水滴图
def liquid() -> Liquid:
    liquid = (
        Liquid(init_opts=opts.InitOpts(theme="withe",width="1200px",height="400px"))
        .add("水滴图",[0.45,0.45])
        .set_global_opts(title_opts=opts.TitleOpts(title="今日湿度",pos_top="2%",pos_left="2"))
    )
    return liquid

# %%组合图
def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        bar(), line(), pie(), liquid()
    )
    page.render("可视化数据面板.html")
page_draggable_layout()
os.system("可视化数据面板.html")
# if __name__ == "__main__":
#     page_draggable_layout()
#%%
page = Page(layout=Page.SimplePageLayout)
page.add(
    bar(), line(), pie(), liquid()
)
page.render("可视化数据面板.html")
os.system("可视化数据面板.html")
#%%
page.save_resize_html(source="可视化数据面板.html", cfg_file="chart_config.json", dest="可视化数据面板.html")#每一次需要调整
os.system("可视化数据面板.html")