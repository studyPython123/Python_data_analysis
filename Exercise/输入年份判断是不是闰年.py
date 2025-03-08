# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 输入年份判断是不是闰年
#%%函数
def function(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year}是闰年")
    else:
        print(f"{year} 是平年")
#%%执行
year = int(input("请输入一个年份："))
function(year)