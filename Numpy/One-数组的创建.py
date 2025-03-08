# Author: 邵世昌
# CreatTime: 2024/10/29
# FileName: One
# numpy  处理数值型数据
import numpy as np
import random as rand
# %% 使用numpy生成数组
t1 = np.array([1,2,3])
t2 = np.array(range(10))
t3 = np.arange(10) # t2 和 t3相同
print(t1)
print(t2)
print(t3)
# %%设置数组类型
t4 = np.array(range(10),dtype="int64")
print(t4)
print(t4.dtype)

# %%调整数据类型
t5 = t4.astype("float32")
print(t5)
print(t5.dtype)

# %%生成小数
t6 = np.array([rand.random() for i in range(10)])
print(t6)
print(t6.dtype)
# 修改小数位数
t7 = np.round(t6,2)
print(t7)