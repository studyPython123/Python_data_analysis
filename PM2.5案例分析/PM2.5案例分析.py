# Author: 邵世昌
# CreateTime: 2024/11/8
# FileName: PM2.5案例分析
#%%导入库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%%画图显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
#%%数据载入
dataset_beijing = pd.read_csv('BeijingPM20100101_20151231.csv')
dataset_chengdu = pd.read_csv('ChengduPM20100101_20151231.csv')
dataset_shanghai = pd.read_csv('ShanghaiPM20100101_20151231.csv')
dataset_shenyang = pd.read_csv('ShenyangPM20100101_20151231.csv')
dataset_guangzhou = pd.read_csv('GuangzhouPM20100101_20151231.csv')
print(dataset_beijing.head())
print(dataset_beijing.info())
keyword = list (dataset_beijing)
print(keyword)

#%%数据合并成dict类型
# dataset = {"beijing":dataset_beijing,"chengdu":dataset_chengdu,
#            "shanghai":dataset_shanghai,"shenyang":dataset_shenyang,"guangzhou":dataset_guangzhou}

#%%PM2.5随时间的变化，可以控制间隔区间
def function_resample(dataset,key,num,ymd):
    period = pd.PeriodIndex(year=dataset["year"], month=dataset["month"],
                            day=dataset["day"], hour=dataset["hour"], freq="h")
    dataset["datetime"] = period
    dataset.set_index("datetime", inplace=True)
    dataset_resample = dataset.resample(f"{num}{ymd}")["PM_US Post"].mean() # 可以控制切割时间段
    dataset_PM = dataset_resample.dropna(inplace=False)
    print(dataset_PM) # 可以快速的获取不同区间的预处理数据
    x_ticks = dataset_PM.index
    x = np.arange(len(x_ticks))
    y = dataset_PM.values
    index_max = np.argmax(y)
    index_min = np.argmin(y)
    print(f"{key}PM2.5浓度最高的时间是：{x_ticks[index_max]}\n最高值是：{y[index_max]}")
    print(f"{key}PM2.5浓度最低的时间是：{x_ticks[index_min]}\n最低值是：{y[index_min]}")
    plt.figure(figsize=(12, 6), dpi=80)
    plt.plot(x, y, color="orange", label=key)
    if ymd == "M":
        num = 1
        for a,b in zip(x,y):
            plt.text(a,b,b,ha="center",va="bottom",fontsize=8)#显示数值标签
    plt.xticks(x[::num], x_ticks[::num], rotation=45)
    plt.xlabel("Time")
    plt.ylabel("PM2.5浓度")
    plt.title(key + "PM2.5浓度随时间的变化情况")
    plt.legend(loc='upper right')
    plt.show()

#%%运行函数function_resample
function_resample(dataset_shenyang,"沈阳市",2,"M")

#%% 每日平均PM2.5值的统计可视化
def function_by_day(dataset,key):
    period = pd.PeriodIndex(year=dataset["year"], month=dataset["month"],
                            day=dataset["day"], hour=dataset["hour"], freq="h")
    dataset["datetime"] = period
    dataset["datetime"] = [str(i)[0:10] for i in dataset["datetime"]]
    dataset_grouped_day = dataset.groupby("datetime")["PM_US Post"].mean()
    print(dataset_grouped_day.head())
    print(dataset_grouped_day.info())
    #数据预处理（去除空值）
    dataset_grouped_day.dropna(axis = 0,how = "any",inplace=True)
    print(dataset_grouped_day)
    x_ticks = dataset_grouped_day.index
    x = np.arange(len(x_ticks))
    y = dataset_grouped_day.values
    index_max = np.argmax(y)
    index_min = np.argmin(y)
    print(f"{key}PM2.5日均浓度最高的日期是：{x_ticks[index_max]}\n最高值是：{y[index_max]}")
    print(f"{key}PM2.5日均浓度最低的日期是：{x_ticks[index_min]}\n最低值是：{y[index_min]}")
    plt.figure(figsize=(12,6),dpi = 80)
    plt.plot(x,y,color = "orange",label=key)
    plt.xticks(x[::50],x_ticks[::50],rotation=45)
    plt.xlabel("Time")
    plt.ylabel("PM2.5浓度")
    plt.title(key+"PM2.5日均浓度随时间的变化情况")
    plt.legend(loc='upper right')
    plt.show()
#%%执行founction_by_day函数
# function_by_day(dataset_beijing,"北京市")
# function_by_day(dataset_chengdu,"成都市")
# function_by_day(dataset_shanghai,"上海市")
function_by_day(dataset_guangzhou,"广州市")
# function_by_day(dataset_shenyang,"沈阳市")

