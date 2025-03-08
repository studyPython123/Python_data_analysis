# Author: 邵世昌
# CreateTime: 2024/12/1
# FileName: 顺序查
import time
#%% 自定义顺序查找函数
def line_search(li,element,num): # 复杂度O(n)
    index_list = []
    for index,ele in enumerate(li):
        if ele == element:
            index_list.append(index)
        if len(index_list) == num: # 确定查找数目
            break
    if len(index_list) == 0:
        return None
    else:
        return index_list

# 顺序查找（多个重复元素时可以返回全部索引）
if __name__ == '__main__':  # 防止函数被外部调用
    li = [1,2,3,4,5,5,5,5]
    element = 5
    t = time.perf_counter() # 计时精度高
    print(line_search(li,element,1))
    print(f'耗时：{time.perf_counter() - t:.8f}s')