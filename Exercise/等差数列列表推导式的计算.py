# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 等差数列列表推导式的计算
def function(n,gaps):
    lis = [1+gaps*n for n in range(n)]
    return lis
print(function(5,20))