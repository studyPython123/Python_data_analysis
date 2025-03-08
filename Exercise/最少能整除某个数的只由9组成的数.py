# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 最少能整除某个数的只由9组成的数
def function(num,b_num):
    while num%b_num != 0:
        num = num*10+9
    return num
print(function(9,13))