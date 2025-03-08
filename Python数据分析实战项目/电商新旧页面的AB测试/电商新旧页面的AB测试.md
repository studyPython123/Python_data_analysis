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
## 2.2 导入并检查数据
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




