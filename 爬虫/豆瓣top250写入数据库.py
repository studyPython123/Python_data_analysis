# Author: 邵世昌
# CreatTime: 2024/11/22
# FileName: 豆瓣top250写入数据库
#%%
import mysql.connector
import requests
from lxml import etree
import pandas as pd
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
name_list = []
score_list = []
dianzan_list = []
category_list = []
connect = mysql.connector.connect(host='localhost',
                                       user='root', password='123wsssc123',
                                       auth_plugin='mysql_native_password', database='爬虫数据')
cursor = connect.cursor()
sql_table = '''
    create table if not exists top250(
        name varchar(30),
        score varchar(5),
        dianzan varchar(10)
    );
'''
try:
    cursor.execute(sql_table)
except BaseException as e:
    print(e)  # 报错
    cursor.execute('drop table top250;')
    cursor.execute(sql_table)
sql_insert = 'insert into top2501(name, score, dianzan) values (%s, %s, %s);'
for number in range(0,250,25):
    utl = f'https://movie.douban.com/top250?start={number}'
    response = requests.get(utl, headers=header)
    tree = etree.HTML(response.text)
    #%%名称
    names = tree.xpath('//*[@id="content"]/div/div/ol/li/div/div/div/a/span[1]')
    scores = tree.xpath('//*[@id="content"]/div/div/ol/li/div/div/div/div/span[2]')
    dianzans = tree.xpath('//*[@id="content"]/div/div/ol/li/div/div/div/div/span[4]')
    # categories = tree.xpath('//span[@class="inq"]')
    # categories = tree.xpath('//*[@id="content"]/div/div/ol/li/div/div/div/p[2]/span')
    for i in range(len(names)):
        data = (names[i].text,scores[i].text,dianzans[i].text.rstrip("人评价"))
        cursor.execute(sql_insert, data)
        connect.commit()
        # name_list.append(names[i].text)
        # score_list.append(scores[i].text)
        # dianzan_list.append(dianzans[i].text.rstrip("人评价"))
    # for i in range(len(categories)):
    #     category_list.append(categories[i].text)
cursor.close()
connect.close()
print('is over')
#%%
# name_list = pd.DataFrame(name_list,columns=['视频名称'])
# score_list = pd.DataFrame(score_list,columns=['评分'])
# dianzan_list = pd.DataFrame(dianzan_list,columns=['评价数量'])
# category_list = pd.DataFrame(category_list,columns=['类别'])#有缺失对不齐
# data = pd.concat([name_list, score_list, dianzan_list, category_list],axis=1)
# data.to_csv("豆瓣top250.csv",encoding="utf_8_sig")
