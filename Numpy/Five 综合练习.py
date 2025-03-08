# Author: 邵世昌
# CreatTime: 2024/10/31
# FileName: Five 综合练习
import numpy as np
import matplotlib.pyplot as plt
#%%导入数据
data_US = np.loadtxt('US_videos.csv', delimiter=",",dtype = "int")
data_GB = np.loadtxt('GB_videos.csv', delimiter=",",dtype = "int")
#%%截取评论数
data_US_comment = data_US[:,-1] #最后一列
data_US_comment = np.clip(data_US_comment, 0, 50000)
d = 1000
bins_num = (data_US_comment.max() - data_US_comment.min()) // d
plt.figure(figsize=(12,6),dpi = 80)
plt.hist(data_US_comment, bins = bins_num)
plt.title("Comment")
plt.show()

#%% 练习2
data_GB = data_GB[data_GB[:,1]<=50000]
data_GB_comment = data_GB[:,-1]
data_GB_like = data_GB[:,1]
plt.figure(figsize=(12,6),dpi = 80)
plt.scatter(data_GB_like,data_GB_comment)
plt.title("Relation between comment and like")
plt.show()