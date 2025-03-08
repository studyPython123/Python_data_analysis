# Author: 邵世昌
# CreatTime: 2024/11/10
# FileName: 实例和实例方法的构建
#%%
class Basic:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        return self.a +self.b
#%%
num = Basic(1,2)
print(num.a,num.b,num.sum)


