# Author: 邵世昌
# CreatTime: 2024/10/28
# FileName: plt scatter
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
y_1 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_2 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x_1 = range(1,32)
x_2 = range(41,72)
plt.figure(figsize=(12,5),dpi=80)
plt.scatter(x_1,y_1,c='r',label="3月份")
plt.scatter(x_2,y_2,c='g',label="10月份")
x= list(x_1)+list(x_2)
xtick_label = [f"3月{i}号" for i in x_1 ] + [f"10月{i-40}号" for i in x_2 ]
plt.xticks(x[::2],xtick_label[::2],rotation=45)
#%%描述信息
plt.title("3月份和10月份的气温变化情况")
plt.legend(loc='upper right')
plt.xlabel("日期")
plt.ylabel("温度")
plt.savefig("scatter.png")
plt.show()