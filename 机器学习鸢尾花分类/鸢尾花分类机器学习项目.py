# Author: 邵世昌
# CreatTime: 2024/12/9
# FileName: 项目代码
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # 使用支持向量机分类器
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['KaiTi']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号
'''
鸢尾花 3 种类别分别为山鸢尾（setosa）、变色鸢尾（versicolor）和维吉尼亚鸢尾（virginica）。
有花萼长度、花萼宽度、花瓣长度、花瓣宽度4项特征，通过这4个特征预测鸢尾花卉属于哪一品种。
'''
# %%载入数据
iris_data = load_iris() # 使用 load_iris 函数加载鸢尾花数据集，返回一个 Bunch 对象
data = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)

# %%每个特征的直方图
ax = data.hist(bins=20, edgecolor='black',figsize=(12, 8))
# 遍历每个直方图，添加数值标签
for i, (ax_i, column) in enumerate(zip(ax.flatten(), data.columns)):
    bars = ax_i.patches # 获取直方图的条形对象
    for bar in bars:
        height = bar.get_height() # 获取条形的高度和中心位置
        x = bar.get_x() + bar.get_width() / 2
        ax_i.text(x, height, str(int(height)), ha='center', va='bottom') # 在条形上方添加数值标签
plt.tight_layout()
plt.show()

# %%每个特征的直方图-标准化之后
ax = data.iloc[:,:-2].hist(bins=20, edgecolor='black',figsize=(12, 8))
# 遍历每个直方图，添加数值标签
for i, (ax_i, column) in enumerate(zip(ax.flatten(), data.iloc[:,:-2].columns)):
    bars = ax_i.patches # 获取直方图的条形对象
    for bar in bars:
        height = bar.get_height() # 获取条形的高度和中心位置
        x = bar.get_x() + bar.get_width() / 2
        ax_i.text(x, height, str(int(height)), ha='center', va='bottom') # 在条形上方添加数值标签
plt.tight_layout()
plt.show()

#%% 线图
data.plot(kind='kde')
data.iloc[:,:-2].plot(kind='kde')

#%% 箱线图
data.boxplot()
data.iloc[:,:-2].boxplot()

#%% 数据处理
data['target'] = iris_data.target # 目标标签
data['target_names'] = data['target'].apply(lambda x: iris_data.target_names[x]) #目标名称
print(data.head())      # 查看数据集前五行数据
print('------------------------------------------------------------------------------')
print(data.info())      # 查看数据集的基本信息
print('------------------------------------------------------------------------------')
print(data.describe())  # 查看数据集的统计信息
# sns.boxplot(y = data['sepal length (cm)'],x = data['target_names'])
#分类分布情况
print(data.groupby('target_names').size())
a = data.describe().iloc[1:3,:4]
#%% 绘制箱线图
fig,axes = plt.subplots(2,2,figsize=(10,8))
sns. boxplot (y = data['sepal length (cm)'],x = data['target_names'], data=data, palette=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=axes[0, 0])
sns. boxplot (y = data['sepal width (cm)'],x = data['target_names'], data=data, palette=["#1f77b4", "#ff7f0e", "#2ca02c"],ax=axes[0, 1])
sns. boxplot (y = data['petal length (cm)'],x = data['target_names'], data=data, palette=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=axes[1, 0])
sns. boxplot (y = data['petal width (cm)'],x = data['target_names'], data=data, palette=["#1f77b4", "#ff7f0e", "#2ca02c"], ax=axes[1, 1])

# %%数据预处理绘制特征分布图
palette = sns.color_palette("hls", 3)
sns.pairplot(data, hue='target',palette= palette, markers=["o", "s", "D"])  # 使用 seaborn 库的 pairplot 函数绘制散点图矩阵，根据 'target' 列着色，并使用不同的标记
plt.show()
#%%
print(data.isnull().sum())  # 检查是否存在缺失值
scaler = StandardScaler() # 创建 StandardScaler 对象
data[iris_data.feature_names] = scaler.fit_transform(data[iris_data.feature_names])  # 对特征列进行标准化处理
print(data.head()) # 查看标准化后的数据

