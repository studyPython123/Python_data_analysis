# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 翻转数字
#%%
def function(num):
    num_str = str(num)
    if int(num_str[-1]) % 2 == 0:
        print("个位数为偶数，直接输出：",num)
    else:
        if num < 0:
            num_str = num_str[1:]
            print("个位数为奇数，逆序输出：",int(num_str[::-1])*(-1))
        else:
            print("个位数为奇数，逆序输出：",int(num_str[::-1]))
num = int(input("请输入一个数："))
function(num)