# Author: 邵世昌
# CreatTime: 2024/11/6
# FileName: Pandas时间序列
#%%导入库
import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
plt.rcParams['font.sans-serif'] = ['KaiTi']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%数据载入
dataset = pd.read_csv('911.csv')
print(dataset.head())
print(dataset.info())
print(dataset.columns)

#%%数据预处理
dataset["title_grouped"] = [i.split(":")[0] for i in dataset["title"]] #新增，不改变原数据
keyword = list(set(dataset["title_grouped"]))

#%%question1(不同类型的紧急情况的次数)
dataset_title_grouped_count = dataset.groupby(by = "title_grouped")["title_grouped"].count()
title = dataset_title_grouped_count.index
count = dataset_title_grouped_count.values
print(dataset_title_grouped_count)

#%%可视化
plt.figure(figsize = (12,6),dpi = 80)
p1 = plt.bar(title,count,width = 0.3,color = 'orange',label = '次数')
plt.bar_label(p1,label_type = "edge")
plt.title("不同类型的紧急情况的次数")
plt.xlabel("类型")
plt.ylabel("次数")
plt.legend(loc = "upper right")
plt.show()

#%%数据预处理
dataset["timeStamp_grouped"] = [i.split('-')[0]+"-"+i.split('-')[1] for i in dataset["timeStamp"]]

#%%question2(不同月份不同类型的紧急情况的次数)
dataset_month_title_grouped = dataset.groupby(by = ["title_grouped","timeStamp_grouped"])["title_grouped"].count()
print(dataset_month_title_grouped.head(9))

#%%可视化
month_grouped = dataset_month_title_grouped["EMS"].index
EMS_grouped_count = dataset_month_title_grouped["EMS"].values
Fire_grouped_count = dataset_month_title_grouped["Fire"].values
Traffic_grouped_count = dataset_month_title_grouped["Traffic"].values
x_label = np.arange(len(month_grouped))
plt.figure(figsize=(12,10),dpi = 80)
plt.plot(x_label,EMS_grouped_count,color = 'orange',label = 'EMS')
plt.plot(x_label,Fire_grouped_count,color = 'blue',label = 'Fire')
plt.plot(x_label,Traffic_grouped_count,color = 'green',label = 'Traffic')
for a,b in zip(x_label,EMS_grouped_count):
    plt.text(a,b,b, ha='center', va='bottom', fontsize=8)
for a,b in zip(x_label,Fire_grouped_count):
    plt.text(a,b,b, ha='center', va='bottom', fontsize=8)
for a,b in zip(x_label,Traffic_grouped_count):
    plt.text(a,b,b, ha='center', va='bottom', fontsize=8)
plt.xticks(x_label,month_grouped,rotation=45)
plt.tick_params(axis='both', which='major',labelsize=8)
plt.legend(loc='upper right',fontsize=14)
plt.xlabel("Month",fontsize=14)
plt.ylabel("Count",fontsize=14,rotation=360)
plt.title("不同月份不同类型的紧急情况的次数")
plt.grid(alpha = 0.4)
plt.show()

#%%不同月份的电话次数
dataset_month_grouped = dataset.groupby(by = ["timeStamp_grouped"])["title_grouped"].count()
print(dataset_month_grouped.head(9))

#%%不同月份的电话次数
index_x = dataset_month_grouped.index
x = np.arange(len(index_x))
y = dataset_month_grouped.values
plt.figure(figsize = (12,6),dpi = 80)
plt.plot(x,y,'orange',label ="电话次数")
# 设置数字标签
for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=8)
plt.xticks(x,index_x,rotation = 45)
plt.title("不同月份的电话次数")
plt.legend(loc = "upper right")
plt.tick_params(axis='both', which='major', labelsize = 8)  # 设置坐标轴刻度字体大小为12
plt.grid(alpha = 0.4)
plt.show()

#%%对应填充方法求question1(该方法适合获取可视化矩阵)(好方法，效率高很多，不要用循环遍历)
zero_df = pd.DataFrame(np.zeros((dataset.shape[0],len(keyword))),columns = keyword)
for key in keyword:
    zero_df[key][dataset["title_grouped"].str.contains(key)] = 1 #好方法，记住
print(zero_df.head())

#%%计数
count_ = np.sum(zero_df,axis =0)
print(count_)

#%%date_range生成时间
date_day = pd.date_range(start='2020-01-01',end='2020-12-31',freq='D')
date_month = pd.date_range(start='2020-01-01',end='2020-12-31',freq='ME')
date_year = pd.date_range(start='2020-01-01',end='2020-12-31',freq='YE')
date_10_day = pd.date_range(start='2020-01-01',end='2020-12-31',freq='10D')
date_day_10_numbers = pd.date_range(start='2020-01-01',periods=10,freq='D')
print(date_day_10_numbers)

#%%to_datetime函数转换为时间类型
dataset["timeStamp"] =pd.to_datetime(dataset["timeStamp"])

#%%resample函数(生成的数据不是很准确)
dataset.set_index("timeStamp",inplace=True)#已经变化，不能再重复运行

#%%
count_by_month = dataset.resample("ME").count()
print(count_by_month.head())