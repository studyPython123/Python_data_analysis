# Author: 邵世昌
# CreatTime: 2024/12/16
# FileName: data_analysis
#%%导入库
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
import warnings
warnings.filterwarnings('ignore')
from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Pie,Map
import  os

#%%导入数据
data_all = pd.read_csv('全部整合信息.csv',encoding='utf-8')
login_data = pd.read_csv('login_dealed.csv',encoding='utf-8')
stu_info = pd.read_csv('study_information_dealed.csv',encoding='utf-8')

#'''-----------------------------------------------------------海外用户分析-----------------------------------------------------------------------------'''
#%%海外用户数量分析
country = pd.DataFrame(list(set(data_all['国家'])),columns=['国家']).dropna(axis=0)
print(data_all['国家'].isnull().sum()) # 空值数量
country_user_counts = data_all.groupby('国家')['user_id'].count().sort_values(ascending=False)
country_user_counts.columns = '用户数量'
country_user_counts_external= country_user_counts.drop('中国',axis=0)
pie_user_external = (
    Pie(init_opts=opts.InitOpts(theme='withe',width='1000px',height='600px'))
    .add('饼图',[list(i) for i in zip(country_user_counts_external.index.tolist(),country_user_counts_external.values.tolist())],
         label_opts=opts.LabelOpts(is_show=True,
            position="outside", formatter="{b}-{c}({d}%)"
             )
         )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True, title="海外用户占比分析", pos_left="center"
        ),
        legend_opts=opts.LegendOpts(
            pos_top="4%"
        )
    )
)
pie_user_external.render("海外用户占比分析.html")
os.system("海外用户占比分析.html")

#'''-----------------------------------------------------------海外用户登入量分析-----------------------------------------------------------------------------'''
#%%海外用户登入量分析
country_login_counts = login_data.groupby('国家')['user_id'].count().sort_values(ascending=False)
country_login_counts.columns = '用户登入量'
country_login_counts_external = country_login_counts.drop('中国',axis=0)
pie_external_login = (
    Pie(init_opts=opts.InitOpts(theme='withe',width='1200px',height='600px'))
    .add('饼图',[list(i) for i in zip(country_login_counts_external.index.tolist(),country_login_counts_external.tolist())],
         label_opts=opts.LabelOpts(
             is_show=True, position="outside", formatter="{b}-{c}({d}%)"
            )
         )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True, title="海外登入量占比分析", pos_left= 'center'
        ),
        legend_opts=opts.LegendOpts(
            pos_top="4%"
        )
    )
)
pie_external_login.render("海外登入量占比分析.html")
os.system("海外登入量占比分析.html")

#'''------------------------------------------------国内各省份用户数量分析---------------------------------------------------------------------'''
#%%国内各省份用户数量分析
province_user_counts_internal = data_all[data_all['国家'] == '中国'].groupby('省份')['user_id'].count().sort_values(ascending=True)
bar_user_counts_internal  = (
    Bar(init_opts=opts.InitOpts(theme='withe',width='1200px',height='800px'))
    .add_xaxis(province_user_counts_internal.index.tolist())
    .add_yaxis('条形图',province_user_counts_internal.values.tolist(),
               label_opts=opts.LabelOpts(
                   is_show=True, position="outside", formatter="{c}"  # 设置数值标签
               ),
               itemstyle_opts=opts.ItemStyleOpts(color='skyblue'),
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(
                            type_="max", name="最大值",
                            itemstyle_opts=opts.ItemStyleOpts(color="red")
                        ),
                        opts.MarkPointItem(
                            type_="min", name="最小值",
                            itemstyle_opts=opts.ItemStyleOpts(color="green")
                        )
                    ]
                )
        )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True, title="国内各省份用户数量分析", pos_left= 'center'
        ),
        legend_opts=opts.LegendOpts(
            pos_top="4%"
        )
    )
)
bar_user_counts_internal.render("国内各省份用户数量分析.html")
os.system('国内各省份用户数量分析.html')

#%%国内各省份用户数量分析地图
data_list = []
for province_data in zip(province_user_counts_internal.index.tolist(), province_user_counts_internal.values.tolist()):
    print(province_data)
    province_name = province_data[0]
    province_confirm = province_data[1]
    # 处理省份不匹配问题
    if province_name == "新疆":
        province_name = "新疆维吾尔自治区"
    elif province_name == "广西":
        province_name = "广西壮族自治区"
    elif province_name == "宁夏":
        province_name = "宁夏回族自治区"
    elif province_name in ["内蒙古", "西藏"]:
        province_name = province_name + "自治区"
    elif province_name in ["北京", "天津", "重庆", "上海"]:
        province_name = province_name + "市"
    elif province_name in ["香港", "澳门"]:
        province_name = province_name + "特别行政区"
    elif province_name == '黑龙':
        province_name = province_name + "江省"
    else:
        province_name = province_name + "省"
    data_list.append((province_name, province_confirm))
