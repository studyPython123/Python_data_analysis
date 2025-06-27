# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 01定义一个简单的类
class Cat: # 定义类

    def eat(self): # 封装方法
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")
    def speak(self):
        print("小猫喵喵叫")

tom =   Cat() # 创建对象

# 调用方法
tom.eat()
tom.drink()
tom.speak()

print(tom) # 十六进制
addr  = id(tom)
print("%d" % addr) # 十进制