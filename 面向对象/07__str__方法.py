# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 07__str__方法
class Cat:
    def __init__(self,name):# 对象创建时被自动调用
        # self.name =  属性的初始值
        self.name = name
        print(f"{self.name}来了")
    def __del__(self):# 对象销毁前被自动调用
        print(f"{self.name}离开了")
    def __str__(self):# 必须返回字符串
        return f"我是小猫{self.name}"
tom = Cat('Tom')
print(tom)