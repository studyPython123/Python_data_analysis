# 一、分析背景
## 1.1 研究背景和目的
本次分析的数据集来源于一家电商网站，希望通过对于一次AB测试数据的分析判断新旧两版页面在用户转化上是否有显著区别，帮助公司决定是应当采用新的页面，还是保留老的页面。
## 1.2 研究思路
1、对数据进行检查和清洗，确保数据的准确性。
2、然后我们需要明确分析的问题，建立原假设和备选假设。
3、判断样本的抽样分布类型和检测方式，求得检验统计量。
4、确定显著性水平，得出拒绝域。
5、判断检验统计量是否落入拒绝域，得出结论。
6、根据检验结果分析是否采用新页面。
# 二、数据预处理
## 2.1 导入需要的库
```python
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from scipy.stats import norm
```
## 2.2 导入并查看数据相关属性
```python
data = pd.read_csv('AB_data.csv')
print(data.head())
print(data.info())
columns = data.columns
print(columns)
print(data.duplicated().sum())
print(data.isnull().sum())
```
![image](https://github.com/user-attachments/assets/41416201-4292-436a-b1ab-475eb2f91d33)
![image](https://github.com/user-attachments/assets/52a0de2d-b5aa-46d2-9218-ce4973dc753a)

通过检查结果发现没有缺失值，没有重复数据
## 2.3 检查数据的一致性
```python
treatment_number = len(data[data['group'] == 'treatment'])
control_number = len(data[data['group'] == 'control'])
print(f'实验组总人数：{treatment_number}, 对照组总人数：{control_number}')
treatment_old_page = len(data[(data['group'] == 'treatment') & (data['landing_page'] == 'old_page')])
control_new_page = len(data[(data['group'] == 'control') & (data['landing_page'] == 'new_page')])
print(f'实验组但是浏览到旧页面的人数是：{treatment_old_page}\n'
      f'对照组但是浏览到新页面的人数是：{control_new_page}')
print(f'实验组错误数据占比：{treatment_old_page / treatment_number},'
      f'对照组错误数据占比：{control_new_page / control_number}')
```
实验组总人数：147276, 对照组总人数：147202，实验组但是浏览到旧页面的人数：1965，对照组但是浏览到新页面的人数：1928， 实验组错误数据占比：0.0133,对照组错误数据占比：0.0131。 虽然存在错误数据，但并不意味着实验数据无效，由于两组中错误数据的量相差不大，并不影响实验组与对照组的比例，因此只需要依照实际浏览页面进行分组，将错误数据转换为正确的数据。
## 2.4 数据清洗
将实验组中浏览新页面的实验者归入对照组，将对照组中浏览新页面的实验者归入实验组。
```python
treatment_error = data[(data['group'] == 'treatment') & (data['landing_page'] == 'old_page')]
control_error = data[(data['group'] == 'control') & (data['landing_page'] == 'new_page')]
treatment_error_index = list(treatment_error.index)
for index in treatment_error_index:
      data.loc[index, 'group'] = 'control'
control_error_index = list(control_error.index)
for index in control_error_index:
      data.loc[index, 'group'] = 'treatment'
```
正确分组后再次检查数据的一致性，确保不存在冲突的数据，此时实验组总人数：147239, 对照组总人数：147239。
## 2.5 筛查并处理重复记录
虽然通过duplicated函数检查得知不存在重复数据，但是无法排除存在一个实验对象被多次记录或者同时浏览了新旧两种版本的页面，因此需要进一步的筛查。
```python
user = data['user_id']
print(user.duplicated().sum()) # 3894个实验者存在重复数据
user_repeat = user[user.duplicated()] # 提取有重复记录的实验者ID
data_repeat = data[data['user_id'].isin(user_repeat.values.tolist())] # 提取实验者ID重复的所有数据
data_repeat_group_user_id = data_repeat.groupby('user_id')['landing_page']
for group in data_repeat_group_user_id:
      print(group[0],'\n',group[1])
      break
id_repeat = [] # 接收同时浏览了新旧页面的实验者ID
for group in data_repeat_group_user_id:
      if len(set(group[1].values.tolist())) == 2:
            id_repeat.append(group[0])
print(len(id_repeat)) # 1998个实验者同时浏览了新旧页面，为了避免影响，删除这些数据
for i in id_repeat:
      indices_to_drop = data[data['user_id'] == i].index
      data.drop(indices_to_drop, inplace=True)
```
通过对实验对象ID进行筛查，发现有3894个实验对象有重复记录，由于不能确定这些实验对象是多次浏览同一个版本的页面还是浏览了不同页面的版本，因此不能断然选择删除重复数据，这会导致有效数据被删除，所以需要进行判断，由结果可知有1998个实验对象同时浏览了两种版本的网页，无法排除这些实验对象是否受到了两种版本网页的影响，因此选择将这些数据删除，此时剩余290482条数据。

![image](https://github.com/user-attachments/assets/a44958cb-04f6-4aad-9359-ffb3d7a872c2)

