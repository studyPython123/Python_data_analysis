# Author: 邵世昌
# CreateTime: 2024/12/14
# FileName: infant_consume_data_analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import random
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['KaiTi']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%导入并检查数据
baby_info = pd.read_csv("(sample)sam_tianchi_mum_baby.csv",encoding='utf-8')
trade_data = pd.read_csv("(sample)sam_tianchi_mum_baby_trade_history.csv",encoding='utf-8') # 转换为时间数据
pd.set_option('display.max_rows', None) # 取消对显示行数的限制
pd.set_option('display.max_columns', None) # 取消对显示列数的限制
pd.set_option('display.width', None) # 取消对列宽度的限制
pd.set_option('display.float_format', '{:.2f}'.format)  # 设置浮点数输出格式
print(baby_info.head())
print(trade_data.head())
print(baby_info.info())
print(trade_data.info())
print(baby_info.duplicated().sum())
print(trade_data.duplicated().sum())


#%% 提取数据特征
print("商 品 类 目 数：", trade_data.cat1.nunique())
print("商 品 类 别 数：", trade_data.cat_id.nunique())
print("商    品    数：", trade_data.auction_id.nunique())
print("总    销    量：", trade_data.buy_mount.sum())
print("用    户    数：", trade_data.user_id.nunique())
print(f"人 均 购 买 量： {trade_data.buy_mount.sum()/trade_data.user_id.nunique():.2f}")

#%% 将时间数据转换为时间格式
baby_info['datetime'] = pd.to_datetime(baby_info['birthday'],format='%Y%m%d')
trade_data['datetime'] = pd.to_datetime(trade_data['day'],format='%Y%m%d')
trade_data.drop(['property','day'], axis=1, inplace=True)
print(trade_data.datetime.describe())
# 2012-07-02->2015-02-05
#%%数据重采样
baby_count = baby_info.resample('M', on='datetime')['user_id'].count() # 按月分组并计算总销售额
trade_month_sale = trade_data.resample('M', on='datetime')['buy_mount'].sum() #按照月分组的销售额度
trade_quarter_sale = trade_data[['auction_id', 'buy_mount', 'datetime']].groupby(by=[trade_data.datetime.dt.year,
                                                                             trade_data.datetime.dt.quarter])[ 'buy_mount'].sum() #按照季度分组的销售额度
trade_year_sale = trade_data.resample('Y', on='datetime')['buy_mount'].sum() #按照年分组的销售额度
#%%年度销量趋势分析
plt.figure(figsize=(7,5))
x_ticks = trade_year_sale.index.tolist()
x_ticks = [x_ticks[i].strftime('%Y') for i in range(len(x_ticks))]
x = np.arange(len(x_ticks))
y = trade_year_sale.values.tolist()
colors = []
for _ in range(len(y)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,y,color = colors)
plt.bar_label(bar, label_type='edge')
plt.xticks(x,x_ticks)
plt.title('年度销量趋势',fontsize=20)
plt.xlabel('年份',fontsize=12)
plt.ylabel('销量',fontsize=12)
plt.show()
'''
2017/7-2015/2期间总销量是49973件，
从图种可知淘宝和天猫平台母婴商品市场销量整体呈现上升趋势，但是波动较大。
'''
#%%季度销量趋势
plt.figure(figsize=(10, 5))
x_ticks = trade_quarter_sale.index.tolist()
x = np.arange(len(x_ticks))
y = trade_quarter_sale.values.tolist()
colors = []
for _ in range(len(y)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,y,color = colors)
plt.bar_label(bar,label_type = 'edge')
plt.xticks(x,x_ticks)
plt.title("季度销量趋势")
plt.xlabel("(年,季度)")
plt.ylabel("销量")
plt.show()
'''
2015年存在数据缺失，不能真实反应2015年第一季度的销量情况
每年的销售情况整体呈现上升趋势，在第四季度达到最大，而次年的第一季度会有较大幅度的降低。
'''
#%% 月度销量趋势
plt.figure(figsize=(12,7))
x_ticks = trade_month_sale.index.tolist()
x_ticks = [x_ticks[i].strftime('%Y-%m') for i in range(len(x_ticks))]
x = np.arange(len(x_ticks))
y = trade_month_sale.values.tolist()
colors = []
for _ in range(len(y)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,y,color = colors)
plt.bar_label(bar, label_type='edge')
plt.xticks(x,x_ticks,rotation = 45)
plt.title('月度销量趋势',fontsize=20)
plt.xlabel('月份',fontsize=12)
plt.ylabel('销量',fontsize=12)
plt.show()
'''
1、2月的销量很低。
每年的5至7月、11和12月都会出现不同程度的销量上涨，主要集中在假期前夕。
'''
#%% 年份销量对比
grouped = trade_month_sale.groupby(pd.Grouper(freq='A')) # 按照索引的年份分组
trade_year_month_sale = pd.DataFrame()
for group in grouped:
    year = group[0].year
    group = group[1]
    group = pd.concat([group, pd.Series(group.index.month.tolist(), index=group.index)], axis=1)
    group.columns = [f'{year}', 'month']
    group = group.set_index('month', drop=True)
    trade_year_month_sale = pd.concat([trade_year_month_sale, group], ignore_index=False,axis=1)
