# Author: 邵世昌
# CreatTime: 2024/11/3
# FileName: 直方图控制坐标的四种方法
#%%方法1
import matplotlib.pyplot as plt
import numpy as np
# 生成示例数据
data = np.random.randn(1000)
# 绘制直方图，设置柱子的宽度
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black', width=0.8)
plt.title('直方图示例')
plt.xlabel('数值区间')
plt.ylabel('频数')

plt.show()
#%%方法2：使用 align 参数
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black', align='mid')

#%%方3：调整 x 轴的刻度
bins = np.linspace(-3, 3, 31)  # 自定义区间
plt.hist(data, bins=bins, alpha=0.7, color='blue', edgecolor='black')
# 设置自定义 x 轴刻度
plt.xticks(bins, rotation=45)
plt.show()

#%%方法4：使用 numpy.histogram() 函数
data = np.random.randn(1000)
counts, bins = np.histogram(data, bins=30)
# 绘制直方图
plt.bar(bins[:-1], counts, width=np.diff(bins), edgecolor='black', align='edge', alpha=0.7)
plt.title('直方图示例')
plt.xlabel('数值区间')
plt.ylabel('频数')
plt.show()


