# Author: 邵世昌
# CreatTime: 2024/11/17
# FileName: chrome环境测试
#chromedriver需要在当前目录
from selenium import webdriver
driver = webdriver.Chrome()

#%%打开网页
url1 = "https://www.xinpianchang.com/discover/article?from=navigator"
driver.get(url1)#打开网页

#%%页面会切换
url = "https://www.baidu.com/"#需要打开的网址
driver.get(url)#打开网页

#%%切换页面
driver.back()#返回上一页面
driver.forward()#前进到下一个页面

#%%页面交互
#1，找到元素；2，声明我们的操作
element = driver.find_element("id","kw")
element.send_keys("爬虫")#向输入块发送值
element1 = driver.find_element("id","su")
element1.click()#点击百度一下

#%%获取页面内容
content = driver.page_source

#%%
driver.close()#关闭网页
