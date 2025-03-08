# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: case3(待测试)
from pyecharts import options as opts
from pyecharts.faker import Faker#生成随机数
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
import os

bar = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(Faker.choose())
    # .add_yaxis("商家A", Faker.values(), itemstyle_opts=opts.ItemStyleOpts(color="green"))
    # .add_yaxis("商家B", Faker.values(), itemstyle_opts=opts.ItemStyleOpts(color="orange"))
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        # LegendOpts：图例配置项
        legend_opts=opts.LegendOpts(
            # 是否显示图例组件
            is_show=True,
            # 图例的类型。可选值：
            # 'plain'：普通图例。缺省就是普通图例。
            # 'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。
            type_='plain',
            # 图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。默认开启图例选择，可以设成 false 关闭
            # 除此之外也可以设成 'single' 或者 'multiple' 使用单选或者多选模式。
            # selected_mode = False,
            selected_mode=True,
            # selected_mode = 'multiple',
            # 图例组件离容器左侧的距离。
            # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
            # 也可以是 'left', 'center', 'right'。
            # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
            # pos_left = 50,
            pos_left='center',
            # pos_left = 'left',
            # 图例组件离容器右侧的距离（同上）。
            # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
            pos_right=None,
            # 图例组件离容器上侧的距离（同上）。
            # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
            # 也可以是 'top', 'middle', 'bottom'。
            # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
            pos_top=None,
            # 图例组件离容器下侧的距离（同上）。
            # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
            pos_bottom=None,
            # 图例列表的布局朝向。可选：'horizontal', 'vertical'
            orient='horizontal',
            # 图例标记和文本的对齐。默认自动（auto）
            # 根据组件的位置和 orient 决定
            # 当组件的 left 值为 'right' 以及纵向布局（orient 为 'vertical'）的时候为右对齐，即为 'right'。
            # 可选参数: `auto`, `left`, `right`
            align=None,
            # 图例内边距，单位px，默认各方向内边距为5
            padding=5,
            # 图例每项之间的间隔。横向布局时为水平间隔，纵向布局时为纵向间隔。
            # 默认间隔为 10
            item_gap=20,
            # 图例标记的图形宽度。默认宽度为 25
            item_width=50,
            # 图例标记的图形高度。默认高度为 14
            item_height=14,
            # 图例关闭时的颜色。默认是 #ccc
            inactive_color='#E6E61A',
            # 图例组件字体样式，参考 `series_options.TextStyleOpts`
            textstyle_opts=None,
            # 图例项的 icon。
            # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
            # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。
            # 可以通过 'path://' 将图标设置为任意的矢量路径。
            legend_icon='pin',
        )
    )
)
bar.render("pyecharts图例属性设置.html")
os.system("pyecharts图例属性设置.html")
