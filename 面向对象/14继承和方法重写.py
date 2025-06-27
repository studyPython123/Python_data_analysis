# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 14继承和方法重写
class Animal:
    def eat(self): print("吃")
    def drink(self): print("喝")
    def run(self):  print("跑")
    def sleep(self): print("睡")


class Dog(Animal): # 继承Animal的方法
    def bark(self): print("叫")


class XiaoTianQuan(Dog):
    def fly(self): print("哮天犬飞")
    #方法重写
    def bark(self):print("哮天犬汪汪叫")
xiaotianquan = XiaoTianQuan()
xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.fly()
xiaotianquan.bark()