# %%绘图
map_user_counts_internal =(
    Map(init_opts=opts.InitOpts(theme='withe',width='800px',height='600px'))
    .add('地图',data_list,"china",label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="国内各省份用户数量分析地图",pos_left= 'center'),
        visualmap_opts=opts.VisualMapOpts(max_=max(province_user_counts_internal.values.tolist())),
        legend_opts=opts.LegendOpts(
            pos_top="4%"
        )
    )
)
map_user_counts_internal.render("国内各省份用户数量分析地图.html")
os.system('国内各省份用户数量分析地图.html')

# %%绘图(去除广东)
map_user_counts_internal =(
    Map(init_opts=opts.InitOpts(theme='withe',width='800px',height='600px'))
    .add('地图',data_list[:-1],"china",label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="国内各省份用户数量分析地图（广东除外）",pos_left= 'center'),
        visualmap_opts=opts.VisualMapOpts(max_=max(province_user_counts_internal.values.tolist()[:-1])),
        legend_opts=opts.LegendOpts(
            pos_top="4%"
        )
    )
)
map_user_counts_internal.render("国内各省份用户数量分析地图（广东除外）.html")
os.system('国内各省份用户数量分析地图（广东除外）.html')

#'''------------------------------------------------国内各省份登入量分析-------------------------------------------------------------------------'''
#%%国内各省份登入量分析
province_login_counts_internal = login_data[login_data['国家'] == '中国'].groupby('省份')['user_id'].count().sort_values(ascending=True)
bar_login_counts_internal  = (
    Bar(init_opts=opts.InitOpts(theme='withe',width='1200px',height='400px'))
    .add_xaxis(province_login_counts_internal.index.tolist())
    .add_yaxis('国内各省份登入量分析',province_login_counts_internal.values.tolist(),
               label_opts=opts.LabelOpts(
                   is_show=True, position="outside", formatter="{c}"
               ),
               itemstyle_opts=opts.ItemStyleOpts(color='purple')
        )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True, title="国内各省份登入量分析", pos_left= 'center'
        ),
        datazoom_opts=opts.DataZoomOpts( # 区域配置项，滑动组件
            is_show=True, type_="slider", is_realtime=True, range_start=20,
            range_end=60, orient="horizontal", is_zoom_lock=False
        ),
        legend_opts=opts.LegendOpts(
            pos_top="8%"
        )
    )
    .set_series_opts(# 标记点
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(
                    type_="max", symbol="pin", symbol_size=80,
                    itemstyle_opts=opts.ItemStyleOpts(color="red")
                ),
                opts.MarkPointItem(
                    type_="min", symbol="pin", symbol_size=50,
                    itemstyle_opts=opts.ItemStyleOpts(color="green")
                )
            ]
        ),
        markline_opts=opts.MarkLineOpts(# 标记线
            data=[
                opts.MarkLineItem(type_="average",name="平均线")
            ],
            label_opts=opts.LabelOpts(color="red")
        )
    )
)
bar_login_counts_internal.render("国内各省份登入数量分析.html")
os.system('国内各省份登入数量分析.html')

#%%国内各省份登入数量分析地图
province_login_counts_internal = login_data[login_data['国家'] == '中国'].groupby('省份')['user_id'].count().sort_values(ascending=True)
data_list = []
for province_data in zip(province_login_counts_internal.index.tolist(), province_login_counts_internal.values.tolist()):
    print(province_data)
    province_name = province_data[0]
    province_confirm = province_data[1]
    if province_name == "新疆":
        province_name = "新疆维吾尔自治区"
    elif province_name == "广西":
        province_name = "广西壮族自治区"
    elif province_name == "宁夏":
        province_name = "宁夏回族自治区"
    elif province_name in ["内蒙古", "西藏"]:
        province_name = province_name + "自治区"
    elif province_name in ["北京", "天津", "重庆", "上海"]:
        province_name = province_name + "市"
    elif province_name in ["香港", "澳门"]:
        province_name = province_name + "特别行政区"
    elif province_name == '黑龙':
        province_name = province_name + "江省"
    else:
        province_name = province_name + "省"
    data_list.append((province_name, province_confirm))
