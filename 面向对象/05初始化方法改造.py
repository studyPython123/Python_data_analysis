# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 05初始化方法改造
class Cat:
    def __init__(self,name):# 初始化参数
        print("这是一个初始化方法")
        # self.name =  属性的初始值
        self.name = name
    def eat(self):
        print(f"{self.name}爱吃鱼")
tom = Cat("tom")
print(tom.name)

lazy_cat =  Cat("大懒猫")
lazy_cat.eat()