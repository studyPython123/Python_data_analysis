# Author: 邵世昌
# CreatTime: 2024/11/20
# FileName: 京东商城洗发水信息数据
import requests
from lxml import etree
header = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
title_list = []
evaluate_list = []
price_list = []
for item in range(1,5):
    url = f'https://re.jd.com/search?keyword=%E6%B4%97%E5%8F%91%E6%B0%B4&page={item}&enc=utf-8'
    response = requests.get(url, headers=header)
    tree = etree.HTML(response.text)
    titles = tree.xpath('//*[@id="shop_list"]/li/div/div/a/div[2]')
    for title in titles:
        title_list.append(title.text)
        # print(title.text)
    evaluates = tree.xpath('//*[@id="shop_list"]/li/div/div/a/div/span/em')
    for evaluate in evaluates:
        print(evaluate.text)
        evaluate_list.append(evaluate.text)
    # scores2 = tree.xpath('//*[@id="content"]/section/div/a/i/text()')
    # for i in range(len(scores1)):
    #     score_list.append(scores1[i].text+scores2[i])
        # print(scores1[i].text+scores2[i])
    prices = tree.xpath('//*[@id="shop_list"]/li/div/div/a/div/span/text()')
    for price in prices:
        price_list.append(price)
        # print(brief.text)
import pandas as pd
title_list = pd.DataFrame(title_list,columns=['title'])
evaluate_list = pd.DataFrame(evaluate_list,columns=['evaluate'])
price_list = pd.DataFrame(price_list,columns=['price'])
data = pd.concat([title_list,evaluate_list,price_list],axis=1)
data.to_csv("京东商城洗发水数据信息.csv",index=False,encoding="utf_8_sig")
print("is over")