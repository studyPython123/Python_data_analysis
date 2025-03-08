# Author: 邵世昌
# CreatTime: 2024/11/23
# FileName: 查看电脑所有文件
import os
def find_all_files(root_path):
    all_files = []
    for root, dirs, files in os.walk(root_path): # 创建生成器
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files
toot_files = find_all_files('E:\课程材料')
for toot_file in toot_files:
    print(toot_file)
print('is over')