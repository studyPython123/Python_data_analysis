# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 列表中绝对值最大的数据
def abs_max(list_):
    return max(list_,key = abs)
list_ = eval(input("请输入一个只有数值的列表："))
print(abs_max(list_))