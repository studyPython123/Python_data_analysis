# Author: 邵世昌
# CreateTime: 2024/12/8
# FileName: topk问题
# %% 取n个数前k大的元素，排序后切片时间复杂度O(nlogn)
# 用冒泡排序
def kthLargest_maopao(ls,k):# 时间复杂度O(kn)
    n = 0
    for i in range(len(ls)-1):
        exchange = False
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1],ls[j]
                exchange = True
        n += 1
        # 用k作为判断条件，控制排序次数
        if not exchange or n >= k:
            return ls
    return ls
#%% 运行测试
import random
import time
ls = [i for i in range(10000)]
random.shuffle(ls)
print(ls)
t = time.perf_counter()
print(kthLargest_maopao(ls,10)[-10:])
print(f'耗时：{time.perf_counter() - t:.8f}s')

#%% 时间复杂度更低的算法，堆排序时间复杂度O(nlogk)
def sift(ls,low,high): # 调整代码，小根堆
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
        if j + 1 <= high and ls[j + 1] < ls[j]: # 有右孩子且大于左孩子
            j = j + 1 # 指针指向右孩子
        if temp > ls[j]:
            ls[i] = ls[j]
            i = j # 继续往下看一层
            j = 2 * i + 1
        else:
            ls[i] = temp
            break
    else:
        ls[i] = temp # 放在叶子节点上面
#%%
def topk(ls,k):
    heap = ls[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    # 建堆
    for i in range(k,len(ls)-1):
        if ls[i] > heap[0]:
            heap[0] = ls[i]
            sift(heap,0,k-1)
    # 遍历
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,k-1)
    return heap
#%% 测试
import random
import time
ls = [i for i in range(10000)]
random.shuffle(ls)
print(ls)
t = time.perf_counter()
print(topk(ls,10))
print(f'耗时：{time.perf_counter() - t:.8f}s')



