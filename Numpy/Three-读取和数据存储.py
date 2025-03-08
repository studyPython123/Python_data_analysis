# Author: 邵世昌
# CreatTime: 2024/10/30
# FileName: Three
import numpy as np
# %%导入数组
data_1 = np.loadtxt('US_videos.csv', delimiter=",",dtype = "int")# unpack转置
data_2 = np.loadtxt('US_videos.csv', delimiter=",",dtype = "int",unpack=True)
print("第一个数组：",data_1[0,:])
print("第二个数组：",data_2[0,:])

# %%转置的另外三个方法
data_3 = data_1.swapaxes(1,0)
data_4 = data_1.transpose() #excel里面也是这个函数
data_5 = data_1.T
print("第三个数组：",data_3[0,:])
print("\n第四个数组：",data_4[0,:])
print("\n第五个数组：",data_5[0,:])

# %%切片
data1 = data_1[:,1] #取一列
data2 = data_1[1,:] # 取一行
data3 = data_1[1:3] # 取多行
data4 = data_1[:,2:4] # 取多列
data5 = data_1[[1,6,9,10,22,36,55,88]] # 不连续多行
data6 = data_1[:,[1,3]] #不连续多列
data7 = data_1[[0,2],[0,1]] # 取不相邻的点（0，0）（2，1）
data = data_1[::2] #每间隔一个取一个

# %%  数值的修改
data8 = data_1[0:6,]
np.where(data8<10000,0,10)# where函数
data8.clip(1000,5000)# 小于1000替换为1000，大于5000替换为5000

# %%数组的拼接
data8 = data_1[0:6,]
data9 = data_1[100:106,]
np.vstack((data8,data9)) #竖直拼接
np.hstack((data8,data9)) #水平拼接

#%%行列交换
data8[[1,2],:] = data8[[2,1],:] #行交换(第一行和第二行)
data8[:,[1,2]] = data8[:,[2,1]] #列交换(第一列和第二列)

#%%拼接两组数据
data_US = np.loadtxt('US_videos.csv', delimiter=",",dtype = "int")
data_GB = np.loadtxt('GB_videos.csv', delimiter=",",dtype = "int")