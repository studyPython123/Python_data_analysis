# Author: 邵世昌
# CreatTime: 2024/10/27
# FileName: 折线图
import matplotlib.pyplot as plt
import numpy as np
#%%显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
#%%主代码
x = np.linspace(0,50,10000)
y = np.sin(x)
# 设置图片大小
plt.figure(figsize=(12,5),dpi=80)
#%%坐标轴设置
# 设置x轴范围
plt.xlim(1,50)
# 设置y轴的范围
plt.ylim(-1,1)
# 设置x轴刻度间隔
plt.xticks(np.arange(0, 50, 2))
# 设置y轴刻度间隔
plt.yticks(np.arange(-1, 1, 0.1))
#%%绘图
plt.plot(x,y,color='g')
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin(x)")
plt.legend(["sin(x)折线图"],loc="upper right")
# 设置数字标签
# for a, b in zip(x, y):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
#%%保存图片
# 保存图片为jpg格式
# plt.savefig("折线图.jpg")
# 矢量图格式保存图片
# plt.savefig("折线图.svg")
# 显示图片
plt.show()
