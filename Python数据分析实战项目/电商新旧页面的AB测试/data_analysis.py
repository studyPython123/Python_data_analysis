# Author: 邵世昌
# CreateTime: 2025/3/8
# FileName: data_analysis
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from scipy.stats import norm

# ——————————————数据预处理——————————————————
#%%导入数据
data = pd.read_csv('AB_data.csv')
print(data.head())
print(data.info())
columns = data.columns
print(columns)
print(data.duplicated().sum())
print(data.isnull().sum())
# 没有缺失值，没有重复数据

#%%检查数据的一致性
treatment_number = len(data[data['group'] == 'treatment'])
control_number = len(data[data['group'] == 'control'])
print(f'实验组总人数：{treatment_number}, 对照组总人数：{control_number}')
# 实验组总人数：147276, 对照组总人数：147202

treatment_old_page = len(data[(data['group'] == 'treatment') & (data['landing_page'] == 'old_page')])
control_new_page = len(data[(data['group'] == 'control') & (data['landing_page'] == 'new_page')])
print(f'实验组但是浏览到旧页面的人数是：{treatment_old_page}\n'
      f'对照组但是浏览到新页面的人数是：{control_new_page}')
'''
实验组但是浏览到旧页面的人数是：1965
对照组但是浏览到新页面的人数是：1928
'''
print(f'实验组错误数据占比：{treatment_old_page / treatment_number},'
      f'对照组错误数据占比：{control_new_page / control_number}')
'''
 实验组错误数据占比：0.013342296097123767,对照组错误数据占比：0.013097648129780846
 虽然存在错误数据，但并不意味着实验数据无效，由于两组中错误数据的量相差不大，
 并不影响实验组与对照组的比例，因此只需要依照实际浏览页面进行分组，将错误数据转换为正确的数据
'''
#%%数据清洗
treatment_error = data[(data['group'] == 'treatment') & (data['landing_page'] == 'old_page')]
control_error = data[(data['group'] == 'control') & (data['landing_page'] == 'new_page')]
# 将实验组中浏览新页面的实验者归入对照组
treatment_error_index = list(treatment_error.index)
for index in treatment_error_index:
      data.loc[index, 'group'] = 'control'
# 将对照组中浏览新页面的实验者归入实验组
control_error_index = list(control_error.index)
for index in control_error_index:
      data.loc[index, 'group'] = 'treatment'

# %% 检查数据的一致性
treatment_old_page_dealed = len(data[(data['group'] == 'treatment') & (data['landing_page'] == 'old_page')])
control_new_page_dealed = len(data[(data['group'] == 'control') & (data['landing_page'] == 'new_page')])
print(f'实验组但是浏览到旧页面的人数是：{treatment_old_page_dealed}\n'
      f'对照组但是浏览到新页面的人数是：{control_new_page_dealed}')
'''
实验组但是浏览到旧页面的人数是：0
对照组但是浏览到新页面的人数是：0
'''
# 数据一致
treatment_number = len(data[data['group'] == 'treatment'])
control_number = len(data[data['group'] == 'control'])
print(f'实验组总人数：{treatment_number}, 对照组总人数：{control_number}')
'''
实验组总人数：147239, 对照组总人数：147239
'''
# %%检查是否存在一个实验者被多次记录的情况
user = data['user_id']
print(user.duplicated().sum()) # 3894个实验者存在重复数据
user_repeat = user[user.duplicated()] # 提取有重复记录的实验者ID
data_repeat = data[data['user_id'].isin(user_repeat.values.tolist())] # 提取实验者ID重复的所有数据
data_repeat_group_user_id = data_repeat.groupby('user_id')['landing_page']
id_repeat = [] # 接收同时浏览了新旧页面的实验者ID
for group in data_repeat_group_user_id:
      if len(set(group[1].values.tolist())) == 2:
            id_repeat.append(group[0])
print(len(id_repeat)) # 1998个实验者同时浏览了新旧页面，为了避免影响，删除这些数据
for i in id_repeat:
      indices_to_drop = data[data['user_id'] == i].index
      data.drop(indices_to_drop, inplace=True)
# 删除同时处在实验组和对照组的实验数据

#%% 删除重复数据 剩余290482条数据
user = data['user_id']
print(user.duplicated().sum()) # 1896个实验者存在重复数据
user_repeat = user[user.duplicated()] # 提取有重复记录的实验者ID
for i in user_repeat.values.tolist():
      indices_to_drop = data[data['user_id'] == i].index[0]
      data.drop(indices_to_drop, inplace=True)
# 删除浏览两次同一界面的实验者数据中的第一条

#%% 检查是否存在重复数据
user = data['user_id']
print(user.duplicated().sum())
# 重复实验者者记录为0
data.to_csv('data_dealed.csv',index=False)

#%% 流量对比
data = pd.read_csv('data_dealed.csv')
treatment_number = len(data[data['group'] == 'treatment'])
control_number = len(data[data['group'] == 'control'])
print(f'实验组总人数：{treatment_number}, 对照组总人数：{control_number}')
'''
实验组总人数：144319, 对照组总人数：144267
两组流量分配相对均衡，符合分析条件
'''
#%%————————————————假设检验————————————————————
'''
记旧页面的转化率为 p1，新页面的转化率为 p2
原假设 ： p1<p2 即p1-p2<0
备择假设 ：p1>=p2 即 p1-p2>=0
0-1分布：就是n=1情况下的二项分布，任何只有两种结果的随机现象都服从0-1分布
本次检验α取0.05
'''
#  旧版、新版转化用户数
convert_old = data.query('group=="control" & converted==1').shape[0]
convert_new = data.query('group=="treatment" & converted==1').shape[0]
# 旧版、新版转化率
p_old = convert_old / control_number
p_new = convert_new / treatment_number
p_c = (convert_old + convert_new)/(control_number + treatment_number)
z = (p_old - p_new)/ np.sqrt(p_c*(1 - p_c)*( 1/control_number + 1/treatment_number))  #  检验统计量
z_alpha = norm.ppf(0.025)
print('旧版总受试用户数:', control_number, '旧版转化用户数:', convert_old, '旧版转化率:', p_old)
print('新版总受试用户数:', treatment_number, '新版转化用户数:', convert_new, '新版转化率:', p_new)
print('转化率的联合估计:', p_c)
print('检验统计量z:', z)
print(z_alpha)
result = "落入拒绝域，拒绝原假设" if  z  > z_alpha else "接受原假设"
print(result)

#%% 合并标准差
std_old = data[data.landing_page=="old_page"].converted.std()
std_new = data[data.landing_page=="new_page"].converted.std()
s = np.sqrt(((control_number - 1)* std_old**2 + (treatment_number - 1)* std_new**2 ) /
            (control_number + treatment_number - 2))
d = (p_old - p_new) / s # 效应量Cohen's d
print('Cohen\'s d为：', d)

'''
Cohen's d 是一种用于衡量两个样本均值差异大小的效应量指标。
Cohen's d的值约为-0.008304，绝对值很小。
两者虽有显著性水平5%时统计意义上的显著差异，但差异的效应量很小。
可以理解为显著有差异，但差异的大小不显著。
'''