map_login_counts_internal =(
    Map(init_opts=opts.InitOpts(theme='withe',width='1000px',height='800px'))
    .add('地图',data_list,"china",label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="国内各省份登入数量分析地图",pos_left='center'),
        visualmap_opts=opts.VisualMapOpts(max_=max(province_login_counts_internal.values.tolist())),
        legend_opts=opts.LegendOpts(
            pos_top="8%"
        )
    )
)
map_login_counts_internal.render("国内各省份登入数量分析地图.html")
os.system('国内各省份登入数量分析地图.html')
#%%
map_login_counts_internal =(
    Map(init_opts=opts.InitOpts(theme='withe',width='1000px',height='800px'))
    .add('地图',data_list[:-1],"china",label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="国内各省份登入数量分析地图（广东除外）",pos_left='center'),
        visualmap_opts=opts.VisualMapOpts(max_=max(province_login_counts_internal.values.tolist()[:-1])),
        legend_opts=opts.LegendOpts(
            pos_top="8%"
        )
    )
)
map_login_counts_internal.render("国内各省份登入数量分析地图（广东除外）.html")
os.system('国内各省份登入数量分析地图（广东除外）.html')

#-----------------------------------------------用户分布行为差异------------------------------------------------------------
#%%用户分布行为差异
dict_ = {'learn_time':['sum','mean','count'],'number_of_classes_now':['sum','mean'],'course_count':['mean']}
province_user_distribution_describe = data_all.groupby(['省份']).agg(dict_)
province_user_distribution_describe.to_csv('用户分布行为差异描述.csv',encoding='utf_8_sig')
#-----------------------------------------------------活跃度分析-----------------------------------------------------------------
# %%用户活跃度分析
user_login_counts = login_data.groupby('user_id')['login_time'].count().sort_values(ascending=False) # 用户的登入次数
user_learn_times = data_all.groupby('user_id')['learn_time'].sum().sort_values(ascending=False) # 用户总学习时长
user_learn_times_average = (user_learn_times/user_login_counts).sort_values(ascending=False) # 用户的平均每次登入的学习时长
user_learn_times_isnull = user_learn_times_average[user_learn_times_average.isnull()] #获取学习时长为空的用户
min_date = login_data.login_time.min()
max_date = login_data.login_time.max()
line_login_counts_groupby_users = (
    Line(init_opts=opts.InitOpts(theme='withe', width='1200px', height='400px'))
    .add_xaxis(user_login_counts.index.tolist())
    .add_yaxis('折线图', user_login_counts.values.tolist(), itemstyle_opts=opts.ItemStyleOpts(color='purple'))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True,
            title="用户活跃度分析（按用户分析）",
            pos_left= 'center'
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True, type_="slider", is_realtime=True,
            range_start=20, range_end=60, orient="horizontal", is_zoom_lock=False
        ),
        legend_opts=opts.LegendOpts(
            pos_top="8%"
        )
    )
)
line_login_counts_groupby_users.render('用户活跃度分析（按用户分析）.html')
os.system('用户活跃度分析（按用户分析）.html')

#%%按时间分析
login_counts_groupby_time = login_data.groupby('login_time')['user_id'].count().sort_index(ascending=True)
line_login_counts_groupby_time = (
    Line(init_opts=opts.InitOpts(theme='withe',width='1200px',height='400px'))
    .add_xaxis(login_counts_groupby_time.index.tolist())
    .add_yaxis('折线图',login_counts_groupby_time.values.tolist(),itemstyle_opts=opts.ItemStyleOpts(color='purple'))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True,
            title="用户活跃度分析（按时间分析）",
            pos_left= 'center'
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,  type_="slider",  is_realtime=True,
            range_start=20, range_end=60,orient="horizontal", is_zoom_lock  = False
        ),
        legend_opts=opts.LegendOpts(
            pos_top="8%"
        )
    )
)
line_login_counts_groupby_time.render('用户活跃度分析（按时间分析）.html')
os.system('用户活跃度分析（按时间分析）.html')

#%%添加工作日字段
login_data['login_time'] = pd.to_datetime(login_data['login_time'],format='%Y-%m-%d')
for index in login_data['login_time'].index:
    date = login_data.loc[index,'login_time']
    if date.weekday() < 5:
        login_data.loc[index,'是否工作日'] = '是'
    else:
        login_data.loc[index, '是否工作日'] = '否'
#统计工作日和休息日的登入次数
workday_login_counts = login_data[login_data['是否工作日'] == '是'].shape[0] #工作日登入次数
day_off_login_counts = login_data[login_data['是否工作日'] == '否'].shape[0] # 休息日登入次数
login_data.groupby(['是否工作日','user_id']).user_id.count().head()
workday_user_login =  login_data[login_data['是否工作日'] == '是'].groupby('user_id').是否工作日.count()
day_off_user_login =  login_data[login_data['是否工作日'] == '否'].groupby('user_id').是否工作日.count()
user_login = pd.merge(workday_user_login,day_off_user_login,on= 'user_id',how = 'outer' ).fillna(0)
user_login.columns = ['是','否']

