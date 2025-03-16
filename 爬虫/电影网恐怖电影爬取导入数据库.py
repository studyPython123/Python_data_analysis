# Author: 邵世昌
# CreatTime: 2024/11/22
# FileName: 电影网恐怖电影爬取导入数据库
import mysql.connector
import requests
from lxml import etree
header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
title_list = []
score_list = []
brief_list = []
number = int(input("请输入要导入的页码数："))
connect = mysql.connector.connect(host='localhost', user='root', password='123wsssc123',
                                  database='爬虫数据', auth_plugin='mysql_native_password') # auth_plugin必须加
cursor = connect.cursor()
sql_table = '''
    create table if not exists 电影网恐怖电影(
        title varchar(20),
        score varchar(5),
        brief varchar(30)
    );
'''
try:
    cursor.execute(sql_table)
except BaseException as e:
    print(e)
    cursor.execute('drop table if exists 电影网恐怖电影')
    cursor.execute(sql_table)
sql_insert = 'insert into 电影网恐怖电影(title, score, brief) values (%s, %s, %s)'
for item in range(1,number):
    url = f'https://www.1905.com/vod/list/n_1_t_17/o3p{item}.html'
    response = requests.get(url, headers=header)
    tree = etree.HTML(response.text)
    titles = tree.xpath('//*[@id="content"]/section/div/a/h3')
    scores1 = tree.xpath('//*[@id="content"]/section/div/a/i/b')
    scores2 = tree.xpath('//*[@id="content"]/section/div/a/i/text()')
    briefs = tree.xpath('//*[@id="content"]/section/div/a/p')
    for i in range(len(scores1)):
        data = (titles[i].text,scores1[i].text+scores2[i],briefs[i].text) # 元组形式
        cursor.execute(sql_insert, data)
        connect.commit() # 一定要提交内容
cursor.close() # 关闭游标
connect.close() # 一定要关闭连接
print('数据爬取完成，已成功导入数据库')
    # for title in titles:
    #     title_list.append(title.text)
        # print(title.text)
        # score_list.append(scores1[i].text+scores2[i])
    # for brief in briefs:
        # brief_list.append(brief.text)
        # print(brief.text)
# import pandas as pd
# title_list = pd.DataFrame(title_list,columns=['title'])
# score_list = pd.DataFrame(score_list,columns=['score'])
# brief_list = pd.DataFrame(brief_list,columns=['brief'])
# data = pd.concat([title_list,score_list,brief_list],axis=1)
# data.to_csv("电影网恐怖电影数据爬取.csv",index=False,encoding="utf_8_sig")
# print("is over")