#%%数据分割
x = data[iris_data.feature_names]  # 特征数据
y = data['target']  # 目标标签
# 将数据集按 70% 训练集和 30% 测试集进行分割，设置随机种子为 42 以确保可重复性
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)
print(f"训练集大小: {x_train.shape[0]}, 测试集大小: {x_test.shape[0]}") # 查看分割后的数据集大小
#%%支持向量机
svc = SVC(kernel='linear')# 创建SVM分类器
svc.fit(x_train, y_train)# 训练模型
y_pred_svc = svc.predict(x_test)# 在测试集上预测
conf_matrix = confusion_matrix(y_test, y_pred_svc)# 混淆矩阵
print(f"准确率: {accuracy_score(y_test, y_pred_svc)*100:.2f}%")
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris_data.target_names, yticklabels=iris_data.target_names)# 可视化混淆矩阵
plt.xlabel('预测类别',fontsize =20)
plt.ylabel('实际类别',fontsize =20)
plt.title('支持向量机混淆矩阵',fontsize =20)
plt.show()
print("Classification Report:\n", classification_report(y_test, y_pred_svc))  # 打印分类报告，包括精确率、召回率、F1 分数等
print('-')
#%%KNN算法
knn = KNeighborsClassifier(n_neighbors=3)  # 初始化 KNN 分类器,创建一个 K 近邻分类器对象，设置近邻数为 3
knn.fit(x_train, y_train) # 训练模型
y_pred_knn = knn.predict(x_test)  # 使用训练好的模型对测试数据进行预测，得到预测标签
print(f"准确率: {accuracy_score(y_test, y_pred_knn)*100:.2f}%") # 计算准确率
sns.heatmap(confusion_matrix(y_test, y_pred_knn), annot=True, fmt='d', cmap='Blues',
            xticklabels=iris_data.target_names, yticklabels=iris_data.target_names)# 可视化混淆矩阵
plt.xlabel('预测类别',fontsize =20)
plt.ylabel('实际类别',fontsize =20)
plt.title('KNN算法混淆矩阵',fontsize =20)
plt.show()
print("Classification Report:\n", classification_report(y_test, y_pred_knn))  # 打印分类报告，包括精确率、召回率、F1 分数等
print('-')
#%%决策树
clf = DecisionTreeClassifier(random_state=42) # 创建决策树分类器实例
clf.fit(x_train, y_train) # 训练模型
y_pred_clf = clf.predict(x_test)
accuracy = accuracy_score(y_test, y_pred_clf) # 计算准确率
print(f"Accuracy: {accuracy*100:.2f}%")
sns.heatmap(confusion_matrix(y_test, y_pred_clf), annot=True, fmt='d', cmap='Blues',
            xticklabels=iris_data.target_names, yticklabels=iris_data.target_names)# 可视化混淆矩阵
plt.xlabel('预测类别',fontsize =20)
plt.ylabel('实际类别',fontsize =20)
plt.title('决策树算法混淆矩阵',fontsize =20)
plt.show()

#%%随机森林评估器
estimator = RandomForestClassifier()
estimator.fit(x_train,y_train)
y_pred_est = estimator.predict(x_test) #模型评估
accuracy = accuracy_score(y_test, y_pred_est) # 计算准确率
print(f'模型准确率：{accuracy*100:.2f}%')
sns.heatmap(confusion_matrix(y_test, y_pred_est), annot=True, fmt='d', cmap='Blues',
            xticklabels=iris_data.target_names, yticklabels=iris_data.target_names) # 可视化混淆矩阵
plt.xlabel('预测类别',fontsize =20)
plt.ylabel('实际类别',fontsize =20)
plt.title('随机森林算法混淆矩阵',fontsize =20)
plt.show()

#%%预测分类可视化
x_test['target'] = y_pred_knn
palette = sns.color_palette("hls", 3)
sns.pairplot(x_test, hue='target',palette= palette, markers=["o", "s", "D"])  # 使用 seaborn 库的 pairplot 函数绘制散点图矩阵，根据 'target' 列着色，并使用不同的标记
plt.show()

#%%实际类别可视化
x_test['target'] = y_test
palette = sns.color_palette("hls", 3)
sns.pairplot(x_test, hue='target',palette= palette, markers=["o", "s", "D"])  # 使用 seaborn 库的 pairplot 函数绘制散点图矩阵，根据 'target' 列着色，并使用不同的标记
plt.show()

