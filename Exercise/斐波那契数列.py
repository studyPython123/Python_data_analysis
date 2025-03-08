# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 斐波那契数列
def feibonaqi(n):
    a  = b =1
    list = [a,b]
    for i in range(n-2):
        temp = a
        a = b
        b = temp + b
        list.append(b)
    return list
num = eval(input("请输入需要打印的斐波那契数列的数据个数："))
print(feibonaqi(num))

