# Author: 邵世昌
# CreatTime: 2024/12/15
# FileName: data_deal
#%% 导入库
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import warnings
import jieba
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
'''*****************************************************login***********************************************************'''
#%%login数据导入并检查
login_data = pd.read_csv('login.csv',encoding='gbk')
print(login_data.head())
print(login_data.info()) #查看属性
print(login_data.isnull().sum()) # 检查空值
for i in login_data.columns:
    print(f'{i}',login_data[login_data[f'{i}'] == '--'])  # 检查异常值
'''
任务 1 数据预处理
任务 1.1 对照附录 1，理解各字段的含义，进行缺失值、重复值等方面的必12要处理，将处理结果保存为“task1_1_X.csv”（如果包含多张数据表，X 可从 1 开始往后编号），并在报告中描述处理过程。
任务 1.2 对用户信息表中 recently_logged 字段的“--”值进行必要的处理，将处理结果保存为“task1_2.csv”，并在报告中描述处理过程。
'''
#%%数据处理，一天内重复登录的行为视为一次登录即可，以减少数据量
login_data['login_time'] = pd.to_datetime(login_data['login_time'],format='%Y-%m-%d %H:%M:%S') # 转化为时间数据
login_data['login_time'] = login_data['login_time'].dt.date # 保留日期数据
login_data.drop_duplicates(inplace=True) #删除重复数据
'''
# 删除重复数据(地址不同也删除)
# login_data_user_id_login_time_distinct = login_data[['user_id','login_time']].drop_duplicates() #保留每人每日的一次记录
# login_place_list = [] # 接纳对应索引的地址
# for i in login_data_user_id_login_time_distinct.index:
#      login_place_list.append(login_data.loc[i,'login_place'])
# login_place_list_df = pd.DataFrame(login_place_list,index=login_data_user_id_login_time_distinct.index) # 地址转化为表格，索引为对照索引
# login_data_distinct = pd.concat([login_data_user_id_login_time_distinct,login_place_list_df],axis=1,ignore_index=False)
'''
#%%# 以最近的时间为基准，计算出用户每一次登录距离现在的时间
login_data['time_gap_days'] = [f'{i.days}days' for i in (login_data['login_time'].max() - login_data['login_time']).tolist()]
login_data = login_data.reset_index(drop=True) #索引重排序

#%% 细分地区
for i in range(login_data.shape[0]):
    if login_data.loc[i,'login_place'][0:2] == '中国':
        login_data.loc[i,'国家'] = '中国'
        if '黑龙江' in login_data.loc[i,'login_place']:
            login_data.loc[i,'省份'] = '黑龙江'
            if len(login_data.loc[i,'login_place'])>5:
                login_data.loc[i,'地区'] = login_data.loc[i,'login_place'][5:]
            else:pass
        if '新疆维吾尔' in login_data.loc[i,'login_place']:
            login_data.loc[i,'省份'] = '新疆维吾尔'
            if len(login_data.loc[i,'login_place'])>7:
                login_data.loc[i,'地区'] = login_data.loc[i,'login_place'][7:]
            else:pass
        if '内蒙古' in login_data.loc[i,'login_place']:
            login_data.loc[i,'省份'] = '内蒙古'
            if len(login_data.loc[i,'login_place'])>5:
                login_data.loc[i,'地区'] = login_data.loc[i,'login_place'][5:]
            else:pass
        else:
            login_data.loc[i,'省份'] = login_data.loc[i,'login_place'][2:4]
            login_data.loc[i,'地区'] = login_data.loc[i,'login_place'][4:]
    else:
        li = [word for word in jieba.cut(login_data.iloc[i,2])]
        if len(li) == 2:
            login_data.loc[i,'国家'] = li[0]
            login_data.loc[i,'省份'] = li[1]
        else:
            login_data.loc[i,'国家'] = li[0]
    if i%10000 == 0:
        print(f'{round(i*100/(int(login_data.shape[0])),2)}%')
login_data.to_csv('login_dealed.csv',encoding='utf_8_sig',index=False) # 保存处理好的数据

'''*****************************************************study_information***********************************************************'''
#%%study_information数据处理
study_information = pd.read_csv('study_information.csv',encoding='gbk')
print(study_information.head())
print(study_information.info())
print(study_information.isnull().sum()) # 缺失值count(price) = 4238
print(study_information[study_information.price.isnull()].course_id.value_counts()) # 每个课程价格缺失的数据
stu_course = study_information.groupby(['course_id']).agg({'price':['max','min']}) # 查看价格是否有差异
stu_course[(stu_course['price']['max'] != stu_course['price']['min'])]
#%% 数据类型转换，课程进度转化为数值数据，时间转换为时间数据(保留日期)
study_information.learn_process = [int(i.split(':')[1].split('%')[0]) for i in study_information.learn_process.tolist()]
study_information.course_join_time = pd.to_datetime(study_information.course_join_time,format='%Y-%m-%d %H:%M:%S').dt.date
print(study_information.duplicated().sum())
study_information.to_csv('study_information_dealed.csv',encoding='utf_8_sig',index=False) # 保存处理好的数据

