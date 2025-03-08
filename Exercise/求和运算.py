# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 求和运算
import numpy as np
#%%
def function(a,n):
    list_num= []
    for i in range(1,n+1):
        b = str(a)*i
        print(b,end="\n")
        list_num.append(b)
    list_num = list(map(int,list_num))
    sum_num = sum(list_num)
    print(f"前{n}个数的和是：{sum_num}")
a = eval(input("请输入叠数的数值："))
n = eval(input("请输入求和项："))
function(4,5)
