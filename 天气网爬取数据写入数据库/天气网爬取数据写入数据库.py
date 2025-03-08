# Author: 邵世昌
# CreateTime: 2024/2/22
# FileName: 天气网爬取数据写入数据库
#%%
import urllib.request
import mysql.connector
from bs4 import BeautifulSoup
import pandas as pd
header ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
city_code = {
    '北京': '101010100',
    '上海': '101020100',
    '广州': '101280101',
    '深圳': '101280601',
    '成都':'101270101',
    '杭州':'101210101'
}
#%% 连接数据库
connect = mysql.connector.connect(host='localhost',
                                       user='root', password='123wsssc123',
                                       auth_plugin='mysql_native_password', database='mydataset1')
cursor = connect.cursor()
sql_table = '''
    create table weather_table1 (
        city varchar(20),
        date varchar(20),
        wea varchar(20),
        tem varchar(20),
        win varchar(20),
        primary key (city,date)
    );
'''
try:
    cursor.execute('drop table if exists weather_table1;')
    cursor.execute(sql_table)
except BaseException as e:
    print(e)  # 报错
sql = 'insert into weather_table1 (city,date,wea,tem,win) values (%s,%s,%s,%s,%s);'

#%%爬取数据写入数据库
data = []
for city in city_code.keys():
    url = f'https://www.weather.com.cn/weather/{city_code[city]}.shtml'
    response = urllib.request.urlopen(url) # http 协议
    html = response.read().decode('utf-8') # 网页所有数据
    # 解析需要的数据-转换为文档树结果
    soup = BeautifulSoup(html,'html.parser')
    lis = soup.select('ul[class="t clearfix"] > li')
    for li in lis:
        date = li.select("h1")[0].text.strip()
        wea = li.select('p[class="wea"]')[0].text.strip()
        tem = li.select('p[class="tem"]')[0].text.strip()
        win = li.select('p[class="win"]')[0].text.strip()
        row = (city, date, wea, tem, win)
        data.append(row)
        cursor.execute(sql,row)
        connect.commit() # 提交数据
cursor.close()
connect.close()
data = pd.DataFrame(data,columns=['city','date','wea','tem','win'])
data.to_csv("天气网数据.csv",index=False,encoding='utf_8_sig')
print('is over')

