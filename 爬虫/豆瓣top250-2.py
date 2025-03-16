# Author: 邵世昌
# CreatTime: 2024/11/20
# FileName: 豆瓣top250-2
import requests
# from lxml import etree
import pandas as pd
from bs4 import BeautifulSoup#有缺陷，有些数据没路径
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
title_list = []
score_list = []
for number in range(0, 250,25):
    response = requests.get(f'https://movie.douban.com/top250?start={number}',headers=header)
    html = response.text
    soup = BeautifulSoup(html,'前端.parser')
    #主题
    titles = soup.findAll("span",attrs={"class":"title"})
    for title in titles:
        if "/" not in title.string:
            title_list.append(title.string)
            # print(title.string)
    #评分
    scores = soup.findAll("span",attrs={"class":"rating_num"})
    for score in scores:
        if "/" not in score.string:
            score_list.append(score.string)
            # print(score.string)

title_list = pd.DataFrame(title_list,columns=['title'])
score_list = pd.DataFrame(score_list,columns=['score'])
data = pd.concat([title_list,score_list],axis=1)
print(data)

# data.to_csv("豆瓣top250（bs4）.csv",encoding="utf_8_sig")