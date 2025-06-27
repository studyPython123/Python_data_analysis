# Author: 邵世昌
# CreateTime: 2025/4/1
# FileName: 19定义类方法
class Tool(object):
    count = 0
    @classmethod # 装饰器
    def show_tool_count(cls):# 类方法
        print(cls.count)
    def __init__(self,name):
        self.name = name
        Tool.count += 1
tool1 = Tool("1")
tool2 = Tool("2")
# tool3 = Tool("3")
Tool.show_tool_count()