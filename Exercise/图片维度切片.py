# Author: 邵世昌
# CreatTime: 2024/11/11
# FileName: 图片维度切片
#%%
import matplotlib.pyplot as plt
#%%导入图片
rose = plt.imread('rose2.jpg')
print(rose.shape)
#%%显示原图
plt.subplot(2,2,1)
plt.imshow(rose)
plt.axis("off")
plt.show()
#%%换为蓝色
plt.subplot(2,2,2)
plt.imshow(rose[:,:,[2,1,0]])
plt.axis("off")
plt.show()
#%%换为绿色
plt.subplot(2,1,2)
plt.imshow(rose[:,:,[1,0,2]])
plt.axis("off")
plt.show()
plt.savefig('rose-change.png')