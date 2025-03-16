# Author: 邵世昌
# CreatTime: 2024/11/18
# FileName: 爬取数据实战（酷我音乐）
#%%爬取新片场点赞量
import requests
from lxml import etree
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
url =  "https://www.xinpianchang.com/discover/article?from=navigator"
response = requests.get(url, headers=header)
print(response.text)
etree = etree.HTML(response.text)
# elements = etree.xpath("//span[@class='pl']")
elements = etree.xpath('//*[@id="__next"]/section/main/div/div/div/div/a/div/ul/li[2]/span[2]')
for element in elements:
    print(element.text)
#%%爬取QQ音乐播放量
import requests
from lxml import etree
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
url =  "https://y.qq.com/"
response = requests.get(url, headers=header)
# print(response.text)
etree = etree.HTML(response.text)
# elements = etree.xpath("//span[@class='pl']")
elements = etree.xpath('//*[@id="content"]/div/div/ul/li/div/div[2]')
for element in elements:
    print(element.text)