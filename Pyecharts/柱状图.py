# Author: 邵世昌
# CreatTime: 2024/11/12
# FileName: 柱状图
import os
from pyecharts.charts import Bar
import pyecharts.options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
#%%
bar = (
    Bar(
        init_opts=opts.InitOpts(
            width="1400px", height="1000px",
            bg_color={#指定背景
                'image':JsCode('img'),
                "repeat":"no-repeat"
            }
            # animation_opts=opts.AnimationOpts(
            #     animation_delay=1000,#动画延时1秒钟
            #     animation_easing="elasticOut"#具有弹性的动画
            # )
        )
    )
    .add_xaxis(Faker.cars)
    .add_yaxis("汽车", Faker.values(),
           label_opts=opts.LabelOpts(
               is_show=True,position="outside",
               formatter="{c}"
           ),
            itemstyle_opts=opts.ItemStyleOpts(
                color="green"
            )
    )
    .add_yaxis("汽车", Faker.values(),
               label_opts=opts.LabelOpts(
                   is_show=True, position="outside",
                   formatter="{c}"
               ),
               itemstyle_opts=opts.ItemStyleOpts(
                   color="purple"
               )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="柱状图",
            subtitle="副标题"
        ),
        xaxis_opts=opts.AxisOpts(name="汽车"),
        yaxis_opts=opts.AxisOpts(name="销量")
    )
)
#%%导入js代码
bar.add_js_funcs(
    """
    var img = new Image();
    img.src = 'https://user-images.githubusercontent.com/19553554/71825144-2d568180-30d6-11ea-8ee0-63c849cfd934.png'
    """
)
bar.render("柱状图.html")
os.system("柱状图.html")