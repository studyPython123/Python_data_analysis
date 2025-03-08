# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 列表排序
#%%
import numpy as np
#%%
def function(n):
    #索引偶数项逆序
    list_ = np.random.randint(0,100,size = n)
    print(f"排序前的序列是：{list_}")
    list_[::2] = sorted(list_[::2], reverse = True)
    print(f"索引偶数项逆序排序后的序列是：{list_}")
    list_[1::2] = sorted(list_[1::2], reverse = True)
    print(f"索引奇数项逆序排序后的序列是：{list_}")
#%%
n = int(input("请输入一个整数："))
function(n)
