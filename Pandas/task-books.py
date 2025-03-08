# Author: 邵世昌
# CreatTime: 2024/11/5
# FileName: task-books
#%%question
#1不同年份的书的数量
#2不同年份书的平均评分情况
#%%导入库
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['KaiTi']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%数据载入
dataset = pd.read_csv('books.csv')
print(dataset.head().iloc[:,0:5])
print(dataset.info())
key = list(dataset)
print(key)

#%%数据预处理
dataset = dataset[pd.notnull(dataset['original_publication_year'])]#%%去除original_publication_year为空的列

#%%question1
dataset_original_publication_year = dataset.groupby(by = 'original_publication_year')
dataset_original_publication_year_count = dataset_original_publication_year["id"].count()
display_data = dataset_original_publication_year_count.sort_values(ascending=False).head(20)
print(display_data)
publication_year = list(map(int,display_data.index))
count = list(display_data.values)

#%%可视化
plt.figure(figsize=(12,6),dpi = 80)
p1 = plt.barh(publication_year,count,color = 'orange',label = "销售数量")
plt.bar_label(p1,label_type = "edge")
plt.yticks(publication_year)
plt.title("销售数量前20的年份及销售情况")
plt.xlabel("数量")
plt.ylabel("年份")
plt.legend(loc = "upper right")
plt.show()

#%%question2 average_rating
dataset_average_rating_grouped = dataset.groupby(by = 'original_publication_year')
dataset_average_rating_grouped_mean = dataset_average_rating_grouped["average_rating"].mean()
display_data_average_rating = dataset_average_rating_grouped_mean.sort_index(ascending=False).head(20)
print(display_data_average_rating)
publication_year_average_rating = list(map(int,display_data_average_rating.index))
average_rating =  list(display_data_average_rating.values)

#%%可视化
plt.figure(figsize=(12,6),dpi = 80)
p2 = plt.barh(publication_year_average_rating,average_rating,color = 'orange',label = "平均分数")
plt.bar_label(p2,label_type = "edge")
plt.xlim(3,5)
plt.yticks(publication_year_average_rating)
plt.title("近20年平均评分情况")
plt.xlabel("评分")
plt.ylabel("年份")
plt.legend(loc = "upper right")
plt.show()

#%%折线图(年平均分波动趋势)
plt.figure(figsize=(12,6),dpi = 80)
plt.plot(range(len(dataset_average_rating_grouped_mean.index)),dataset_average_rating_grouped_mean.values,color = 'b')
plt.xticks(range(len(dataset_average_rating_grouped_mean.index))[::15],dataset_average_rating_grouped_mean.index[::15],rotation = 45)
plt.show()