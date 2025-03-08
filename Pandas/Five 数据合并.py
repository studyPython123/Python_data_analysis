# Author: 邵世昌
# CreatTime: 2024/11/4
# FileName: Five 数据合并

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

#%%表格拼接（不需要行或列相同）
df1 = pd.DataFrame(np.zeros((2,4)))
df2 = pd.DataFrame(np.ones((3,3)))
horizontal_concat1 = pd.concat([df1, df2], axis=1) # 水平拼接
horizontal_concat0 = pd.concat([df1, df2], axis=0) # 竖直拼接

#%%表格拼接，join函数(（inner、outer、left、right）)(按照行索引)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'b'])
df2 = pd.DataFrame({'C': [5, 6]}, index=['a', 'c'])
result = df1.join(df2,how='outer')  # how连接
print(result)

#%%表格拼接，merge函数(（inner、outer、left、right）)(按照列索引)
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['B', 'C', 'D'], 'value': [4, 5, 6]})
result = pd.merge(df1, df2, on='value', how='inner')#以on为基准how连接
print(result)

#%%说明
# join() 和 merge() 都是强大的工具，用于数据连接。
# 选择哪个方法取决于具体需求：
# 如果你需要根据索引连接，使用 join()；
# 如果你需要根据某些列连接，使用 merge()。

#%%join函数拼接列表字符串(只能是字符串，不能是数字)
list_1 = ['I','L','O','V','E','Y','O','U']
list_1 = '-'.join(list_1) #拼接后是str类型
print(list_1)
print(type(list_1))

#%%拼接原数据和分类数据(两组数据的行数相同)
data_group_concat = pd.concat([data, df_group], axis=1)
print(data_group_concat.head())
