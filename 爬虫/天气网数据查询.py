# Author: 邵世昌
# CreatTime: 2024/11/22
# FileName: 天气网数据查询
import urllib.request #自带
from bs4 import BeautifulSoup
header ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
url = 'https://www.weather.com.cn/weather/101270101.shtml'
response = urllib.request.urlopen(url)# http 协议
html = response.read().decode('utf-8') # 网页所有数据
# %%解析需要的数据-转换为文档树结果
soup = BeautifulSoup(html,'前端.parser')
lis = soup.select('ul[class="t clearfix"] > li')
for li in lis:
    date = li.select("h1")[0].text.strip()
    wea = li.select('p[class="wea"]')[0].text.strip()
    tem = li.select('p[class="tem"]')[0].text.strip()
    win = li.select('p[class="win"]')[0].text.strip()
    print(date,wea,tem,win)
