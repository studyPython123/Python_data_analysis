# Author: 邵世昌
# CreateTime: 2025/3/15
# FileName: 多进程含参数
import  multiprocessing
import time

def sing(num):
    for i in range(num):
        print('sing......')
        time.sleep(1)

def dance(num):
    for i in range(num):
        print('dance......')
        time.sleep(1)

def rap(num):
    for i in range(num):
        print('rap......')
        time.sleep(1)

if __name__ == '__main__':
    sing_process = multiprocessing.Process(target=sing,args=(3,)) # 用元组方式给指定任务传参
    dance_process = multiprocessing.Process(target=dance,args=(5,)) # 用元组方式给指定任务传参
    rap_process = multiprocessing.Process(target=rap,kwargs={'num':4}) # 用字典方式给指定任务传参
    sing_process.start()
    dance_process.start()
    rap_process.start()