trade_year_month_sale = trade_year_month_sale.sort_index(ascending=True)
trade_year_month_sale.plot()

#%%销售下降与销售提高的原因分析
year = int(input('请输入要分析的年份：'))
# months = [11,12]
months = [2,3]
for month in months:
    plt.subplot(2,1,month-1)
    trade_day_sale = trade_data[(trade_data['datetime'].dt.year == year) & (trade_data['datetime'].dt.month == month) ]
    trade_day_sale = trade_day_sale.resample('d', on='datetime')['buy_mount'].sum() #按照年分组的销售额度
    x_ticks = trade_day_sale.index.day.tolist()
    x = np.arange(len(x_ticks))
    y = trade_day_sale.values.tolist()
    colors = []
    for _ in range(len(y)):
        r = random.random()
        g = random.random()
        b = random.random()
        colors.append((r, g, b))
    bar = plt.bar(x,y,color = colors)
    plt.bar_label(bar, label_type='edge')
    plt.xticks(x,x_ticks)
    plt.title(f'{year}年{month}月每日销量',fontsize=20)
    plt.xlabel('日期',fontsize=12)
    plt.ylabel('销量',fontsize=12)
plt.tight_layout()
plt.show()

#%%不同年份各月份销售情况对比分析
months = int(input('请输入需要分析的时间段(上半年请输入6，下半年请输入12)：'))
for month in range(months-5,months+1):
    if month > 6:
        plt.subplot(3,2,month-6)
    else:
        plt.subplot(3, 2, month)
    trade_data_month_1 = trade_data[trade_data['datetime'].dt.month == month]
    trade_data_month_1 = trade_data_month_1.groupby('datetime')['buy_mount'].sum()
    trade_data_month_1.sort_index(inplace=True)
    trade_data_month_1_year = trade_data_month_1.resample('Y')
    for temp in trade_data_month_1_year:
        temp = temp[1]
        print(temp)
        plt.plot(range(1,len(temp.values.tolist())+1),temp.values.tolist(), label=f'{temp.index.year[0]}')
    plt.legend(loc='upper right')
    plt.title(f'{month}月份数据',fontsize=20)
    plt.xlabel('日期',fontsize=12)
    plt.ylabel('销量',fontsize=12)
    plt.tight_layout()
plt.show()

#%%不同大类不同年份的各月份销售情况对比分析
trade_data_type = trade_data.groupby(['cat1'])[['datetime','buy_mount']]
month = int(input('请输入需要分析的月份：'))
t = 1
for temp in trade_data_type:
    plt.subplot(3,2,t)
    print(temp[0][0])
    temp_df = temp[1]
    temp_df_year = temp_df.groupby('datetime')['buy_mount'].sum()
    temp_df_year_month_1 = temp_df_year[temp_df_year.index.month == month]
    temp_df_year_12_month_1 = temp_df_year_month_1[temp_df_year_month_1.index.year == 2012]
    temp_df_year_13_month_1 = temp_df_year_month_1[temp_df_year_month_1.index.year == 2013]
    temp_df_year_14_month_1 = temp_df_year_month_1[temp_df_year_month_1.index.year == 2014]
    temp_df_year_15_month_1 = temp_df_year_month_1[temp_df_year_month_1.index.year == 2015]
    x = range(1,32)
    plt.plot(temp_df_year_12_month_1.tolist(),label = '2012')
    plt.plot(temp_df_year_13_month_1.tolist(),label = '2013')
    plt.plot(temp_df_year_14_month_1.tolist(),label = '2014')
    plt.plot(temp_df_year_15_month_1.tolist(),label = '2015')
    plt.xticks(x, range(1, 32))
    plt.xlabel('月份',fontsize=12)
    plt.ylabel('销量',fontsize = 12)
    plt.title(f'{temp[0][0]}大类({month}月份)',fontsize=20)
    plt.legend(loc='upper right')
    plt.tight_layout()
    t += 1