'''*****************************************************users***********************************************************'''
#%%users数据处理
users_data = pd.read_csv('users.csv',encoding='gbk')
print(users_data.head())
print(users_data.info())
print(users_data.duplicated().sum()) # 有3个重复数据
users_data.drop_duplicates(inplace = True)  # 删除重复数据

#%%缺失值处理
print(users_data.isnull().sum())# 缺失值count(user_id) = 67\count(school) = 33409
users_data = users_data[~users_data.user_id.isnull()] # 保留id不空的用户（缺失值不多）
users_data['是否填写学校'] = users_data['school'] # 创建是否填写的虚拟变量
users_data['是否填写学校'][~users_data['是否填写学校'].isnull()] = 1
users_data['是否填写学校'][users_data['是否填写学校'].isnull()] = 0
print(users_data['是否填写学校'].value_counts())
#%%异常值处理
'''
可以看出有一些recently_logged时间和现在的时间很接近，有一些很远，因此可以将‘--’进行进一步分析
用户注册后未登录
用户注册后就未退出登录 使用login中的最新登录信息进行替换
因此考虑使用学习时间加上注册的时间作为其最近的登录时间，且设置一天学习8小时为上限
'''
recently_logged_outliers = users_data.recently_logged[users_data.recently_logged == '--']
recently_logged_normals = users_data.recently_logged[users_data.recently_logged != '--']
keys = login_data.groupby('user_id').login_time.max().index.tolist()
values = login_data.groupby('user_id').login_time.max().values.tolist()
login_time = {}
for i in range(len(keys)):
    login_time[keys[i]] = values[i] # 获取用户最近登入时间（login表格里面）！！！
for index in recently_logged_outliers.index:
    if users_data.loc[index,'user_id'] in login_time.keys(): # 学习时间为0
        users_data.loc[index,'recently_logged'] = pd.to_datetime(login_time[users_data.loc[index,'user_id']]) # 最近登入时间为注册时间
    else:
        if (pd.to_datetime(users_data.loc[index,'register_time']) + datetime.timedelta(days=(int(users_data.loc[index,'learn_time'])+1) / 480)) > pd.to_datetime('2020-06-18'):
            users_data.loc[index,'recently_logged'] = pd.to_datetime('2020-06-18') # 目前的日期
            print('修改时间为最新时间')
        else:
            users_data.loc[index,'recently_logged'] = pd.to_datetime(users_data.loc[index,'register_time']) + datetime.timedelta(days=int(users_data.loc[index,'learn_time']) / 480)

#%%获取时间差
users_data['register_time'] = pd.to_datetime(users_data['register_time']).dt.date # 转换为时间格式
users_data['recently_logged'] = pd.to_datetime(users_data['recently_logged']).dt.date # 转换为时间格式
users_data['register_now_gap_time'] = (users_data['recently_logged'].max() - users_data['register_time']).tolist()# 注册到目前的时间差
users_data['logged_now_gap_time'] = (users_data['recently_logged'].max() - users_data['recently_logged']) #最近登入到现在时间差
users_data['register_logged_gap_time'] = (users_data['recently_logged'] - users_data['register_time']) # 注册到最近登入时间

# %%添加选课数量字段
users_data['number_of_classes_now'] = users_data['number_of_classes_join']-users_data['number_of_classes_out']#获取用户现在加入的班级的数量
course_counts = study_information.groupby('user_id')['course_id'].count() # 获取不同客户的选课数量
users_data.set_index('user_id',inplace=True)
for user_id in course_counts.index:
     users_data.loc[user_id,'course_count'] = course_counts[user_id]
users_data.reset_index(inplace=True,drop=False)
users_data['course_count'].fillna(0,inplace=True)

#%%信息整合
login_data_groupby_userid = login_data.groupby('user_id')[['login_time','国家','省份','地区']]
recently_logged_location = {} # 接收客户最近登入的地址
for temp in login_data_groupby_userid:
    user_id = temp[0]
    temp_sortby_login_time = temp[1].sort_values(by = 'login_time',ascending=False)
    recently_logged_location[user_id] = temp_sortby_login_time.iloc[0,1:]
users_data.set_index('user_id',inplace=True)
for user_id,location in recently_logged_location.items():
    if user_id in users_data.index:
        users_data.loc[user_id,'国家'] = location['国家']
        users_data.loc[user_id,'省份'] = location['省份']
        users_data.loc[user_id,'城市'] = location['地区']
print("is over")
users_data.reset_index(inplace=True,drop=False)
users_data.to_csv('全部整合信息.csv',encoding='utf_8_sig',index=False)