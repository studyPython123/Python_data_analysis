# Author: 邵世昌
# CreateTime: 2024/12/2
# FileName: 冒泡排序
# %%自定义冒泡排序算法(复杂度：O(n^2))
import time
import random
def maopao_Sort(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls
if __name__ == '__main__':
    ls = [random.randint(1, 50) for i in range(10)]
    print(f'基础算法排序前的列表是：{ls}')
    print(f'基础算法排序后的列表是：{maopao_Sort(ls)}')

# %%改进(当一趟没有变化的时候跳出循环，后续不用再遍历)
def maopao_Sort_imporve(ls,reverse):
    for i in range(len(ls) - 1):
        exchange = False
        for j in range(len(ls) - 1 - i):
            if not reverse:
                if ls[j] > ls[j + 1]:
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
                    exchange = True # 不要总是用计数判断
            else:
                if ls[j] < ls[j + 1]:
                    ls[j], ls[j + 1] = ls[j + 1], ls[j]
                    exchange = True # 不要总是用计数判断
        if not exchange:
            return ls
    return ls
if __name__ == '__main__':
    ls = list(range(10000))
    random.shuffle(ls)
    # ls = [random.randint(1, 50) for i in range(10)]
    print(f'改进算法排序前的列表是：{ls}')
    t = time.perf_counter()
    print(f'改进算法排序后的列表是：{maopao_Sort_imporve(ls,reverse = True)}')
    print(f'耗时：{time.perf_counter() - t:.8f}s')
    t = time.perf_counter()
    print(f'改进算法排序后的列表是：{maopao_Sort_imporve(ls,reverse = False)}')
    print(f'耗时：{time.perf_counter() - t:.8f}s')
# 改进算法不仅能够选择排序方式，还减少了查询次数