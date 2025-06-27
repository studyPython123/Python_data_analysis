# Author: 邵世昌
# CreateTime: 2025/4/1
# FileName: 20静态方法
class Dog(object):
    @staticmethod # 静态方法
    def run():
        print("小狗跑跑跑...")
# 可以不创建对象
Dog.run()