plt.show()
'''
2013/2/1-2013/2/15处于销量谷底，2013年春节假期：2013/2/9-2013/2/15
2014/1/26-2014/2/4处于销售谷底，2014年春节假期：2014/1/31-2014/2/6
'''

#%%2013和2014年各大类销量情况对比分析
trade_data_year = trade_data.resample('y',on ='datetime')[['cat1','buy_mount']]
cat_df = pd.DataFrame()
for cat1 in trade_data_year:
    print(cat1[0].year)
    cat = cat1[1]
    cat_year = cat.groupby('cat1')['buy_mount'].sum()
    cat_df = pd.concat([cat_df,cat_year],axis = 1,ignore_index=False)
cat_df.columns = ['2012','2013','2014','2015']
fig,ax1 = plt.subplots()
xticks = cat_df.index.tolist()
bar_width = 0.35
bar_position1 = range(len(xticks))
bar_position2 = [i + bar_width for i in bar_position1]
p1 = ax1.bar(bar_position1,cat_df['2013'].tolist(),width=bar_width,color='blue',label='2013',alpha = 0.5)
ax1.bar_label(p1,label_type = 'edge')
p2 = ax1.bar(bar_position2,cat_df['2014'].tolist(),width=bar_width,color='orange',label='2014',alpha = 0.5)
ax1.bar_label(p2,label_type = 'edge')
ax1.set_ylabel('销售量',color='b')
ax1.tick_params('y', colors='b')
plt.xticks([p + bar_width / 2 for p in bar_position1], xticks)
ax2 = ax1.twinx()
line_y = [(cat_df['2014'].tolist()[i]/cat_df['2013'].tolist()[i]-1)*100 for i in bar_position1]
# 循环添加数值标签
ax2.plot(bar_position2,line_y,color='red',label = '同比增长率')
for i, j in zip(bar_position2, line_y):
    ax2.annotate(f'{str(round(j,2))}%', xy=(i, j), xytext=(0, -10), textcoords='offset points', ha='center',va='bottom')
ax2.set_ylabel('同比增长率', color='r')
ax2.tick_params('y', colors='r')
# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')
plt.title('2013-2014各大类的销售量以及2014年的同比增长率')
plt.show()

#%% 商品大类销售情况分析
plt.figure(figsize=(7,5))
cat = trade_data.groupby("cat1")['buy_mount'].sum()
x_ticks=cat.index.tolist()
x = np.arange(len(x_ticks))
y = cat.values.tolist()
colors = []
for _ in range(len(y)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,y,color = colors)
plt.bar_label(bar,label_type='edge')
plt.xticks(x,x_ticks)
plt.title("商品大类销售情况")
plt.xlabel("商品大类")
plt.ylabel('销售量')
plt.show()

#%% 人均大类购买量分析
plt.figure(figsize=(10,5))
cat_aver_user = (trade_data.groupby("cat1")['buy_mount'].sum() /
                 trade_data.groupby("cat1")['user_id'].count()).sort_values(ascending=False)
x_ticks=cat_aver_user.index.tolist()
x = np.arange(len(x_ticks))
y = cat_aver_user.values.tolist()
colors = []
for _ in range(len(y)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,y,color = colors)
plt.bar_label(bar,label_type='edge')
plt.xticks(x,x_ticks)
plt.title("商品大类人均购买情况")
plt.xlabel("商品大类")
plt.ylabel("人均购买量")
plt.show()

