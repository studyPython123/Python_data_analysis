# Author: 邵世昌
# CreatTime: 2025/3/7
# FileName: 哪吒2之魔童脑海影评爬取写入数据库
import requests
from lxml import etree
import mysql.connector
header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
conn = mysql.connector.connect(host='localhost', user='root', password='123wsssc123',
                               database='爬虫数据',auth_plugin='mysql_native_password')
cursor = conn.cursor()
mysql_table_create = '''
    CREATE TABLE IF NOT EXISTS 哪吒2之魔童脑海影评(
    id INT PRIMARY key AUTO_INCREMENT,
    author_name VARCHAR(100),
    lookling_or_not VARCHAR(10),
    evaluate_time VARCHAR(30) NOT NULL,
    region VARCHAR(10),
    likes INT,
    content VARCHAR(1000)
    )
'''
try:
    cursor.execute(mysql_table_create)
except BaseException as e:
    print(e)
    cursor.execute('drop table if exists 哪吒2之魔童脑海影评')
    cursor.execute(mysql_table_create)
mysql_insert = '''INSERT INTO 哪吒2之魔童脑海影评(author_name,lookling_or_not,evaluate_time,region,likes,content) values(%s, %s, %s, %s,%s,%s)'''
#%%
data = []
number = int(input("请输入想要获取的评论数："))
for item in range(0,number,20):
    url = f'https://movie.douban.com/subject/34780991/comments?start={item}&limit=20&status=P&sort=new_score'
    response = requests.get(url, headers=header)
    tree = etree.HTML(response.text)
    # -------------------------------------------------------------------------------------------------------
    author_name = tree.xpath('/前端/body/div/div/div/div/div/div/div/h3/span[2]/a')
    # for i in range(len(author_name)):
    #     print(author_name[i].text.strip())
    # ------------------------------------------------------------------------------------------------------
    lookling_or_not = tree.xpath('/前端/body/div/div/div/div/div/div/div/h3/span[2]/span[1]')
    # for i in range(len(lookling_or_not)):
    #     print(lookling_or_not[i].text.strip())
    # -------------------------------------------------------------------------------------------------------
    evaluate = tree.xpath('/前端/body/div/div/div/div/div/div/div/h3/span/span[2]/text()')
    # for i in range(len(evaluate)):
    #     print(evaluate[i].text.strip())
    # -------------------------------------------------------------------------------------------------------
    evaluate_time = tree.xpath('//*[@id="comments"]/div/div/h3/span/span[3]')
    # for i in range(len(evaluate_time)):
    #     print(evaluate_time[i].text.strip())
    # -------------------------------------------------------------------------------------------------------
    region = tree.xpath('//*[@id="comments"]/div/div/h3/span/span[4]')
    # for i in range(len(region)):
    #     print(region[i].text.strip())
    # -------------------------------------------------------------------------------------------------------
    likes = tree.xpath('/前端/body/div/div/div/div/div/div/div/h3/span[1]/span[1]')
    # print(len(likes))
    # for i in range(len(likes)):
    #     print(likes[i].text.strip())
    # -------------------------------------------------------------------------------------------------------
    content = tree.xpath('//*[@id="comments"]/div/div/p/span')
    # print(len(author_name))
    # for i in range(len(content)):
    #     print(content[i].text.strip())
    for i in range(len(author_name)):
        # print(author_name[i].text)
        try:
            row = (
                        author_name[i].text.strip(),lookling_or_not[i].text.strip(),evaluate_time[i].text.strip(),
                        region[i].text.strip(),likes[i].text.strip(),content[i].text.strip()
                   )
            data.append(row)
        except IndexError:
            continue
print(len(data))
import pandas as pd
df = pd.DataFrame(data)
print(df)
for i in range(len(data)):
    cursor.execute(mysql_insert,data[i])
    conn.commit()
cursor.close()
conn.close()
print("is over")