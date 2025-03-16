# Author: 邵世昌
# CreateTime: 2025/3/15
# FileName: 多进程
import  multiprocessing
import time

def sing():
    for i in range(3):
        print('sing......')
        time.sleep(1)

def dance():
    for i in range(3):
        print('dance......')
        time.sleep(1)

def rap():
    for i in range(3):
        print('rap......')
        time.sleep(1)

if __name__ == '__main__':
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    rap_process = multiprocessing.Process(target=rap)
    sing_process.start()
    dance_process.start()
    rap_process.start()