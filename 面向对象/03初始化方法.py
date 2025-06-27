# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 03初始化方法
class Cat:
    def __init__(self):
        print("这是一个初始化方法")

if __name__ == '__main__':
    # 创建对象时会自动调用初始化方法
    tom = Cat()
