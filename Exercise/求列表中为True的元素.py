# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 求列表中为True的元素
def is_Ture(list_):
    ture = [item for item in list_  if bool(item)==True]
    return ture
list_ = [1,2,3,0,'','a',False]
print(is_Ture(list_))