# Author: 邵世昌
# CreatTime: 2024/11/18
# FileName: 爬取哔哩哔哩视频的播放量和点赞量
import  requests
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
utl = 'https://www.bilibili.com/'
response = requests.get(utl, headers=header)
from lxml import etree
tree = etree.HTML(response.text)

#%%爬取名称
name_list =[]
names = tree.xpath('//*[@id="i_cecream"]/div/main/div/div/div/div/div/div/div/div/h3/a')
for name in names:
    name_list.append(name.text)
#%%爬取播放量
boufangs_list = []
boufangs = tree.xpath('//*[@id="i_cecream"]/div/main/div/div/div/div/div/div/a/div/div/div/div/span[1]/span')
for boufang in boufangs:
    boufangs_list.append(boufang.text)
#%%爬取点赞量
dianzan_list = []
dianzans = tree.xpath('//*[@id="i_cecream"]/div/main/div/div/div/div/div/div/a/div/div/div/div/span[2]/span')
for dianzan in dianzans:
    dianzan_list.append(dianzan.text)

#%%数据合并
import pandas as pd
name_list = pd.DataFrame(name_list,columns=['name'])
boufangs_list = pd.DataFrame(boufangs_list,columns=['boufang'])
dianzan_list = pd.DataFrame(dianzan_list,columns=['dianzan'])
dataset = pd.concat([name_list,boufangs_list],axis=1)
dataset = pd.concat([dataset,dianzan_list],axis=1)
dataset.to_csv("哔哩哔哩视频播放量点赞量爬取数据.csv",encoding="utf_8_sig")#保存防止出现乱码
