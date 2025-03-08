# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 得到新列表
#%%
def function(list_):
    length = [len(str(i)) for i in list_]
    print(length)
#%%
list_ = eval(input("请输入一个列表："))
function(list_)