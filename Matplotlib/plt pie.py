# Author: 邵世昌
# CreatTime: 2024/10/29
# FileName: plt pie
#%%
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
labels = ['苹果', '香蕉', '橙子', '草莓', '葡萄']
sizes = [30, 25, 20, 15, 10]
explode = (0.1, 0, 0, 0, 0)  # 让“苹果”这一块突出，值越大，突出越远
plt.pie(sizes, labels=labels, autopct='%1.1f%%',explode=explode)
plt.legend( loc='upper right')
plt.axis('equal')  # 让饼图为圆形
plt.savefig('pie.png')
plt.show()
