# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 求内积
import  numpy as np
def function(list1,list2):
    return np.dot(list1,list2) #求内积
list1 = [1,2,3]
list2 = [4,5,6]
print(function(list1,list2))

def function2(list1,list2):
    t = 0
    for i in range(len(list1)):
        t = t + (list1[i] * list2[i])
    return t
print(function2(list1,list2))