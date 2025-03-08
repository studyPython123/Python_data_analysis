# Author: 邵世昌
# CreatTime: 2024/11/5
# FileName: Seven 索引和复合索引
#%%导入库
import pandas as pd
import numpy as np
#%%
t = {"小明":[1,2,3,4],"小王":[5,6,7,8],"小红":list('wxyz')}
t = pd.DataFrame(t)
print(t)

#%%修改行索引
t.index = list("ABCD")
print(t)

#%%保留指定的列
t_1 = t.reindex(index=["A","C","F","G"])
print(t_1)

#%%设定某列为索引
t_2 = t.set_index("小明",drop=False)#drop=False表示表格保留该列
print(t_2)
#可以设定多列为索引(复合索引)

#%%行标签的唯一值数量
len = t.set_index("小明").index.unique()#便于去重
print(len)

#%%修改行标签
t.columns = list("大中小")
print(t)

#%%复合索引中取值
t = {"a":[1,2,3,4],"b":[5,6,7,8],"c":list('wxyz'),"d":list("opqr")}
t = pd.DataFrame(t)
t_3 = t.set_index(["a","d"],drop=True)
print(t_3)

#%%swaplevel函数(更换列索引的顺序)
b = t_3["b"]
b = b.swaplevel().iloc[2]#可以多次采用索引取元素

#%%
# b[1,"o"]#取元素

#%%读取外部数据
data = pd.read_csv(r'starbucks_store_worldwide.csv')
data_index = data.index #获取行标签
data_columns = data.columns
# print(data_index)
data_country_groupyed = data.groupby(by = "Country")
# for i in data_country_groupyed:
#     print("-" * 100)
#     print(i)
#     print("*"*100)
# print(data_country_groupyed["Brand"].count().sort_values(ascending = False).head(10))
count_top10 = data_country_groupyed["Brand"].count().sort_values(ascending = False).head(10)
country_x = list(count_top10.index)
country_y = list(count_top10.values)

#%%导入库
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['KaiTi']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

#%%可视化店铺数量排名前十的国家
# plt.figure(figsize=(12,6),dpi = 80)
plt.subplot(2,1,1)
p1 = plt.barh(country_x[::-1],country_y[::-1],color = 'orange',label = "店铺数量")
plt.bar_label(p1,label_type = 'edge')
plt.xlabel("国家")
plt.ylabel("数量")
plt.title("店铺数量前十的国家的店铺数量情况")
# 设置数字标签
# for a, b in zip(x, y):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.legend(loc = 'lower right')
plt.show()

#%%获取数据
data_CN = data[data["Country"] == "CN"]
data_CN_province_grouped = data_CN.groupby(by = 'State/Province')
data_CN_province_grouped_count = data_CN_province_grouped["Brand"].count().sort_values(ascending = False)
print(data_CN_province_grouped_count)
china_province_x = list(data_CN_province_grouped_count.index)
china_province_y = list(data_CN_province_grouped_count.values)

#%%中国每个城市的店铺数量可视化
# plt.figure(figsize=(12,6),dpi = 80)
plt.subplot(2,1,2)
p1 = plt.bar(china_province_x,china_province_y,color = 'green',label = "店铺数量")
plt.bar_label(p1,label_type = 'edge',fontsize=6)
plt.xlabel("省份")
plt.ylabel("数量")
plt.legend(loc = 'upper right')
plt.plot(china_province_y,'r')
plt.title("中国各个省份的店铺数量情况")
plt.tight_layout()
plt.show()