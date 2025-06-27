# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 08面向对象封装案例
class Person(object):
    def __init__(self,name,height):
        self.name = name
        self.height = height
    def run(self):
        print(f"{self.name}跑步了，体重降低0.5公斤")
        self.height -= 0.5
        print(f"{self.name}小明的体重是{self.height:.2f}公斤")
    def eat(self):
        print(f"{self.name}吃东西了，体重增加1公斤")
        self.height += 1
        print(f"{self.name}小明的体重是{self.height:.2f}公斤")
    def __str__(self):
        return f"我的名字叫{self.name}，体重是{self.height:.2f}公斤"
if __name__ == '__main__':
    # 创建小明对象
    xiaoming = Person('小明',60)
    xiaoming.run()
    xiaoming.eat()
    print(xiaoming)
    # 创建小美对象
    xiaomei = Person('小美',45)
    xiaomei.run()
    xiaomei.eat()
    print(xiaomei)