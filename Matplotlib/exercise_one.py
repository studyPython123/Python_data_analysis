# Author: 邵世昌
# CreatTime: 2024/10/27
# FileName: exercise_one
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,4,3,3,1,1,1]
z = [1,0,3,1,2,2,3,3,2,2,1,1,1,1,1,1,1,1,1]
x= range(11,30)
plt.figure(figsize=(12,5),dpi=80)
plt.plot(x,y,'g',x,z,'r')
xtick_label = [f"{i}岁" for i in x]
plt.xlim(11,29)
plt.ylim(0,6)
plt.xticks(x,xtick_label)
plt.yticks(np.arange(0,6,1))
plt.xlabel("年龄")
plt.ylabel("男/女朋友数量")
plt.title("我和朋友不同年龄的男/女朋友数量对比情况")
plt.legend(["我的","朋友"],loc="upper right") # 图形标签
plt.grid() # 网格
plt.savefig('exercise_one.png')
plt.show()
