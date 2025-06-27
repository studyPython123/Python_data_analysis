# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 02创建两个猫对象
class Cat: # 定义类

    def eat(self): # 封装方法
        print(f"{self.name}爱吃鱼")
    def drink(self):
        print("小猫要喝水")
    def speak(self):
        print("小猫喵喵叫")

tom =   Cat() # 创建对象
#%% 添加属性
tom.name = "小白" # 不推荐该方法
# 调用方法
tom.eat()
tom.drink()
tom.speak()

#%%
lazy_cat = Cat()
lazy_cat.name = '大懒猫'
lazy_cat.eat()
lazy_cat.drink()
lazy_cat.speak()
lazy_cat2 = lazy_cat # 拷贝
