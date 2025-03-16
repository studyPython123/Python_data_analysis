# Author: 邵世昌
# CreatTime: 2024/11/17
# FileName: 提取cookie
#%%控制页面
from selenium import webdriver
driver = webdriver.Chrome()
#%%
url = "https://www.xinpianchang.com/"
driver.get(url)
#%%获取cookie
cookies = driver.get_cookies()
#%%json序列化，转成文本进行储存
import json
cookies_str = json.dumps(cookies)
with open(r"cookies.txt","w",encoding="utf-8") as file:
    file.write(cookies_str)
#%%关闭页面
driver.close()