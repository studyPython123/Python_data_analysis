# Author: 邵世昌
# CreatTime: 2024/11/20
# FileName: 电影网内地爱情电影
import requests
from lxml import etree
header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
title_list = []
score_list = []
brief_list = []
for item in range(1,54):
    url = f'https://www.1905.com/vod/list/n_1_t_1_a_1/o3p{item}.html'
    response = requests.get(url, headers=header)
    tree = etree.HTML(response.text)
    titles = tree.xpath('//*[@id="content"]/section/div/a/h3')
    for title in titles:
        title_list.append(title.text)
        # print(title.text)
    scores1 = tree.xpath('//*[@id="content"]/section/div/a/i/b')
    scores2 = tree.xpath('//*[@id="content"]/section/div/a/i/text()')
    for i in range(len(scores1)):
        score_list.append(scores1[i].text+scores2[i])
        # print(scores1[i].text+scores2[i])
    briefs = tree.xpath('//*[@id="content"]/section/div/a/p')
    for brief in briefs:
        brief_list.append(brief.text)
        # print(brief.text)
import pandas as pd
title_list = pd.DataFrame(title_list,columns=['title'])
score_list = pd.DataFrame(score_list,columns=['score'])
brief_list = pd.DataFrame(brief_list,columns=['brief'])
data = pd.concat([title_list,score_list,brief_list],axis=1)
data.to_csv("电影网内地爱情电影.csv",index=False,encoding="utf_8_sig")
print("is over")