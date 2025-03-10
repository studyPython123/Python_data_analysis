# Author: 邵世昌
# CreatTime: 2025/3/7
# FileName: bar
from cutecharts.charts import Bar
from cutecharts.components import Page
from cutecharts.faker import Faker

def bar_base() -> Bar:
    chart = Bar("Bar-基本示例")
    chart.set_options(labels=Faker.choose(), x_label="I'm xlabel", y_label="I'm ylabel")
    chart.add_series("series-A", Faker.values())
    return chart
def bar_tickcount_colors():
    chart = Bar("Bar-调整颜色")
    chart.set_options(labels=Faker.choose(), y_tick_count=10, colors=Faker.colors)
    chart.add_series("series-A", Faker.values())
    return chart
bar_base().render('bar.html')
import os
os.startfile('bar.html')


