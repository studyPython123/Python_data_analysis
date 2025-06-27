# Author: 邵世昌
# CreateTime: 2025/4/1
# FileName: 21方法综合案例
class Game():
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod # 静态方法
    def show_help():
        print("帮助信息：让僵尸进入大门")
    @classmethod # 类方法
    def show_top_score(cls):
        print(f"历史最高分是{cls.top_score}")
    def start_game(self): # 实例方法
        print(f"{self.player_name}开始游戏了")

# 1、查看游戏帮助信息
Game.show_help()

#2、查看历史最高得分
Game.show_top_score()

#3、创建游戏对象
game = Game("小明")
game.start_game()