# %%初始化 KNN 分类器
from sklearn.model_selection import GridSearchCV
# 定义参数范围
param_grid = {'n_neighbors': range(1, 20)}  # 创建一个参数字典，设置 'n_neighbors' 参数的取值范围为 1 到 19
# 网格搜索
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)  # 创建一个 GridSearchCV 对象，使用 KNeighborsClassifier 和定义的参数范围，设置交叉验证折数为 5
grid_search.fit(x_train, y_train) # 使用训练数据进行网格搜索，以找到最佳参数组合
# 最优参数
print(f"Best parameters: {grid_search.best_params_}")  # 打印通过网格搜索找到的最优参数
# 使用最优参数训练模型
knn_best = grid_search.best_estimator_  # 获取使用最优参数训练的最佳模型
y_pred_best = knn_best.predict(x_test)  # 使用最佳模型对测试数据进行预测
# 评估模型
print(f"Accuracy（best）: {accuracy_score(y_test, y_pred_best)*100:.2f}%")                      # （优化后）计算并打印模型在测试集上的准确率
print('-')
print("Classification Report（best）:\n", classification_report(y_test, y_pred_best))  # （优化后）打印分类报告，包括精确率、召回率、F1 分数等
print('-')
print("Confusion Matrix（best）:\n", confusion_matrix(y_test, y_pred_best))            # （优化后）打印混淆矩阵，显示真实标签和预测标签之间的关系
print('-')

#%%
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# 加载鸢尾花数据集
iris = load_iris()
x = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)
# 定义不同的分类器以及对应的要搜索的超参数网格
classifiers = {
    "knn": (KNeighborsClassifier(), {
        "n_neighbors": list(range(1, 11)),
        "weights": ["uniform", "distance"]
    }),
    "决策树": (DecisionTreeClassifier(), {
        "criterion": ["gini", "entropy"],
        "max_depth": list(range(3, 11)),
        "min_samples_split": list(range(2, 6))
    }),
    "随机森林": (RandomForestClassifier(), {
        "n_estimators": list(range(50, 101, 50)),
        "criterion": ["gini", "entropy"],
        "max_depth": list(range(3, 6)),
        "min_samples_split": list(range(2, 6))
    })
}
best_models = {} # 用于存储不同分类器最终的最优模型和准确率
kf = KFold(n_splits=5, shuffle=True, random_state=42) # 5折交叉验证
for name, (clf, param_grid) in classifiers.items():
    grid_search = GridSearchCV(clf, param_grid, cv=kf, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    best_models[name] = best_model
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name}最佳模型准确率: {accuracy*100:.2f}%")

#%%数据分割
svc_list = []
knn_list = []
clf_list = []
est_list = []
for i in range(100):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)
    svc = SVC(kernel='linear')# 创建SVM分类器
    svc.fit(x_train, y_train)# 训练模型
    y_pred_svc = svc.predict(x_test)# 在测试集上预测
    accuracy = accuracy_score(y_test, y_pred_svc)
    svc_list.append(accuracy)
    knn = KNeighborsClassifier(n_neighbors=3)  # 初始化 KNN 分类器,创建一个 K 近邻分类器对象，设置近邻数为 3
    knn.fit(x_train, y_train) # 训练模型
    y_pred_knn = knn.predict(x_test)  # 使用训练好的模型对测试数据进行预测，得到预测标签
    accuracy = accuracy_score(y_test, y_pred_knn)
    knn_list.append(accuracy)
    clf = DecisionTreeClassifier(random_state=42) # 创建决策树分类器实例
    clf.fit(x_train, y_train) # 训练模型
    y_pred_clf = clf.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred_clf) # 计算准确率
    clf_list.append(accuracy)
    estimator = RandomForestClassifier()
    estimator.fit(x_train,y_train)
    y_pred_est = estimator.predict(x_test) #模型评估
    accuracy = accuracy_score(y_test, y_pred_est) # 计算准确率
    est_list.append(accuracy)
df = pd.DataFrame({'支持向量机': svc_list, 'k邻近':knn_list,"决策树":clf_list,"随机森林":est_list})
df.boxplot()