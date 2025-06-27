# Author: 邵世昌
# CreateTime: 2025/3/29
# FileName: test
# 定义一个类
class Car:
    # 类属性
    wheels = 4

    # 构造方法
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # 实例方法：加速
    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.make} {self.model} 加速到 {self.speed} 公里/小时")

    # 实例方法：减速
    def brake(self, decrement):
        if self.speed - decrement < 0:
            self.speed = 0
        else:
            self.speed -= decrement
        print(f"{self.make} {self.model} 减速到 {self.speed} 公里/小时")

    # 类方法
    @classmethod
    def get_wheels(cls):
        return cls.wheels

    # 静态方法
    @staticmethod
    def is_sedan(model):
        sedans = ['Accord', 'Camry']
        return model in sedans
if __name__ == '__main__':
    # 创建 Car 类的实例
    my_car = Car('Toyota', 'Camry', 2022)
    # 调用实例方法
    my_car.accelerate(5)
    my_car.brake(10)
    # 调用类方法
    print(f"汽车有 {Car.get_wheels()} 个轮子")
    # 调用静态方法
    print(f"{my_car.model} 是轿车吗？ {Car.is_sedan(my_car.model)}")
