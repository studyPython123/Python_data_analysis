# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 某个数内偶数求和和奇数求和
#%%
def function(num):
    sum_2 = 0
    sum_1 = 0
    for temp in range(1,num+1):
        if temp % 2 == 0:
            sum_2 += temp
        else:
            sum_1 += temp
    print(f"前{num}数的偶数和是：{sum_2}\n前{num}项的奇数和是：{sum_1}")
#%%
num = int(input("请输入一个整数："))
function(num)