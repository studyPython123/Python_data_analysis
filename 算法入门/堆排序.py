# Author: 邵世昌
# CreateTime: 2024/12/3
# FileName: 堆排序
# %%调整代码
def sift(ls,low,high): # 调整代码，大根堆
    '''
    :param ls: 列表
    :param low: 根节点位置
    :param high:最后一个元素的位置
    :return:
    '''
    i = low
    j =  2 * i + 1 # 左孩子
    temp = ls[low] # 把对顶存起来
    while j <= high:
        if j + 1 <= high and ls[j + 1] > ls[j]: # 有右孩子且大于左孩子
            j = j + 1 # 指针指向右孩子
        if temp < ls[j]:
            ls[i] = ls[j]
            i = j # 继续往下看一层
            j = 2 * i + 1
        else:
            ls[i] = temp
            break
    else:
        ls[i] = temp # 放在叶子节点上面
# %% 构建堆
def dui_Sort(ls): # 复杂度O(nlogn)
    n = len(ls)
    for i in range((n - 1) // 2, -1, -1):
        # i表示建立堆的时候调整部分的low
        sift(ls, i, n - 1)
    # 建堆完毕
    for i in range(n -1, -1 ,-1):
        ls[i], ls[0] = ls[0], ls[i]
        sift(ls, 0, i - 1)
    return ls

# %% 程序测试 (查询速度低于快速排序)
import random
import time
ls = [i for i in range(10000)]
random.shuffle(ls)
print(ls)
t = time.perf_counter()
print(dui_Sort(ls))
print(f'耗时：{time.perf_counter() - t:.8f}s')

#%%
import heapq
ls = [i for i in range(10000)]
random.shuffle(ls)
print(ls)
heapq.heapify(ls) # 建立堆
print(ls)
ls_sort = []
n = len(ls)
for i in range(n):
    ls_sort.append(heapq.heappop(ls))

# eapq.heappop(ls)每一次弹出最小的数