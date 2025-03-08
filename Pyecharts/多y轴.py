# Author: 邵世昌
# CreatTime: 2024/11/15
# FileName: 多y轴
import os

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

# x 轴数据
x_data = ["{}月".format(i) for i in range(1, 13)]
# ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']


# 条形图
bar = (
    Bar()
    .add_xaxis(x_data)

    # y1
    .add_yaxis(
        "蒸发量",  # 系列名称
        [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],  # 系列数据项
        # 添加第一个轴，索引为0,（默认也是0）
        yaxis_index=0,

        color="#d14a61",  # 系列 label 颜色
    )

    # y2
    .add_yaxis(
        "降水量",  # 系列名称
        [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],  # 系列数据项
        # 添加第二个轴，索引设为1
        yaxis_index=1,
        color="#5793f3",  # 系列 label 颜色
    )

    # 对 y1 轴进行更加细致的配置
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="蒸发量",  # 坐标轴名称
            type_="value",  # 坐标轴类型  'value': 数值轴，适用于连续数据。
            min_=0,  # 坐标轴刻度最小值
            max_=250,  # 坐标轴刻度最大值
            position="right",  # 轴的位置  右侧
            # 轴线配置
            axisline_opts=opts.AxisLineOpts(
                # 轴线颜色
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            # 轴标签显示格式
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        )
    )

    # 提前配置 折线图 的 y 轴
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="温度",
            min_=0,
            max_=25,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            # 分割线配置
            splitline_opts=opts.SplitLineOpts(
                # 显示分割线
                is_show=True,
                # 线样式配置 opacity 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
                linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )

    .set_global_opts(
        # 对 y2 轴进行更加细致的配置
        yaxis_opts=opts.AxisOpts(
            name="降水量",
            min_=0,
            max_=250,
            position="right",
            offset=80,  # Y 轴相对于默认位置的偏移，在相同的 position 上有多个 Y 轴的时候有用。
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        title_opts=opts.TitleOpts(title="Grid-多 Y 轴示例"),
        # 提示框配置
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
)

# 折线图
line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis(
        "平均温度",
        [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        # 折线图对应的y轴索引为2
        yaxis_index=2,
        color="#675bba",
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line)  # 使用overlap(重叠)组件，把折线图重叠在条形图中

# 并行多图
grid = Grid()
grid.add(
    bar,  # 图表实例，仅 `Chart` 类或者其子类
    # 直角坐标系网格配置项
    opts.GridOpts(
        # grid 组件离容器距离
        pos_left="5%",
        pos_right="20%"),
    # 是否由自己控制 Axis 索引
    is_control_axis_index=True
)
grid.render("多y轴.html")
os.system("多y轴.html")
#%%
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

bar = (
    Bar()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "蒸发量",
        [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
        yaxis_index=0,
        color="#d14a61",
    )
    .add_yaxis(
        "降水量",
        [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
        yaxis_index=1,
        color="#5793f3",
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="蒸发量",
            type_="value",
            min_=0,
            max_=250,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="温度",
            min_=0,
            max_=25,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="降水量",
            min_=0,
            max_=250,
            position="right",
            offset=80,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        title_opts=opts.TitleOpts(title="Grid-Overlap-多 X/Y 轴示例"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="25%"),
    )
)

line = (
    Line()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "平均温度",
        [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        yaxis_index=2,
        color="#675bba",
        label_opts=opts.LabelOpts(is_show=False),
    )
)

# 上面的代码和上个例子  都是差不多的
bar1 = (
    Bar()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "蒸发量 1",
        [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
        color="#d14a61",
        xaxis_index=1,
        # y轴索引，继上面的 设为3
        yaxis_index=3,
    )
    .add_yaxis(
        "降水量 2",
        [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
        color="#5793f3",
        xaxis_index=1,
        yaxis_index=3,
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="蒸发量",
            type_="value",
            min_=0,
            max_=250,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="温度",
            min_=0,
            max_=25,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(grid_index=1),
        yaxis_opts=opts.AxisOpts(
            name="降水量",
            min_=0,
            max_=250,
            position="right",
            offset=80,
            # 直角坐标系网格索引
            grid_index=1,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="65%"),
    )
)

line1 = (
    Line()
    .add_xaxis(["{}月".format(i) for i in range(1, 13)])
    .add_yaxis(
        "平均温度 1",
        [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        color="#675bba",
        label_opts=opts.LabelOpts(is_show=False),
        # 新增了一个 x轴的索引，上面的line中x轴的索引为0
        xaxis_index=1,

        yaxis_index=5,
    )
)

overlap_1 = bar.overlap(line)
overlap_2 = bar1.overlap(line1)

# 使用grid将overlap_1和overlap_2进行水平并行放置
grid = (
    # 初始化
    Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add(
        overlap_1, grid_opts=opts.GridOpts(pos_right="58%"),
        # 是否由自己控制 Axis 索引
        is_control_axis_index=True
    )
    .add(overlap_2, grid_opts=opts.GridOpts(pos_left="58%"), is_control_axis_index=True)
    .render("多xy轴.html")
)
os.system("多xy轴.html")
