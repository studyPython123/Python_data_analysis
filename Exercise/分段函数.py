# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 分段函数
#%%
def function(x):
    if x < 0:
        y = 0
    elif x < 5:
        y = x
    elif x <10:
        y = 3*x - 5
    elif x < 20:
        y = 0.5*x - 2
    else:
        y = 0
    print(f"计算得y ={y}")
#%%
x = eval(input("请输入一个数："))
function(x)

