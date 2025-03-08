# Author: 邵世昌
# CreatTime: 2024/11/4
# FileName: Six 数据分组和聚合
#%%导入数据库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%读取外部数据
data = pd.read_csv(r'starbucks_store_worldwide.csv')
dataset = pd.DataFrame(data)
print(dataset.head())
print(dataset.info()) #查看有没有缺失值
print(list(dataset))

#%%分组方法(groupby函数)
grouped = dataset.groupby(by = 'Country')
print(grouped)

#%%统计各个国家的记录的数量
Group_Country_count = grouped["Brand"].count()
print(f"美国的店面数量是{Group_Country_count["US"]}家")
print(f"中国的店面数量是{Group_Country_count["CN"]}家")

#%%统计中国每个省份的店面数量(count计算非nan的数量)
Group_CN = dataset[dataset["Country"]=="CN"]
Group_CN_grouped = Group_CN.groupby(by = 'State/Province')
Group_CN_Province_count = Group_CN_grouped["Brand"].count()
# for i in Group_CN_grouped:
#     print("-" * 100)
#     print(i)
#     print("*"*100)
print(Group_CN_Province_count)

#%%遍历打印每个分组
for i in grouped:
    print("-" * 100)
    print(i)
    print("*"*100)

#%%快速选取选的的一类数据
Country_AR = dataset[dataset["Country"]=="AR"]
print(Country_AR["Brand"].count()) #按照某个字段计数

#%%按多个字段分组
group = dataset.groupby(by=["Country","State/Province"]).count()
print(group.head(10))  #展示所有字段
print(type(group))

#%%按多个字段分组
group = dataset["Brand"].groupby(by=[dataset["Country"],dataset["State/Province"]]).count()
print(group.head(10)) #展示筛选字段
print(type(group))

#%%继续保存DataFrame类型
group = dataset[["Brand"]].groupby(by=[dataset["Country"],dataset["State/Province"]]).count()
print(type(group))
