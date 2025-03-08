# Author: 邵世昌
# CreatTime: 2024/11/24
# FileName: os
import os
print(os.getcwd())# 返回当前工作路径
#%%打开文件夹，获取文件名称列表
path = 'E:\实习材料'
title_filename = [i.rstrip('.docx').rstrip('.jpg') for i in os.listdir(path)]
print(title_filename)
# %% 深层遍历子文件夹，返回路径、文件夹列表、文件列表组成的元组
root_path = 'E:\复试材料'
for path, dirs, files in os.walk(root_path):
    print(path) # 路径
    if len(dirs) != 0:
        print(dirs) # 文件夹
    print(files) # 文件
# %% 判断指定路径是否存在
path1 = 'E:\复试材料'
if os.path.exists(path1):
    print('yes')
else:
    print('no')
# %% 指定路径创建文件夹
try:
    path2 = os.getcwd()+'\华为'
    os.mkdir(path2)
except FileExistsError:
    print("文件夹已存在")
# %% 指定路径创建递归文件夹
try:
    path3 = os.getcwd()+'\华为\员工'
    os.makedirs(path3)
except FileExistsError:
    print("文件夹已存在")
# %%删除文件夹
path4 = os.getcwd()+'\华为'
if os.path.exists(path4):
    os.rmdir(path4)
    # print(f'{path4}已删除')
    print(f'{os.path.split(path4)[1]}文件夹已删除')
else:
    print("文件不存在")

#%%只返回目录和文件名称
path5 = os.getcwd()+'\\test.xlsx'
if os.path.exists(path5):
    print(os.path.dirname(path5)) # 目录
    print(os.path.basename(path5)) # 名称
else:
    print("文件不存在")