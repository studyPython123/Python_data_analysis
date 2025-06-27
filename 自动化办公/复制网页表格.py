# Author: 邵世昌
# CreateTime: 2025/6/7
# FileName: 复制网页表格
import  pandas as pd
list_df = []
for i in range(1,2):
    data = pd.read_html(f'https://s.askci.com/stock/0-0-0/{i}/')
    list_df.append(data[0])
df = pd.concat(list_df, ignore_index=True)
# data.to_csv('test.csv')