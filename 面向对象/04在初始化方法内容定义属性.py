# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 04在初始化方法内容定义属性
class Cat:
    def __init__(self,age):
        print("这是一个初始化方法")
        # self.name =  属性的初始值
        self.name = "Tom"
        self.age = age
tom = Cat(17)
print(tom.name)
print(tom.age)