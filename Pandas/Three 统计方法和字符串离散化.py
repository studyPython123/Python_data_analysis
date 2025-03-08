# Author: 邵世昌
# CreatTime: 2024/11/3
# FileName: 统计方法和字符串离散化
#%%导入库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%读取外部数据
data_movie = pd.read_csv(r'Movie-Data.csv')
print(data_movie.head())
key = list(data_movie) #获取列标签
print(data_movie.info()) #查看数据属性

#%%获取平均分
ratings_mean = data_movie['Rating'].values.mean()
print(f"平均分为：{ratings_mean:0.3}")

#%%查看导演人数(不重复)
director = data_movie['Director'].tolist()#转换为列表
print(len(set(director)))

print(len(data_movie['Director'].unique()))#取唯一值

#%%演员人数(不重复)
temp_actors_list = data_movie['Actors'].str.split(",").tolist()
temp_actors = [i for j in temp_actors_list for i in j]
print(len(set(temp_actors)))

#%%画图显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%runtime分布情况
runtime = data_movie['Runtime (Minutes)'].values
runtime_max = runtime.max()
runtime_min = runtime.min()
num_bin = (runtime_max-runtime_min)//5
plt.figure(figsize=(12,6),dpi = 80)
counts,bins,patches = plt.hist(runtime,int(num_bin),alpha=0.5, color='green', edgecolor='black',label = f"平均时长：{np.mean(runtime)}")
for count, x in zip(counts, bins):
    plt.text(x + (bins[1] - bins[0]) / 2, count, str(int(count)), ha='center', va='bottom') #添加数值标签
plt.xticks(range(runtime_min,runtime_max+5,5))
plt.xlabel("时长")
plt.ylabel("频数",rotation=360)
plt.legend(loc='upper right')
plt.show()

#%%rating分布情况(表格优化)
ratings = data_movie['Rating'].values #获取ndarray数组
ratings_max = ratings.max()
ratings_min = ratings.min()
num_bin = (ratings_max-ratings_min)//0.5
plt.figure(figsize=(12,6),dpi = 80)
counts,bins,patches = plt.hist(ratings,int(num_bin),alpha=0.5, color='orange', edgecolor='black',label = f"平均分：{np.mean(ratings):0.3}")
for count, x in zip(counts, bins):
    plt.text(x + (bins[1] - bins[0]) / 2, count, str(int(count)), ha='center', va='bottom') #添加数值标签
plt.xticks(np.linspace(1.5,9.5,17))
plt.title("rating分布情况")
plt.xlabel("分数")
plt.ylabel("频数",rotation=360)
plt.legend(loc='upper right')
plt.show()