#%% 每月平均PM2.5值的统计可视化(含不同检测机构的对比)
def function_by_month(dataset,key,key1):
    period = pd.PeriodIndex(year=dataset["year"], month=dataset["month"],
                            day=dataset["day"], hour=dataset["hour"], freq="h")
    dataset["datetime"] = period
    dataset["datetime"] = [str(i)[0:7] for i in dataset["datetime"]]
    dataset_grouped_day = dataset.groupby("datetime")["PM_US Post"].mean()
    # print(dataset_grouped_day.head())
    # print(dataset_grouped_day.info())
    #数据预处理（去除空值）
    dataset_grouped_day.dropna(axis = 0,how = "any",inplace=True)
    # print(dataset_grouped_day)
    x_ticks = dataset_grouped_day.index
    x = np.arange(len(x_ticks))
    y = dataset_grouped_day.values
    index_max = np.argmax(y)
    index_min = np.argmin(y)
    print(f"{key}PM2.5月均浓度最高的月份是：{x_ticks[index_max]}\n最高值是：{y[index_max]}")
    print(f"{key}PM2.5月均浓度最低的月份是：{x_ticks[index_min]}\n最低值是：{y[index_min]}")
    plt.figure(figsize=(12,6),dpi = 80)
    plt.plot(x,y,color = "orange",label=key)
    # for a,b in zip(x,y):
    #     plt.text(a,b,b,ha="center",va="bottom",fontsize=8)#显示数值标签
    plt.xticks(x,x_ticks,rotation=45)
    plt.xlabel("Time")
    plt.ylabel("PM2.5浓度")
    plt.title(key+"PM2.5月均浓度随时间的变化情况")
    #PM_Dongsi
    dataset["datetime"] = period
    dataset["datetime"] = [str(i)[0:7] for i in dataset["datetime"]]
    dataset_grouped_day = dataset.groupby("datetime")["PM_Dongsi"].mean()
    # print(dataset_grouped_day.head())
    # print(dataset_grouped_day.info())
    #数据预处理（去除空值）
    dataset_grouped_day.dropna(axis = 0,how = "any",inplace=True)
    # print(dataset_grouped_day)
    x_ticks = dataset_grouped_day.index
    x = np.arange(len(x_ticks))
    y = dataset_grouped_day.values
    index_max = np.argmax(y)
    index_min = np.argmin(y)
    print(f"{key1}PM2.5月均浓度最高的月份是：{x_ticks[index_max]}\n最高值是：{y[index_max]}")
    print(f"{key1}PM2.5月均浓度最低的月份是：{x_ticks[index_min]}\n最低值是：{y[index_min]}")
    plt.plot(x, y, color="green", label=key1)
    # for a,b in zip(x,y):
    #     plt.text(a,b,b,ha="center",va="bottom",fontsize=8)#显示数值标签
    plt.legend(loc='upper right')
    plt.show()

#%%执行founction_by_month函数
function_by_month(dataset_beijing,"北京市PM_US Post","北京市PM_Dongsi")
# function_by_month(dataset_chengdu,"成都市")
# function_by_month(dataset_shanghai,"上海市")
# function_by_month(dataset_guangzhou,"广州市")
# function_by_month(dataset_shenyang,"沈阳市")

#%%PM2.5随时间的变化趋势
def function_by_hour(dataset,key):
    #把分开的时间字符串通过periodIndex的方法转化为pandas的时间类型
    period = pd.PeriodIndex(year=dataset["year"],month=dataset["month"],
                            day=dataset["day"],hour=dataset["hour"],freq="h")
    dataset["datetime"] = period
    print(dataset.head())
    #数据预处理（去除空值）"PM_US Post"
    data = pd.concat([dataset["datetime"],dataset["PM_US Post"]],axis=1)
    data.dropna(axis = 0,how = "any",inplace=True)
    x_ticks = data['datetime']
    y = data['PM_US Post']
    index_max = np.argmax(y)
    index_min = np.argmin(y)
    print(f"{key}PM2.5浓度最高的时间是：{x_ticks.iloc[index_max]}\n最高值是：{y.iloc[index_max]}")
    print(f"{key}PM2.5浓度最低的时间是：{x_ticks.iloc[index_min]}\n最低值是：{y.iloc[index_min]}")
    x = np.arange(len(x_ticks))
    plt.figure(figsize=(10,6),dpi = 80)
    plt.plot(x,y,color = 'orange',label = key)
    plt.xticks(x[::1000],x_ticks[::1000],rotation =45)
    plt.xlabel("Time")
    plt.ylabel("PM2.5浓度")
    plt.title(key+"PM2.5随时间的变化情况")
    plt.legend(loc='upper right')
    plt.show()
#%%执行函数function
# function_by_hour(dataset_beijing,"北京市")
# function_by_hour(dataset_chengdu,"成都市")
# function_by_hour(dataset_shanghai,"上海市")
# function_by_hour(dataset_guangzhou,"广州市")
function_by_hour(dataset_shenyang,"沈阳市")