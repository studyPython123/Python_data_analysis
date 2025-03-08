# Author: 邵世昌
# CreatTime: 2024/11/2
# FileName: Two_DataFrame
#%%导入库
import pandas as pd
import numpy as np

#%%创建DataFrame
data = pd.DataFrame(np.arange(12).reshape((3,4)),index = ['X','Y','Z'],columns=['A','B','C','D'])
print(data)

#%%获取行列索引
index_data = data.index
column_data = data.columns
print("行索引：\n",list(index_data))
print("列索引：\n",list(column_data))

#%%创建多维字典转换为DataFrame
columns=list("ABCDEFGHI")
temp_dict1 = {columns[i]:(i,i*2) for i in range(len(columns))}
print("字典：\n",temp_dict1)
pf = pd.DataFrame(temp_dict1)
print("二维表格：\n",pf)

#%%多个字典创建DateFrame
temp_dict1 = {columns[i]:(float(i),float(i*2)) for i in range(len(columns))}
temp_dict2 = {columns[i]:(float(i*2),float(i*3)) for i in range(len(columns))}
temp_dict3 = {columns[i]:(float(i*3),float(i*4)) for i in range(len(columns))}
temp_dicts = [temp_dict1,temp_dict2,temp_dict3]
pf = pd.DataFrame(temp_dicts)
print(pf) #缺失字段显示为NaN

#%%情况查询
print(pf.head())
print(pf.tail())
print(pf.shape)
print(pf.info())
print(pf.describe())

#%%导入外部数据
data = pd.read_csv(r"dogNames2.csv")
print("前五行数据：\n",data.head(),"\n数据类型：\n",data.info())
data_columns = list(data.columns)

#%%排序方法
data_sorted = data.sort_values(by=data_columns[1],ascending=False)
print(data_sorted.head())

#%%DataFrame切片
print(data_sorted[:20]) #前20行
print(data_sorted[data_columns[0]],type(data_sorted[data_columns[0]])) #取列，Serier类型

#%%生成随机DataFrame
t = pd.DataFrame(np.random.randint(1,100,(3,4)),index = ['X','Y','Z'],columns=['A','B','C','D'])

#%%loc
print(t)
print(t.loc["X","A"]) #通过标签索引行数据
print(t.loc[["X","Z"],["A","D"]])
print(t.loc["Y",["A","C"]])
print(t.loc["X":"Z",["B","C"]])#Z被选中了

#%%iloc
print(t)
print(t.iloc[0,0])#通过位置获取行数据
print(t.iloc[[0,2],[0,3]])
print(t.iloc[1,[0,2]])
print(t.iloc[0:3,[1,2]])

#%%布尔索引
data[(data[data_columns[1]]>800)&(data[data_columns[1]]<1000)]

#%%筛选符合条件的内容
data[(data[data_columns[0]].str.len()>4)&(data[data_columns[1]]>700)]

#%%切割成列表
print(data[data_columns[0]].str.split(""))
print(data[data_columns[0]].str.split("").tolist())#转为列表

#%%查找缺失值
print(pd.isnull(data).head())
print(data[pd.notnull(data).head(4)])

#%%删除NAN所在行列
data.dropna(axis = 0,how = "any",inplace=True)# inplace是否原地修改，只要有NAN就删除
data.dropna(axis = 0,how = "all",inplace=True)#全都是NAN才删除

#%%填充缺失值
data.fillna(data.mean(),inplace = True) #用均值填充