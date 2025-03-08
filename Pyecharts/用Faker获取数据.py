# Author: 邵世昌
# CreatTime: 2024/11/12
# FileName: 用Faker获取数据
#%%导入库
from pyecharts.faker import Faker
#%%导入同属性的7个值
Faker.choose()
Faker.values()
print(Faker.cars) #随机的车
print(Faker.country)
print(Faker.days_attrs)
print(Faker.clock)#时钟列表