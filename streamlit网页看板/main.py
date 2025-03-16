# Author: 邵世昌
# CreateTime: 2025/3/16
# FileName: main
import pandas
import pandas as pd
import streamlit as st
import altair as alt
st.set_page_config(layout = 'wide')
@st.cache_data
def load_data():
    return pd.read_csv(r"E:\Pycharm\orgintext\streamlit数据看板\订单.csv")
data = load_data()

# 侧边栏
st.sidebar.header('筛选条件：')
region_values = data['区域'].unique()
regions = st.sidebar.multiselect('区域', region_values) or region_values

category_values = data['类别'].unique()
categories = st.sidebar.multiselect('类别', category_values) or category_values

son_category_values = data['子类别'].unique()
son_categories = st.sidebar.multiselect('子类别', son_category_values) or son_category_values
data = data.query('区域 in @regions and 类别 in @categories and 子类别 in @son_categories')

# 页面
st.title('订单销售数据看板')

# 指标
total_sales = int(data['销售额'].sum())
avg_zk = int(round(data['折扣'].mean(),2))
stars = ':star:' * avg_zk
avg_sales = int(round(data['销售额'].mean(),2))

left ,mid,right = st.columns(3)
with left:
    st.subheader('总销售额：')
    st.subheader(f'{total_sales}￥')
with mid:
    st.subheader('折扣：')
    st.subheader(f'{avg_zk}{stars}')
with right:
    st.subheader('平均销售额：')
    st.subheader(f'{avg_sales}￥')
c = alt.Chart(data).mark_bar().encode(
    x = alt.X('sum(销售额)',title='总销售额'),
    y = '子类别'
)
st.altair_chart(c, use_container_width=True)