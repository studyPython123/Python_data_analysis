# Author: 邵世昌
# CreatTime: 2025/3/7
# FileName: 亚马逊数据爬取写入数据库
#%%
import requests
from lxml import etree
import mysql.connector
header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
connect = mysql.connector.connect(host='localhost',
                               user='root',password='123wsssc123',
                               database='爬虫数据',auth_plugin='mysql_native_password')
cursor = connect.cursor()
sql_table_create = '''
        CREATE TABLE IF NOT EXISTS 亚马逊_男生服装配饰组合(
        id INT AUTO_INCREMENT,
        title VARCHAR(200),
        score float DEFAULT 0,
        price double DEFAULT 0,
        other VARCHAR(200) DEFAULT NULL,
        primary key(id)
        )
'''
try:
    cursor.execute(sql_table_create)
except BaseException as e:
    print(e)
    cursor.execute('drop table if exists 亚马逊_男生服装配饰组合')
    cursor.execute(sql_table_create)
sql_insert = 'insert into 亚马逊_男生服装配饰组合(title, score, price,other) values (%s, %s, %s,%s)'
#%%
number = int(input("请输入你要爬取数据的页数："))
# for item in range(1,number):
url = 'https://www.amazon.com/-/zh/s?k=man+costume+accessories+set&page=2&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=1Y5IR8SUFQW30&qid=1741329452&sprefix=man+costumeaccessories+set%2Caps%2C312&xpid=4zxPvXPALLky8&ref=sr_pg_2'
response = requests.get(url,headers=header)
tree = etree.HTML(response.text)
title = tree.xpath('//*[@id="20516511-835c-4491-b55e-af537a76dcbd"]/div/div/span/div/div/div/div/a/h2/span/text()')
print(title)
score = tree.xpath('//*[@id="20516511-835c-4491-b55e-af537a76dcbd"]/div/div/span/div/div/div[2]/div[2]/div[1]/span[2]/div/a')
print(score)
price = tree.xpath('//*[@id="20516511-835c-4491-b55e-af537a76dcbd"]/div/div/span/div/div/div[2]/div[3]/div/div[1]/a/span/span')
print(price)

#%%
from bs4 import BeautifulSoup
import urllib.request #自带
response = urllib.request.urlopen(url)  # http 协议
html = response.read().decode('utf-8')  # 网页所有数据
soup = BeautifulSoup(html,'前端.parser')
lis = soup.select('ul[class="t clearfix"] > li')