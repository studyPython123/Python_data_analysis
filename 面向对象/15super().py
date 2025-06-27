# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 15super()
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
    # def bark(self):print("哮天犬汪汪叫")
    def bark(self):
        # 针对子类需求编写
        print("神一样的叫唤...")
        # 使用super()调用父类中封装的方法
        super().bark()
        # 增加其他子类的代码
        print("335345235")
xiaotianquan = XiaoTianQuan()
xiaotianquan.eat()
xiaotianquan.drink()
xiaotianquan.run()
xiaotianquan.sleep()
xiaotianquan.fly()
xiaotianquan.bark()