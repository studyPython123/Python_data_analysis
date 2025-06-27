# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 11私有属性和私有方法
class Women:
    def __init__(self,name):
        self.name = name
        self.__age = 18 # 私有属性不能被外部访问
    def __secret(self): # 私有方法不能被外部访问
        print(f"{self.name} is {self.__age} years old")
    def secret(self):
        self.__secret()
xiaofang = Women("xiaofang")
print(xiaofang.__age)
xiaofang.__secret()
xiaofang.secret()