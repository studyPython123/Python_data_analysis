# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 求两个列表中相同元素和不同元素
#%%
list1 = [1,2,3]
list2 = [3,5,6]
set1 = set(list1)
set2 = set(list2)
print(f"{list1}和{list2}的相同元素是：{set1&set2}")
print(f"{list1}和{list2}的不同元素是：{set1^set2}")