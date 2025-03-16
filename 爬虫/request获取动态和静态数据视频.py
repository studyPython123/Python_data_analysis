# Author: 邵世昌
# CreatTime: 2024/11/17
# FileName: request获取动态和静态数据视频
from selenium import webdriver
import requests
driver = webdriver.Chrome()
#%%自己构造请求(静态加载资源)
#静态数据：页面上有，发送请求的时候可以直接获取回来的数据
#动态数据：页面上有，发送请求的时候获取不回来
#请求行，请求头，请求体
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
url = "https://www.xinpianchang.com/discover/article?from=navigator"
response = requests.get(url, headers=headers)
response.text

#%%动态加载资源
#需要手动的找到网址
#%%
driver.get(url)
driver.close()