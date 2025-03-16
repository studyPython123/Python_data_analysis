# Author: 邵世昌
# CreateTime: 2025/3/15
# FileName: 获取进程编号
import  multiprocessing
import time
import os

def sing(num):
    print(f"sing进程的编号：{os.getpid()}")
    print(f"sing父进程的编号：{os.getppid()}")
    for i in range(num):
        print('sing......')
        time.sleep(1)

def dance(num):
    print(f"dance进程的编号：{os.getpid()}")
    print(f"dance父进程的编号：{os.getppid()}")
    for i in range(num):
        print('dance......')
        time.sleep(1)

def rap(num):
    print(f"rap进程的编号：{os.getpid()}")
    print(f"rap父进程的编号：{os.getppid()}")
    for i in range(num):
        print('rap......')
        time.sleep(1)

if __name__ == '__main__':
    sing_process = multiprocessing.Process(target=sing,args=(3,)) # 用元组方式给指定任务传参
    dance_process = multiprocessing.Process(target=dance,args=(5,)) # 用元组方式给指定任务传参
    rap_process = multiprocessing.Process(target=rap,kwargs={'num':4}) # 用字典方式给指定任务传参
    sing_process.daemon = True
    dance_process.daemon =True
    rap_process.daemon = True # 保护主进程，当主进程结束时子进程会自动销毁
    sing_process.start()
    dance_process.start()
    rap_process.start()
    time.sleep(1)
    print(f"主进程的编号：{os.getpid()}")