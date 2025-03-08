# Author: 邵世昌
# CreatTime: 2024/11/12
# FileName: 全局配置设置
#%%导入库
import os
from pyecharts import options as opts
from pyecharts.charts import Bar, Geo, Line
from pyecharts.faker import Faker#产生随机数据
from pyecharts.globals import RenderType#设置渲染风格

#%%主函数（链式调用）
bar = (
    Bar(#初始项设置
        init_opts=opts.InitOpts(theme = "write",#主题颜色
             #画布大小
            width="700px",height="400px",
            #渲染风格Canvas,svg
            renderer=RenderType.CANVAS,
            # bg_color="dark"#背景颜色优先级大于theme
        )
    )
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A",Faker.values())
    .add_yaxis("商家B",Faker.values())
    .add_yaxis("商家C",Faker.values())
    #全局配置项
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title = "柱形图",
            # title_link="",#跳转链接
            subtitle = "副标题",
            # subtitle_link="",#跳转链接
            pos_left="left",#显示位置
            pos_top= "0px",
            padding=5,  # 内边距
            item_gap=5,  # 主标题和副标题之间的距离
        ),
        #区域配置项，滑动组件
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,#是否显示组件
            type_="slider",#组件的类型：slider,inside
            is_realtime=True,#是否实时更新图像
            range_start=20,#组件开始百分比
            range_end=60,#组件结束百分比
            orient="horizontal",#horizontal或者vertical
            is_zoom_lock=False#是否缩放
        ),
        #图例配置项
        legend_opts=opts.LegendOpts(
            #图例类型，是否可以滚动plain或者scroll
            type_="plain",#默认
            is_show=True,#是否显示图例
            pos_left="center",#位置
            orient="horizontal",#位置
            #设置图例是否点击
            # True:开启图例点击
            # False:关闭图例点击
            # single:单选
            # multiple:多选
            selected_mode="multiple",
            align="auto",#图标和文字的对齐位置，auto,left
            padding=5,  # 内边距
            item_gap=5,  # 图例之间的距离
            item_width=30,# 图例的宽
            item_height=15,# 图例的高
            inactive_color="#ccc",#图例关闭时的颜色
            #pyecharts常见的图标：circle,rect,roundRect,triangle,diamond,arrow
            legend_icon="roundRect"
        ),
        #视觉映射
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            type_="color",#size或者color
            min_ = 0, #最小值
            max_= 150, #最大值
            range_opacity=1,#全局透明度
            range_text=["max","min"],#两端的文本
            range_color=["green","orange","red"],#设置颜色
            orient="horizontal",#horizontal或者vertical
            pos_top="8%",
            pos_left="15%",
            is_piecewise= True,#是否分段
            is_inverse=True#是否翻转
        ),
        #提示框配置项,鼠标提示框
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            #触发类型
            # item：一般用于散点图，柱形图，饼图
            # axis：提示坐标轴，一般与折线图，条形图，
            trigger="item",
            #触发条件
            #mousemove，click，mousemove|click
            trigger_on="mousemove|click",
            is_show_content=True,#是否显示提示框内容
            #标签内容
            #字符串中的模板变量
            #{a}：系列名series_name
            #{b}：数据名
            #{c}：值
            formatter = "{a}：{b}-{c}",
            background_color="white",#背景颜色
            border_color="black",#边框的颜色
            border_width=1,#边框的厚度
        ),
        #坐标轴
        xaxis_opts=opts.AxisOpts(
            is_show=True,#是否显示x轴
            #坐标轴类型
            #value:：数值
            #category：类目，离散值
            #time：时间轴，时间序列数据
            type_= "category"
        ),
        yaxis_opts=opts.AxisOpts(
            is_show=True,
            type_= "value",
            #不显示y轴的线
            axisline_opts=opts.AxisLineOpts(is_show=False),
            #不显示刻度
            axistick_opts=opts.AxisTickOpts(is_show=False)
        )
    )
)
bar.render("case1.html")
os.system("case1.html")

#%%折线图
line = (
    Line(#初始项设置
        init_opts=opts.InitOpts(theme = "write",#主题颜色
             #画布大小
            width="700px",height="400px",
            #渲染风格Canvas,svg
            renderer=RenderType.CANVAS,
            # bg_color="dark"#背景颜色优先级大于theme
        )
    )
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A",Faker.values(),itemstyle_opts=opts.ItemStyleOpts(color="orange"))
    .add_yaxis("商家B",Faker.values(),itemstyle_opts=opts.ItemStyleOpts(color="purple"))
    .add_yaxis("商家C",Faker.values(),itemstyle_opts=opts.ItemStyleOpts(color="green"))
    #全局配置
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title = "折线图"
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis"
        )
    )
    .set_series_opts(
        itemstyle_opts=opts.ItemStyleOpts(
            #图的颜色
            # color="red",
            opacity=0.6,#透明度
            # border_color="red",#边框颜色
            border_width=20,#边框宽度
        ),
        #线条
        linestyle_opts=opts.LineStyleOpts(
            is_show=True,
            width=2,#线条宽度
            # color="green",
            type_="dashed",#solid,dashed,dotted线条样式
        ),
        #标签配置项
        label_opts=opts.LabelOpts(
            is_show=True,
            font_family="Arial",#字体
            font_size=12,#字体大小
            font_style="normal",#是否斜体，italic
            font_weight="bold",#是否加粗
            position="outside",#位置top,left,right,bottom,inside,outside
            color="orange",#颜色
            rotate=45 #旋转角度
        ),
        #标记点
        markpoint_opts=opts.MarkPointOpts(
            data=[#特殊标记值,min,max,mean
                opts.MarkPointItem(
                    type_="max",
                    symbol="pin",#标记的图形
                    symbol_size=50#标记点的大小
                ),
                opts.MarkPointItem(
                    type_="min",
                    symbol="pin",
                    symbol_size=50,
                    # itemstyle_opts=opts.ItemStyleOpts(color="blue")
                )
            ]
        ),
        #标记线
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average",
                                  name="平均线")
            ],
            label_opts=opts.LabelOpts(color="red")
        )
    )
)
line.render("case2.html")
os.system("case2.html")