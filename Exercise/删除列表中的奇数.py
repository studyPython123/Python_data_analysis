# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 删除列表中的奇数
#%%
import numpy as np
def function(n):
    list_ = np.random.randint(0,100,n)
    list_ = list(list_)
    print(f"删除奇数前的序列是：{list_}")
    result = []
    for i in list_:
        if i % 2 == 0:
            result.append(i)
    print(f"删除奇数后的序列是：{result}")
#%%
n = int(input("请输入一个整数："))
function(n)