#%% 大类下子类别数量
plt.figure(figsize=(6,5))
cat_count = trade_data.groupby("cat1")['cat_id'].count()
x_ticks = cat_count.index.tolist()
x = np.arange(len(x_ticks))
y = cat_count.values.tolist()
colors = []
for _ in range(len(y)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,y,color = colors)
plt.bar_label(bar,label_type='edge')
plt.xticks(x,x_ticks)
plt.title("商品大类的子类数量")
plt.xlabel("商品大类")
plt.ylabel("数量")
plt.show()
'''
大类28和50008168销量最佳
大类38虽然销量低、子类数最少但是人均购买量却很高，说明用户在购买38大类下的产品时选择余地较少
但同时用户对此类产品的需求又很旺盛，可以适量的增加38大类下的子类产品，提高销售量
'''
#%% 复购率分析
repurchase_data_group = trade_data.groupby(['user_id','cat1'])['datetime'].count()
print(repurchase_data_group[repurchase_data_group.values != 1])
user_number = trade_data.user_id.nunique() # 总用户数
list = [3,2,10,1,0,0]
repurchase_rate = [i/user_number for i in list]
# 814316568用户4次购买28大类的产品
print(trade_data[trade_data.user_id == 814316568])
baby_info[baby_info.user_id == 814316568]
# %%
plt.figure(figsize=(6,5))
x_ticks =[28, 38, 50008168, 50014815, 50022520, 122650008]
x = np.arange(len(x_ticks))
colors = []
for _ in range(len(repurchase_rate)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,repurchase_rate,color = colors)
plt.bar_label(bar,label_type = 'edge')
plt.xticks(x,x_ticks)
plt.title('各大类的复购率')
plt.xlabel('大类')
plt.ylabel('复购率')
plt.show()

#%%用户的需求分析
'''
设购买量大于20为大量购买
购买量大于100为批量采购
购买量大于500为大批量采购
'''
trade_data_group_user = trade_data.groupby(['user_id'])['buy_mount'].sum()
user_buy_num_than_20 = trade_data_group_user[(trade_data_group_user .values >= 20)&(trade_data_group_user<100)] # 提取购买量达到20的购买记录
user_buy_num_than_100 = trade_data_group_user[(trade_data_group_user .values >= 100)&(trade_data_group_user<500)] # 提取购买量达到100的购买记录
user_buy_num_than_500 = trade_data_group_user[(trade_data_group_user .values >= 500)] # 提取购买量达到500的购买记录

#%%购买量大于500的用户购买情况
plt.figure(figsize=(10,5))
trade_data_than_500 = trade_data[trade_data['user_id'].isin(user_buy_num_than_500.index.tolist())]
x_ticks = trade_data_than_500.user_id.tolist()
x = np.arange(len(x_ticks))
y = trade_data_than_500.buy_mount.tolist()
colors = []
for _ in range(len(y)):
    r = random.random()
    g = random.random()
    b = random.random()
    colors.append((r, g, b))
bar = plt.bar(x,y,color =colors)
plt.bar_label(bar,label_type='edge')
plt.xticks(x,x_ticks)
plt.title('购买量大于500的用户购买情况')
plt.xlabel('用户id')
plt.ylabel('购买量')
plt.show()
# 2288344467在2014-11-13购买量10000件50014815大类的商品，这就能解释为什么2014-11-13的商品销量异常的高
# %%筛查购买量在500以上的客户的孩子情况
user_buy_num_than_500_user_id = user_buy_num_than_500.index.tolist()
print(baby_info[baby_info.user_id.isin(user_buy_num_than_500_user_id)])
print(trade_data[trade_data['user_id'].isin(baby_info[baby_info.user_id.isin(user_buy_num_than_500_user_id)].user_id.tolist())])
'''
说明这些用户是大型采购商，在很大程度上影响销量趋势
'''

#%%筛查购买量在100以上的客户的孩子情况
user_buy_num_than_100_user_id =  user_buy_num_than_100.index.tolist()
print(baby_info[baby_info.user_id.isin(user_buy_num_than_100_user_id)])
print(trade_data[trade_data['user_id'].isin(baby_info[baby_info.user_id.isin(user_buy_num_than_100_user_id)].user_id.tolist())])
'''
说明这些用户是中小型采购商
'''
#%% 筛查购买量在20以上的客户的孩子情况
user_buy_num_than_20_user_id =  user_buy_num_than_20.index.tolist()
print(baby_info[baby_info.user_id.isin(user_buy_num_than_20_user_id)])
print(trade_data[trade_data['user_id'].isin(baby_info[baby_info.user_id.isin(user_buy_num_than_20_user_id)].user_id.tolist()) ])
'''
说明这些用户是微小型采购商
'''