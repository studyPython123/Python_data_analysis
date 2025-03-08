# Author: 邵世昌
# CreatTime: 2024/10/29
# FileName: Two
import numpy as np
# %%创建二维数组
t1 = np.array([[1,2,3,4,5,6],[2,3,4,5,6,7]])
print(t1)
print(t1.shape)

# %%修改形状
t2 = t1.reshape(3,4)
print(t2)
print(t2.shape)

# %%创建多维数组
t3 = np.arange(24).reshape(2,3,4) #2块3行4列
print(t3)
print(t3.shape)

# %%降维 reshape有返回值，不改变原先数组
t4 = t3.reshape(6,4)
print(t4)
print(t4.shape)

t5 = t4.reshape(24)
print(t5)
print(t5.shape)

# %% 直接转为一维数组
t6 = t3.flatten()
print(t6)
print(t6.shape)

# %%数组的计算
# 基本计算+-×÷：对应位置+-×÷
# %%列维度相同（广播原则）
t7 = np.arange(4)
t8 = t4 - t7
print(t8)

#%%行维度相同
t9 = np.arange(6).reshape(6,1)
t10 = t4 - t9
print(t10)