#%%用户流失分析
province_user_lost = data_all.groupby(['省份','logged_now_gap_time']).user_id.count().unstack()
data_all['流失时间划分'] = [i.split(',')[0].rstrip(' days') for i in data_all['logged_now_gap_time']]
data_all['流失时间划分'].replace('0:00:00',0,inplace=True) # 数据转换
for i in range(data_all.shape[0]):
    if int(data_all.loc[i,'流失时间划分']) > 150:
        data_all.loc[i,'流失时间划分']='大于150天'
    elif 90 <=int(data_all.loc[i,'流失时间划分'])  < 150:
        data_all.loc[i,'流失时间划分']='90-150天'
    elif 30 <=int(data_all.loc[i,'流失时间划分'])  < 90:
        data_all.loc[i,'流失时间划分']='30-90天'
    elif 15 <= int(data_all.loc[i,'流失时间划分']) < 30:
        data_all.loc[i,'流失时间划分']='15-30天'
    elif 7 <= int(data_all.loc[i,'流失时间划分']) < 15:
        data_all.loc[i,'流失时间划分']='7-15天'
    elif 0 <= int(data_all.loc[i,'流失时间划分']) < 7:
        data_all.loc[i,'流失时间划分']='7天内'
province_user_lost_days = data_all.groupby(['省份','流失时间划分']).user_id.count().unstack()
province_user_lost_days.to_csv('省份用户流失数量按时间划分.csv',encoding='utf_8_sig')

#%%课程选课人数
bar1=(
    Bar(init_opts=opts.InitOpts(theme='white'))
    .add_xaxis(stu_info.course_id.value_counts().index.tolist()[:30])
    .add_yaxis('柱状图',stu_info.course_id.value_counts().values.tolist()[:30],itemstyle_opts=opts.ItemStyleOpts(color='purple'))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True, title="课程选课人数", pos_left= 'center'
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True, type_="slider", is_realtime=True,
            range_start=20,  range_end=60,  orient="horizontal",  is_zoom_lock=False
        ),
        legend_opts=opts.LegendOpts(
            pos_top="5%"
        )
    )
)
bar1.render('课程选课人数.html')
os.system('课程选课人数.html')

#%%最受欢迎免费课程
bar2=(
    Bar(init_opts=opts.InitOpts(theme='white'))
    .add_xaxis(stu_info[stu_info['price']==0].course_id.value_counts().index.tolist()[:30])
    .add_yaxis('柱状图',stu_info[stu_info['price']==0].course_id.value_counts().values.tolist()[:30],itemstyle_opts=opts.ItemStyleOpts(color='purple'))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True, title="最受欢迎免费课程", pos_left= 'center'
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True, type_="slider",  is_realtime=True,   range_start=20,
            range_end=60,   orient="horizontal",  is_zoom_lock=False
        ),
        legend_opts=opts.LegendOpts(
            pos_top="5%"
        )
    )
)
bar2.render('最受欢迎免费课程.html')
os.system('最受欢迎免费课程.html')

#%%最受欢迎收费课程
bar3=(
    Bar(init_opts=opts.InitOpts(theme='white'))
    .add_xaxis(stu_info[stu_info['price']!=0].course_id.value_counts().index.tolist()[:30])
    .add_yaxis('柱状图',stu_info[stu_info['price']!=0].course_id.value_counts().values.tolist()[:30],itemstyle_opts=opts.ItemStyleOpts(color='purple'))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            is_show=True,  title="最受欢迎收费课程", pos_left= 'center'
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,   type_="slider", is_realtime=True,
            range_start=20,  range_end=60,    orient="horizontal", is_zoom_lock=False
        ),
        legend_opts=opts.LegendOpts(
            pos_top="5%"
        )
    )
)
bar3.render('最受欢迎收费课程.html')
os.system('最受欢迎收费课程.html')

#%% 可以看出课程的价格为109时候，用户学习时间和数量都相对较优，但是随着价格的上升，用户学习时间突然下降
stu_info.groupby(['price']).agg({'learn_process':['sum','mean'],'user_id':['count']})
stu_info[stu_info['price']==129].groupby(['course_id']).agg({'learn_process':['mean','count']}) #课程129
stu_info[stu_info['price']==109].groupby(['course_id']).agg({'learn_process':['mean','count']}) #课程109
stu_info[stu_info['price']==299].groupby(['course_id']).agg({'learn_process':['mean','count']}) #课程299
stu_info[stu_info['price']==369].groupby(['course_id']).agg({'learn_process':['mean','count']}) #课程369
stu_info_course=pd.DataFrame(stu_info.groupby(['course_id']).agg({'learn_process':['mean'],'price':['mean']}))
data_all.to_csv('data_user_all.csv',encoding='utf_8_sig')