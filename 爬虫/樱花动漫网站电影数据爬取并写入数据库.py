# Author: 邵世昌
# CreatTime: 2025/3/7
# FileName: 樱花动漫网站电影数据爬取并写入数据库
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
        CREATE TABLE IF NOT EXISTS 樱花动漫网动漫(
        id INT AUTO_INCREMENT,
        title VARCHAR(30) NOT NULL,
        score float DEFAULT 0,
        updates VARCHAR(200) DEFAULT NULL,
        primary key(id)
        )
'''
try:
    cursor.execute(sql_table_create)
except BaseException as e:
    print(e)
    cursor.execute('drop table if exists 樱花动漫网动漫')
    cursor.execute(sql_table_create)
sql_insert = 'insert into 樱花动漫网动漫(title, score, updates) values (%s, %s, %s)'
#%%
url = 'https://www.qdjybzjl.com/list/dongman_maoxian____.html'
response = requests.get(url, headers=header)
tree = etree.HTML(response.text)
title = tree.xpath('//*[@id="content"]/li/div/h5/a')
score = tree.xpath('//*[@id="content"]/li/a/span[2]')
updates = tree.xpath('//*[@id="content"]/li/a/span[3]')
for i in range(len(title)):
    row = (title[i].text, score[i].text, updates[i].text)
    print(row)
    cursor.execute(sql_insert, row)
    connect.commit()
cursor.close()
connect.close()
print('is over')