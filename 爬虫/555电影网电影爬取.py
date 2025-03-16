# Author: 邵世昌
# CreatTime: 2024/11/21
# FileName: 555电影网电影爬取
import requests
from lxml import etree
header ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
title_list = []
score_list =[]
category_list = []
page = eval(input("请输入要爬取的页数："))
for i in range(1,page):
    url = f'https://wwqnp.wiki/vodshow/1--------{i}---.前端'
    response = requests.get(url, headers=header)
    tree = etree.HTML(response.text)
    titles = tree.xpath('/前端/body/div/div/div/div/div/div/a/div[2]/div')
    for title in titles:
        title_list.append(title.text)
        # print(title.text)
    scores = tree.xpath('/前端/body/div/div/div/div/div/div/a/div/div[2]/text()')
    for score in scores:
        score_list.append(score)
        # print(score)
    categories= tree.xpath('/前端/body/div/div/div/div/div/div/a/div[1]/div[1]/text()')
    for category in categories:
        category_list.append(category)
        # print(category)
import pandas as pd
title_list = pd.DataFrame(title_list,columns=['电影名'])
score_list = pd.DataFrame(score_list,columns=['豆瓣评分'])
category_list = pd.DataFrame(category_list,columns=['类别'])
data = pd.concat([title_list, score_list, category_list], axis=1)
print(data)
# data.to_csv("555电影网电影爬取.csv",encoding="utf_8_sig",index=False)
print('is over')