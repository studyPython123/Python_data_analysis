# Author: 邵世昌
# CreatTime: 2024/10/31
# FileName: Four nan和常用方法
import numpy as np
#%%导入数据
data_US = np.loadtxt('US_videos.csv', delimiter=",",dtype = "int")
data_GB = np.loadtxt('GB_videos.csv', delimiter=",",dtype = "int")

#%%添加国家信息
data_US_1 = np.ones((data_US.shape[0],1))
data_GB_1 = np.ones((data_GB.shape[0],1))
data_US = np.hstack((data_US,data_US_1))
data_GB = np.hstack((data_GB,data_GB_1))

#%%拼接两组数组
data_US_GB = np.vstack((data_US,data_GB))

#%%求最大值最小值位置
t =[ [1,2,3,4],[4,5,6,7]]
print(np.argmax(t,axis=0)) #axis = 0表示取每一列的最大值
print(np.argmin(t,axis=1))#axis = 1表示去每一行的最小值

#%%生成随机数
t1 = np.random.randint(0,5,(2,3)) #随机整数
t2 = np.random.random((2,3)) #0-1之间的浮点数
t3 = np.random.uniform(1,15,(2,3)) #均匀分布
#%% 生成随机数种子
np.random.seed(5) #保证随机数字和之前一次一样
t4 = np.random.randint(10,20,(2,3))
print(t4)

#%% nan 和 inf (float类型)
a = np.inf
b = np.nan
t = [1,2,3,4,np.inf,np.nan]
#判断nan的数量
number_1 = np.count_nonzero(t != t)
number_2 = np.count_nonzero(t == t)

#%%判断是否是nan或者inf类型
np.isnan(t)
np.isinf(t)
t[np.isnan(t)] = 100
t[np.isinf(t)] = 100

#%%算特征值
data = np.arange(0,24).reshape(4,6)
data.sum(axis = 0) #计算每一列的和
data.sum(axis = 1 ) #计算每一行的和
data.mean(axis = 0) #均值
data.mean(axis = 1)
np.ptp(data,axis = 0) #求极值
np.median(data,axis = 0)

#%% 综合练习(重要)
def fill_ndarray(data):
    data = np.arange(12).reshape((3,4)).astype(float)
    data[1,2:] = np.nan
    for i in range(data.shape[1]):
        temp_col = data[:,i] #当前一列
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num !=0:
            temp_col[np.isnan(temp_col)] = np.nanmean(temp_col)
            # temp_not_nan_col = temp_col[temp_col==temp_col] #当前一列不为nan的array
            # temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean() #赋值nan
    return data
if __name__ == '__main__':
    data = np.arange(12).reshape(3,4).astype(float)
    data[1,2:] = np.nan
    print(data)
    data = fill_ndarray(data)
    print(data)

#%%
data = np.arange(24).astype(float)
data[5] = np.nan
print("第一种求法\n",data.sum(),"\n",data.mean())
print("\n第二种求法\n",np.nansum(data),"\n",np.nanmean(data))
