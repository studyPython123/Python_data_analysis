# Author: 邵世昌
# CreateTime: 2024/12/2
# FileName: 插入排序
# %%
import random
import time
def insert_Sort(ls): # 时间复杂度O(n^2)
    for i in range(1, len(ls)): # i 表示摸到的数字的下标
        temp = ls[i] # 摸到的牌
        j = i - 1 # 手中最后一张牌
        while ls[j] > temp and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = temp
        print(f'第{i}步：{ls}')
    return ls
if __name__ == '__main__':
    ls = [random.randint(1,100) for i in range(15)]
    print(f'插入算法排序前列表：{ls}')
    t = time.perf_counter()
    print(f'插入算法排序后列表：{insert_Sort(ls)}')
    print(f'耗时：{time.perf_counter() - t:.8f}s')


