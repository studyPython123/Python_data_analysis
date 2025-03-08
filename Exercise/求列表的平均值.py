# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 求列表的平均值
#%%
def function(data):
    print(f"列表{data}的平均值是:{sum(data)/len(data):.2f}")
#%%
data = eval(input("请输入一个列表："))
function(data)
