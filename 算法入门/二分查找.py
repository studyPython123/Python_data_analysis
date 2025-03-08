# Author: 邵世昌
# CreateTime: 2024/12/1
# FileName: 二分查找
# %%自定义二分查找数值列表(找到就结束)
import time
def erfen_search(li,element): # 循环减半，复杂度是O(logn)
    li_sorted = sorted(li,reverse=False)
    left = 0
    right = len(li_sorted)-1
    while left <= right: # 候选区有值
        mid = (left + right) // 2
        if element > li_sorted[mid]:
            left = mid+1
        elif element < li_sorted[mid]:
            right = mid-1
        else:
            result = f'{li}升序排序后查找到元素{element}的索引为{mid}'
            return result
    result = f'{li}中未查找到元素{element}'
    return result
# 函数运行
if __name__ == '__main__':
    a = input("请输入列表：").split(',')
    li = list(map(int,a)) # 转换为列表
    element = int(input("请输入需要查找的元素："))
    t = time.perf_counter() # 计时精度高
    print(erfen_search(li, element))
    print(f'耗时：{time.perf_counter() - t:.8f}s')
