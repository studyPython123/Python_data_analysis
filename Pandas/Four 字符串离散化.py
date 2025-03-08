# Author: 邵世昌
# CreatTime: 2024/11/3
# FileName: 数据的合并和分组聚合
#%%导入库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%画图显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%读取外部数据
data = pd.read_csv(r'Movie-Data.csv')
key = list(data.columns)
data_genre = data['Genre'].str.split(",").tolist() #[[],[],[]]
labels = list(set([i for j in data_genre for i in j]))

#%%构建分类矩阵
df_group = pd.DataFrame(np.zeros((1000,len(labels))),columns=labels)
for i in range(1000):
    df_group.loc[i,data_genre[i]] = 1 #好方法
print(df_group.head())

#%%统计每个人分类的电影的数量和
genre_counts = df_group.sum(axis = 0) #每一列求和
print(genre_counts)

#%%排序
genre_counts = genre_counts.sort_values()

#%%可视化(条形图)
plt.figure(figsize=(10,6),dpi = 80)
p1 = plt.barh(labels,genre_counts,color = 'orange',label= "电影数量")
plt.bar_label(p1,label_type = 'edge')
plt.title("不分类电影的数量和")
plt.ylabel("数量",rotation=360)
plt.legend(loc='lower right')
plt.xlabel("电影类型")
# plt.tight_layout() #防止重叠
plt.savefig("Movie-Genre-barh.png")
plt.show()

#%%可视化(柱状图)
plt.figure(figsize=(10,6),dpi = 80)
x = np.arange(len(labels))
p1 = plt.bar(x,genre_counts,color = 'orange',label= "电影数量")
plt.bar_label(p1,label_type = 'edge')
plt.xticks(x,labels,rotation = 45)
plt.ylabel("数量",rotation=360)
plt.title("不分类电影的数量和")
plt.xlabel("电影类型")
plt.legend(loc='upper left')
plt.plot(genre_counts,color = 'red')
plt.savefig("Movie-Genre-bar.png")
# plt.tight_layout()
plt.show()