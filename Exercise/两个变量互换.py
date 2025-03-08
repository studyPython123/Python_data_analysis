# Author: 邵世昌
# CreatTime: 2024/11/14
# FileName: 两个变量互换
def change(str1,str2):
    str1,str2 = str2,str1
    print(str1,str2)
change(123,456)