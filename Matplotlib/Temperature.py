# Author: 邵世昌
# CreatTime: 2024/10/27
# FileName: Temperature
import matplotlib.pyplot as plt
import random as ra
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
x = range(0,120)
y = [ra.randint(20,35) for i in range(120)]
plt.figure(figsize=(12,5),dpi=80)
plt.plot(x,y,'g')
plt.xlabel('时间')
plt.ylabel('温度(℃)',rotation=90)
plt.title('10点-12点每分钟的温度变化情况')
plt.legend(["Temperature"],loc='upper right')
# xtick_labels = [f"10点{i}分" for i in range(60)]
# xtick_labels += [f"11点{i}分" for i in range(60)]
xtick_labels = [f"{int(i/60)+10}点{i % 60}分" for i in range(120)]
i = eval(input("请输入时间的显示间隔："))
plt.xticks(list(x)[::i],xtick_labels[::i],rotation=45)
plt.show()
