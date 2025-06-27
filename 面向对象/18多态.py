# Author: 邵世昌
# CreateTime: 2025/3/31
# FileName: 18多态
class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print(f"{self.name}在玩耍。。。")

class XiaoTianDog(Dog):
    def __init__(self,name):
        self.name = name
    def game(self):
        print(f"{self.name}在玩耍。。。")

class Person():
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print(f"{self.name}和{dog.name}玩耍")
        dog.game()

dog = Dog("普通的狗")
xiaotiandog = XiaoTianDog("哮天犬")
person = Person("小明")
person.game_with_dog(dog)
person.game_with_dog(xiaotiandog)