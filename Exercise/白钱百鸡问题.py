# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 白钱百鸡问题
#%%
for x in range(0,20):
    for y in range(0,33):
        z = 100 - x -y
        if 5*x + 3*y + z /3 == 100:
            print(f"公鸡：{x}只，母鸡：{y}只，小鸡：{z}只")
