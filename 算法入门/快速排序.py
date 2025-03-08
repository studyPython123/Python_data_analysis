# Author: 邵世昌
# CreateTime: 2024/12/2
# FileName: 快速排序
#%%
import random
def partition(arr, low, high,reverse): # 从两边查找保证左边小，右边大
    temp = arr[low]
    if not reverse:
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while arr[low] <= temp and low < high:
                low += 1
            arr[high] = arr[low]
    else:
        while low < high:
            while low < high and arr[high] <= temp:
                high -= 1
            arr[low] = arr[high]
            while arr[low] >= temp and low < high:
                low += 1
            arr[high] = arr[low]
    arr[low] = temp
    return low,arr
# %% 改进快速排序(需要提前知道列表的长度)
def quick_sort(array,left,right,reverse): # 时间复杂度O(nlogn)
    if left < right:
        mid,array = partition(array,left,right,reverse)
        quick_sort(array,left,mid - 1,reverse)
        quick_sort(array,mid + 1,right,reverse)
    return array
import time
# arr = [random.randint(1,100) for i in range(15)]
#%%
arr = list(range(10000))
random.shuffle(arr)
print(f'快速排序算法排序前：{arr}')
t = time.perf_counter()
print(f'快速排序算法归位后：{partition(arr, 0, len(arr) - 1, True)[1]}')
print(f'快速排序算法排序后：{quick_sort(arr, 0, len(arr) - 1, True)}')
print(f'耗时：{time.perf_counter() - t:.8f}s')

# 缺点(最糟糕的情况：已经逆序的序列)
# 递归默认最大深度是996
#%% 修改递归的深度
# import sys
# sys.setrecursionlimit(10000) # 设置位10000