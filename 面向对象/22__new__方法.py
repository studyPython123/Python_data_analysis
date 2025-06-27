# Author: 邵世昌
# CreateTime: 2025/4/1
# FileName: 22__new__方法
class MusicPlayer(object):
    def __new__(cls, *args, **kwargs): # 静态方法
        print("创建方法，分配空间")
        instance =  super().__new__(cls) # 分配空间
        return instance # 返回对象的引用

    def __init__(self):
        print("播放器初始化")

player = MusicPlayer()
print(player)