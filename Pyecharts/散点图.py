# Author: 邵世昌
# CreatTime: 2024/11/21
# FileName: 散点图
import os
from pyecharts.charts import Scatter
import pyecharts.options as opts
data = [
    [10.0, 8.04],
    [8.0, 6.95],
    [13.0, 7.58],
    [9.0, 8.81],
    [11.0, 8.33],
    [14.0, 9.96],
    [6.0, 7.24],
    [4.0, 4.26],
    [12.0, 10.84],
    [7.0, 4.82],
    [5.0, 5.68],
]
data.sort(key=lambda x: x[0])
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]
scatter = (
    Scatter(init_opts=opts.InitOpts(theme = 'dark'))
    .add_xaxis(x_data)
    .add_yaxis("散点图",y_data)
)
scatter.render("这是一个散点图.html")
os.system("这是一个散点图.html")