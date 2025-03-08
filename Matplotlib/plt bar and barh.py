# Author: 邵世昌
# CreatTime: 2024/10/28
# FileName: plt bar and barh
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
a = ["战狼2","速度与漖情8","功夫瑜伽","西游伏妖篇","变形金刚5:最后的骑士","摔跤吧!爸爸","加勒比海盗5-死无对证","金刚:骷毂岛","极限特工:极回归","生化危机6:终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3:殊死一战","蝴蛛侠:英雄归来","悟空传","银河护卫队2","情圣","新木乃伊"]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,5.23]
plt.figure(figsize=(10,6),dpi=80)
p1 = plt.barh(a,b,label = "票房",align='center',color = 'orange')
plt.bar_label(p1, label_type='center')
plt.title("20部电影的票房对比情况")
plt.legend()
plt.savefig("barh-movie-20.png")
plt.show()