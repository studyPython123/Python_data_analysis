# Author: 邵世昌
# CreateTime: 2025/3/15
# FileName: 单进程
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
    sing()
    dance()
    rap()
