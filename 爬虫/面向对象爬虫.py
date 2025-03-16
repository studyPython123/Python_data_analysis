# Author: 邵世昌
# CreatTime: 2024/11/22
# FileName: 面向对象爬虫
import urllib.request #自带
import mysql.connector
from bs4 import BeautifulSoup
#%% 定义一个Weather类
class Weather(object):
    def __init__(self,city,date,wea,tem,win):
        print('Weather正在初始化.....')
        self.city = city
        self.date = date
        self.wea = wea
        self.tem = tem
        self.win = win
    def __str__(self):
        return f'Weather [{self.city = },{self.date = },{self.wea = },{self.tem = },{self.win = }]'
    def __del__(self):
        print('Weather正在销毁......')

#%%创建一个WeatherForcastDB类
class WeatherForcastDB(object):
    def __init__(self):
        print('WeatherForcastDB正在初始化.....')
        # 1、创建数据库
        self.connect = mysql.connector.connect(host='localhost',
                                       user='root',password='123wsssc123',
                                       auth_plugin='mysql_native_password')
        # 获取cursor对象
        self.cursor = self.connect.cursor()
        sql_db = 'create database if not exists weather_database;'
        self.cursor.execute(sql_db)
        # 2、创建数据表
        # 切换到对应数据库
        self.cursor.execute('use weather_database;')
        sql_table = '''
            create table weather_table (
                city varchar(20),
                date varchar(20),
                wea varchar(20),
                tem varchar(20),
                win varchar(20),
                primary key (city,date)
            );
        '''
        try:
            self.cursor.execute(sql_table)
        except BaseException as e:
            print(e) # 报错
            self.cursor.execute('drop table weather_table;')
            self.cursor.execute(sql_table)
    # 插入数据行为
    def insertWeather(self,weather):
        print(f'正在将{weather}插入到数据库当中........')
        # 编写插入的sql语句
        sql = 'insert into weather_table (city,date,wea,tem,win) values (%s,%s,%s,%s,%s);'
        values = (weather.city,weather.date,weather.wea,weather.tem,weather.win)# 元组类型
        self.cursor.execute(sql,values)
        # 增删改后要提交
        self.connect.commit()
    # 查询所有数据
    def query_weather(self):
        print('正在执行数据库查询......')
        sql_query = 'select * from weather_table;'
        self.cursor.execute(sql_query)
        result_set = self.cursor.fetchall()
        weather_list = []
        for row in result_set:
            city,date,wea,tem,win = row
            # 封装数据对象
            weather = Weather(city,date,wea,tem,win)
            weather_list.append(weather)
        # 最后将数据表返回
        return weather_list
    def __del__(self):
        print('WeatherForcastDB正在销毁......')
        # 释放与数据库相关的资源
        self.cursor.close()
        self.connect.close()
#%%创建WeatherForcast类
class WeatherForcast(object):
    #初始化
    def __init__(self):
        print('WeatherForcast正在初始化......')
        # 天气预报数据库对象
        self.weather_forcast_db = WeatherForcastDB()
        # 城市的代码
        self.city_code = {
            '北京':'101010100',
            '上海': '101020100',
            '广州': '101280101',
            '深圳': '101280601'
        }
    # 查询行为
    def city(self,city):
        print(f'WeatherForcast 正在 查询{city}的提取数据......')
        if city not in self.city_code:
            print(f"根据{city}查询不到对应的城市代码")
            return
        # 有城市才会执行
        city_code = self.city_code[city]
        url = f'https://www.weather.com.cn/weather/{city_code}.shtml'
        response = urllib.request.urlopen(url)  # http 协议
        html = response.read().decode('utf-8')  # 网页所有数据
        soup = BeautifulSoup(html, '前端.parser')
        lis = soup.select('ul[class="t clearfix"] > li')
        for li in lis:
            date = li.select("h1")[0].text.strip()
            wea = li.select('p[class="wea"]')[0].text.strip()
            tem = li.select('p[class="tem"]')[0].text.strip()
            win = li.select('p[class="win"]')[0].text.strip()
            # 将获取的数据封装为weather对象模型
            weather = Weather(city, date, wea, tem, win)
            # 将查询的数据保存到数据库当中
            self.weather_forcast_db.insertWeather(weather)
        # 数据库
    # 查询行为
    def query_all(self):
        # 查询数据并接收数据
        weather_list = self.weather_forcast_db.query_weather()
        for weather in weather_list:
            print(weather)
    # 析构
    def __del__(self):
        print('WeatherForcast正在销毁......')
# 主方法
if __name__ == '__main__':
    #1、创建天气预报对象
    Weather_forcast = WeatherForcast()
    #2、定义获取城市的列表
    cities = ['北京','上海','广州','深圳','新疆']
    for city in cities:
        Weather_forcast.city(city)
    # 3、遍历城市天气数据
    Weather_forcast.query_all()