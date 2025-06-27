# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 10士兵突击案例
#%% 枪类
class Gun():
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0 # 默认清空弹夹
    def add_bullet(self,count):
        if (self.bullet_count + count) <= 45:
            self.bullet_count += count
            print(f"装填子弹数量：{count}  弹夹子弹数量：{self.bullet_count}")
        else:
            print(f"装填子弹数量：{45-self.bullet_count}")
            self.bullet_count = 45
            print(f'弹夹子弹数量：{self.bullet_count}')
        print("-" * 20)
    def shoot(self):
        if self.bullet_count >= 1:
            self.bullet_count -= 1
            print(f"发射成功，子弹数量减1，当前弹夹子弹数量{self.bullet_count}")
        else:
            print(f"{self.model}弹夹内没有子弹，无法发射")
            return
        print("-" * 20)
    def __str__(self):
        return (f'型号：{self.model}\n'
                       f'弹夹子弹数量: {self.bullet_count}')

#%%
class Solider():
    def __init__(self,name):
        self.name = name
        self.gun = None # 新兵没有枪
    def fire(self):
        if self.gun is None:
            print(f"{self.name}没有枪")
            return
        print(f"冲冲冲...{self.name}")
        self.gun.shoot()
    def increasing_bullet(self,count):
        self.gun.add_bullet(count)

#%%创建枪对象
gun = Gun("AK47")
print(gun)
gun.add_bullet(50)
gun.shoot()

#%%
solider = Solider("许三多")
solider.gun = gun # 给许三多分发一支枪
print(solider.gun)
solider.fire()
solider.increasing_bullet(10)