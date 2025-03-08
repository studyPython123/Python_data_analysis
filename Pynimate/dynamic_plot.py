# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: dynamic_plot
import matplotlib.pyplot as plt
import numpy as np
import time
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
"""
     绘制动态图
"""
plt.ion()
t0 = time.time()#程序启动时间
while True:
    plt.clf()#清空上一行显示
    plt.subplot(1,2,1)
    plt.title("曲线图")
    plt.xlabel("时间（s）")
    plt.ylabel("数量")
    plt.ylim(-2,2)
    #绘图
    t = time.time() - t0
    x = np.arange(t,t+8,0.1)
    y1= np.sin(x)
    y2= np.sin(x*3)/3
    y3= np.sin(x*5)/5
    y4= np.sin(x*7)/7
    """
    开始绘制
    """
    plt.plot(x,y1,color="red",linestyle = ':',label="y= np.sin(x)/1")
    plt.plot(x, y2, color="b",linestyle = ':', label="y= np.sin(3x)/3")
    plt.plot(x, y3, color="y",linestyle = ':', label="y= np.sin(5x)/5")
    plt.plot(x, y4, color="g",linestyle = ':', label="y= np.sin(7x)/7")
    plt.legend(loc = "upper right")

    plt.subplot(1,2,2)
    y5 = y1+y2+y3+y4
    plt.plot(x,y5,color='orange',linestyle = ':',label="叠加信号")
    plt.legend(loc = "upper right")
    plt.pause(0.05)

