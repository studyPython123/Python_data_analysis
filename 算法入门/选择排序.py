# Author: 邵世昌
# CreateTime: 2024/12/2
# FileName: 选择排序
#%%
import random
import time
# %% 不好的普通算法
def select_Sort_simple(ls): # 不推荐，复杂度是： O(n^2)
    ls_new = []
    lenth = len(ls)
    for i in range(lenth):
        ls_new.append(min(ls))
        ls.remove(min(ls))
    return ls_new
if __name__ == '__main__':
    ls = [random.randint(1,10000) for i in range(1000)]
    print(f'普通算法排序前列表：{ls}')
    t = time.perf_counter()
    print(f'普通算法排序后列表：{select_Sort_simple(ls)}')
    print(f'耗时：{time.perf_counter() - t:.8f}s')

#%% 改进算法
def select_Sort_improve(ls,reserve): # 时间复杂度(O(n^2))
    for i in range(len(ls) - 1): # 第几趟
        min_index = i
        for j in range(i + 1, len(ls)):
            if reserve:
                if ls[min_index] > ls[j]:
                    min_index = j
            else:
                if ls[min_index] < ls[j]:
                    min_index = j
        ls[min_index], ls[i] = ls[i], ls[min_index]
    return ls
if __name__ == '__main__':
    ls = [random.randint(1,10000) for i in range(1000)]
    print(f'改进算法排序前：{ls}')
    t = time.perf_counter()
    print(f'改进算法排序后：{select_Sort_improve(ls,reserve = False)}')
    print(f'耗时：{time.perf_counter() - t:.8f}s')