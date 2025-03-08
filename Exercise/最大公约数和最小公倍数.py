# Author: 邵世昌
# CreatTime: 2024/11/9
# FileName: 最大公约数和最小公倍数
import numpy as np
x = eval(input("x = "))
y = eval(input("y = "))
list = [x,y]
min = np.min(list)
for i in range(x,0,-1):
    if x % i ==0 & y%i == 0:
        print(f"{x}和{y}的最大公约数是：{i}")
        print(f"{x}和{y}的最小公倍数数是：{x*y // i}")
        break
