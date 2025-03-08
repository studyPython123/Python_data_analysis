# Author: 邵世昌
# CreatTime: 2024/10/28
# FileName: plt hist2
# %%绘制不等间隔的直方图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
interkal = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,477]
plt.figure(figsize=(12,6),dpi = 80)
p1 = plt.bar(range(12),quantity,width = 1)
plt.bar_label(p1,label_type = 'edge')
x = [i-0.5 for i in range(13)]
plt.xticks(x,interkal+[150])
plt.grid()
plt.savefig('bar to hist.png')
plt.show()