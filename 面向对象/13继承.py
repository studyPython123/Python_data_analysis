# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 13继承
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")
wangcai = Animal()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()

#%%创建狗类
class Dog(Animal): # 继承Animal的方法
    def bark(self):
        print("叫")
xiaobai = Dog()
xiaobai.bark()
xiaobai.run()
xiaobai.sleep()
xiaobai.drink()
xiaobai.eat()

#%%创建猫类
class Cat(Animal):
    def catch(self):
        print("喵喵叫")
xiaomao = Cat()
xiaomao.run()
xiaomao.sleep()
xiaomao.drink()
xiaomao.eat()

#%%哮天犬类
class XiaoTianQuan(Dog):
    def fly(self): print("哮天犬飞")
xiaotianquan = XiaoTianQuan()
xiaotianquan.bark()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.drink()
xiaotianquan.eat()
xiaotianquan.fly()