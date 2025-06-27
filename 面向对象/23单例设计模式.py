# Author: 邵世昌
# CreateTime: 2025/4/1
# FileName: 23单例设计模式
class MusicPlayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        # 1、判断类属性是否是空对象
        if cls.instance is None:
            # 2、调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3、返回类属性保存的对象引用
        return cls.instance
    init_flag = False # 记录是否执行过初始化动作
    def __init__(self):
        if self.init_flag:
            return
        print("初始化播放器")
        self.init_flag = True
musicplayer1 = MusicPlayer()
musicplayer2 = MusicPlayer()
print(musicplayer1,'\n', musicplayer2) # 内存地址是一样的
