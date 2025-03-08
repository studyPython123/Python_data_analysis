# Author: 邵世昌
# CreatTime: 2024/10/28
# FileName: plt bar
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
a = ["猩球眼起3:终极之战","敦刻尔克","蛛快:英雄归来","战狼2"]
b_14 = [2358,399,2358,362]
b_15 = [12357,156,2045,168]
b_16 = [15746,312,4497,319]
plt.figure(figsize=(12,5),dpi=80)
bar_width = 0.2  # 条形宽度
index_b_14 = np.arange(len(a))  # b_14条形图的横坐标
index_b_15 = index_b_14 + bar_width  # b_15条形图的横坐标
index_b_16 = index_b_15 + bar_width # b_15条形图的横坐标
p1 = plt.bar(index_b_14,b_14,width=bar_width,label="2017-09-17",color="orange")
p2 = plt.bar(index_b_15,b_15,width=bar_width,label="2017-09-18",color="yellow")
p3 = plt.bar(index_b_16,b_16,width=bar_width,label="2017-09-19",color="green")
#%%数值标签
plt.bar_label(p1, label_type='edge')
plt.bar_label(p2, label_type='edge')
plt.bar_label(p3, label_type='edge')
#%%
plt.legend()  # 显示图例
plt.xticks(index_b_14 + bar_width/3, a)  # 让横坐标轴刻度显示 a 里的电影名，index_b_14 + bar_width/3 为横坐标轴刻度的位置
plt.xlabel("电影名")
plt.ylabel('票房')  # 纵坐标轴标题
plt.title('2017/09/14-2017/09/16三日4部电影的票房情况对比')  # 图形标题
plt.legend(loc="upper right")
plt.savefig('side-by-side-bar.png')
plt.show()



