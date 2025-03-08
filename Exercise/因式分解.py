# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 因式分解
#%%
def function(x):
    t = x
    i = 2
    result =[]
    while True:
        if t == 1:
            break
        elif t % i == 0:
            result.append(i)
            t = t / i
        else:
            i += 1
    print(x,"=","*".join(map(str, result)))
#%%
x= eval(input("请输入一个小于 1000 的整数:"))
function(x)