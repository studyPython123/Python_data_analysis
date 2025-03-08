# Author: 邵世昌
# CreateTime: 2024/2/22
# FileName: 电影网内地爱情电影数据爬取导入数据库
import mysql.connector
import pandas as pd
import requests
from lxml import etree
header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
connect = mysql.connector.connect(host='localhost', user='root', password='123wsssc123',
                                  database='爬虫数据',auth_plugin='mysql_native_password')
cursor = connect.cursor()
sq_table ='''
    create table if not exists 电影网内地爱情电影(
        title varchar(20),
        score varchar(5),
        brief varchar(30)
    );
'''
try:
    cursor.execute('drop table if exists 电影网内地爱情电影') # 清除旧表，防止数据重复
    cursor.execute(sq_table) # 创建新表
except BaseException as e:
    print(e)
sql_insert = 'insert into 电影网内地爱情电影(title, score, brief) values (%s, %s, %s)'

#%%爬取数据写入数据库
data = []
number = int(input("请输入需要爬取数据的页码："))
for item in range(1,number):
    url = f'https://www.1905.com/vod/list/n_1_t_1_a_1/o3p{item}.html'
    response = requests.get(url, headers=header)
    tree = etree.HTML(response.text)
    titles = tree.xpath('//*[@id="content"]/section/div/a/h3')
    scores1 = tree.xpath('//*[@id="content"]/section/div/a/i/b')
    scores2 = tree.xpath('//*[@id="content"]/section/div/a/i/text()')
    briefs = tree.xpath('//*[@id="content"]/section/div/a/p')
    for i in range(len(scores1)):
        row = (titles[i].text,scores1[i].text+scores2[i],briefs[i].text)
        data.append(row)
        cursor.execute(sql_insert, row)
        connect.commit() # 提交事务
cursor.close() # 关闭游标，释放资源
connect.close() # 关闭数据库
data = pd.DataFrame(data, columns=['title', 'score', 'brief'])
data.to_csv("电影网内地爱情电影.csv",index = False,encoding='utf_8_sig')
print("is over")
