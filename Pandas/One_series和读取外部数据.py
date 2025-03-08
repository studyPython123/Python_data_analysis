# Author: 邵世昌
# CreatTime: 2024/11/1
# FileName: One_series和读取外部数据
#%%导入库
import string
import pandas as pd

#%%series创建
#series表示一维数据（带标签的数组）
t = pd.Series(range(3), index=['a','b','c'])#index指定索引
print(t,"\n",type(t))

#%%用字典创建series
temp_dict = {"a":10,"b":20,"c":30}
t1 = pd.Series(temp_dict)
print(t1,"\n",type(t1))

#%%用生成器生成字典
temp_list = ['a','b','c','d']
temp_dict1 = {temp_list[i]:i for i in range(4)}
print(temp_dict1)

#%%创建字母的函数
temp_string = string.ascii_uppercase[0:5]
print(temp_string)

#%%
#获取表格索引
index_t1 = t1.index
#获取值
value_t1 = t1.values #numpy.ndarray
print(t1.head()) #默认查看前几行数据

#%%和ndarray相同的函数
print(t1.argmax(axis=0))
print(t1.argmin(axis=0))
print(t1.clip(15,25))
print(t1.where(t1 >10,15)) #与ndarray的作用相反

#%%读取外部数据(csv文件)
data_dog_name = pd.read_csv(r'dogNames2.csv')
print(data_dog_name.head())