# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 求年龄
#%%
def age(n):
    if n == 1:
        age = 10
    else:
        age = 10+2*(n-1)
    return age
num = int(input("请输入人数："))
print(age(num))
