# Author: 邵世昌
# CreateTime: 2025/3/15
# FileName: 文件夹高并发copy器
import os
import multiprocessing
def work_copy(file_name,source_dir,target_dir):
    source_path = source_dir + "/" + file_name
    target_path = target_dir + "/" + file_name
    with open(source_path,'rb') as source_file: # 读取
        with open(target_path,'wb') as target_file: # 写入
            while True:
                data = source_file.read(1024) # 最多读取1024个字节
                if data:
                    target_file.write(data)
                else:
                    break


if __name__ == '__main__':
    source_dir = r"C:\Users\25782\Desktop\数据分析\Excel表格操作练习实操\01 excel操作基础练习" # 源文件路径
    target_dir = r"C:\Users\25782\Desktop\target" # 目标文件路径
    try:
        os.mkdir(target_dir) # 创建目标文件
    except FileExistsError:
        print("文件夹已存在，未创建~")
    file_list = os.listdir(source_dir)
    for file in file_list:
        work_copy(file,source_dir,target_dir)
        work_process = multiprocessing.Process(target=work_copy,args=(file,source_dir,target_dir))
        work_process.start()