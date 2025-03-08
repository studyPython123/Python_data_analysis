# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 按要求输出1000以内的数
def function():
    result = []
    for i in range(2,1001):
        if i%3==2 and i%5==2 and i%7 ==2:
            result.append(i)
    return result
print(function())
