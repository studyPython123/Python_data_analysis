# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 求前n阶乘的和
#%%
def function(n):
    s = 0
    for temp in range(1,n+1):
        t = 1
        for i in range(1,temp+1):
            t *= i
        s += t
    print(f"前{n}阶乘的和是：{s}")
n = int(input("请输入项数：n = "))
function(n)
#%%
def function2(n):
    s = 0
    t = 1
    for i in range(1,n+1):
        t *= i
        s += t
    print(f"前{n}阶乘的和是：{s}")
n = int(input("请输入项数：n = "))
function(n)

