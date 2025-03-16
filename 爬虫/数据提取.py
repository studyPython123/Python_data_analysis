# Author: 邵世昌
# CreatTime: 2024/11/17
# FileName: 数据提取
#提取格式：前端,json,xml
#实现方式：xpath,css,bs4
 #%%xpath：节点+谓语
import  requests
headers = {
 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
url = "https://www.xinpianchang.com/discover/article?from=navigator"
response = requests.get(url, headers=headers)#提取的全部数据
print(response)
# print(response.text)
#%%使用xpath规则进行提取(爬取网页电影名称)
from lxml import etree
etree = etree.HTML(response.text)
#%%提取数据
elements = etree.xpath("//h2[@class='line-clamp-1 break-all']")
for element in elements:
 print(element.text)
#%%提取数据
element_rq = etree.xpath('//*[@id="__next"]/section/main/div/div/div/div/a/div/ul/li[1]/span[2]')
#保存数据
data_list = []
for element in element_rq:
 data_list.append(element.text)
 # print(element.text)
import pandas as pd
df = pd.Series(data_list)
df.to_csv("新片场主页爬取点赞量.csv")



