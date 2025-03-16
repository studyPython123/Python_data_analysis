# Author: 邵世昌
# CreatTime: 2024/11/17
# FileName: 使用cookies进行登入
#%%控制页面
from selenium import webdriver
import json
driver = webdriver.Chrome()
#%%跳过账号密码登入
url = "https://passport.xinpianchang.com/login?mode=quick&redirect_uri=https%3A%2F%2Fvip.xinpianchang.com%2F"
driver.get(url)
#%%读取cookies
with open("cookies.txt", "r",encoding="utf-8") as file:
    cookies_str = file.read()
cookies = json.loads(cookies_str)
#%%向浏览器注入cookies
for cookie in cookies:
    driver.add_cookie(cookie)
driver.get("https://www.xinpianchang.com/")

#%%关闭页面
# driver.close()

