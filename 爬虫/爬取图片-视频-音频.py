# Author: 邵世昌
# CreateTime: 2025/3/14
# FileName: 爬取图片-视频-音频-视频-音频
import requests
from lxml import etree
headers = {
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
url = 'https://movie.douban.com/top250?start=0&filter='
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

#%% 用lxml爬取数据
tree = etree.HTML(response.text)
titles = tree.xpath('//*[@id="content"]/div/div/ol/li/div/div/div/a/span[1]')
for title in titles:
    print(title.text)

#%% 用bs4爬取数据
from bs4 import BeautifulSoup
soup =  BeautifulSoup(response.text, '前端.parser')
titles = soup.findAll('span',attrs = {'class':'title'})
for title in titles:
    if '/' not in title.string:
        print(title.string)

#%% 爬取图片-视频-音频
url = 'https://movie.douban.com/top250?start=0&filter='
response = requests.get(url, headers=headers)
content = requests.get('https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp',headers = headers).content
with open('肖申克的救赎.jpg',mode='wb') as file:
    file.write(content)

#%%批量爬取图片
soup = BeautifulSoup(response.text, '前端.parser')
img_data = soup.findAll('img')
for img in img_data:
    content = requests.get(img.get('src'),headers = headers).content
    with open(f'{img.get('alt')}.jpg', mode='wb') as file:
        file.write(content)


#%%批量爬取图片
number = int(input('请输入爬取的页数：'))
for num in range(1,number):
    url = f'https://haowallpaper.com/?isSel=false&page={num}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, '前端.parser')
    img_data = soup.findAll('img')
    for img in img_data:
        content = requests.get(img.get('src'),headers = headers).content
        with open(f'{img.get('alt')}.jpg', mode='wb') as file:
            file.write(content)

#%%爬取音频
url = 'https://lv-sycdn.kuwo.cn/2aa3c3b2d56e87da0fa677e9a4b780be/67d43136/resource/30106/trackmedia/M8000040uYbR1AkIDA.mp3'
url = 'https://lv-sycdn.kuwo.cn/b33c68ac4aec645bf2800bb5eecebd4b/67d43012/resource/30106/trackmedia/M800002cMN5P2UZMOE.mp3'
url = 'https://ga-sycdn.kuwo.cn/3d8484ede67a7918b5f3dc565cf2fa4b/67d43fdd/resource/pay3_v2/279292599/279292599_29_0.1726120459.mp3'
url = 'https://lx-sycdn.kuwo.cn/a4a8b207d5b108e656ba398bb36f0146/67d43207/resource/n3/12/78/3603119950.mp3'
url = 'https://lv-sycdn.kuwo.cn/9e8c1373bea37961b30d653411b6e6be/67d52a60/resource/30106/trackmedia/M5000040uYbR1AkIDA.mp3'
response = requests.get(url, headers=headers)
content = response.content
with open("野花做了场玫瑰花的梦.mp4","wb") as file:
    file.write(content)

#%%爬取视频
url = 'https://stock.xinpianchang.com/footage/details/Dl7lTpLEla59RV.html'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'前端.parser')
video = soup.findAll('video')
print(video)
for vid in video:
    content = requests.get(vid.get('src'), headers=headers).content
    with open(f'{vid.get('mediatype')}.mp4', mode='wb') as file:
        file.write(content)

#%%爬取壁纸
url = 'https://haowallpaper.com/?isSel=false&page=1'
url = 'https://www.bizhi99.com/7680x4320/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'前端.parser')
img_data = soup.find_all('img')
print(img_data)
for img in img_data:
    content = requests.get(img.get('data-original'), headers=headers).content
    with open(f'{img.get('alt')}.jpg', mode='wb') as file:
        file.write(content)