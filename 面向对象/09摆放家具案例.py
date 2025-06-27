# Author: 邵世昌
# CreateTime: 2025/3/30
# FileName: 09摆放家具案例
#%%创建家具类
class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return f'家具：{self.name}   占地： {self.area:.2f}平方米'

#%% 创建房子类
class House:
    def __init__(self,house_tpye,house_area):
        self.house_tpye = house_tpye
        self.house_area = house_area
        # 剩余面积
        self.free_area = house_area
        # 家具名称列表
        self.items = []
    def __str__(self):
        return (f'房型：{self.house_tpye}\n'
                      f'面积：{self.house_area:.2f}\n'
                      f'剩余面积：{self.free_area:.2f}\n'
                      f'已布置家具：{self.items}')
    def add_item(self,item): # item不需要self ，是外部引入的
        print(f"添加{item}")
        if item.area <= self.free_area:# 判断能否添加
            self.free_area = self.free_area - item.area
            self.items.append(item.name)
        else:
            print(f'{item.name}的占地面积{item.area}平方米大于剩余面积{self.free_area}平方米，无法添置')
            return

#%% 1创建家具
bed = HouseItem('床',40)
chest = HouseItem('衣柜',19)
table = HouseItem('餐桌',1.5)
print(chest)
print(bed)
print(table)

#%% 2创建房子对象
my_house = House("两室一厅",60)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)