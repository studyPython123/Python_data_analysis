# Author: 邵世昌
# CreateTime: 2025/6/7
# FileName: 控制鼠标和键盘
import  pyautogui
import time
# 设置安全特性（移动鼠标到屏幕左上角可强制停止程序）
pyautogui.FAILSAFE = True
# 暂停设置（每执行一个pyautogui操作后暂停的秒数）
pyautogui.PAUSE = 1
# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()
print(f"屏幕尺寸: {screen_width} x {screen_height}")
print("鼠标控制演示将在3秒后开始，请将鼠标移至安全区域...")
time.sleep(10)
currentMouseX,currentMouseY = pyautogui.position()
print(currentMouseX,currentMouseY)
time.sleep(4)
# 移动鼠标（绝对位置）
pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=1)
print("鼠标移动到屏幕中央")

time.sleep(10)
pyautogui.moveTo(988, 392, duration=1)

# 鼠标点击
pyautogui.click()  # 单击
# pyautogui.doubleClick()  # 双击
# pyautogui.rightClick()  # 右键点击
# pyautogui.middleClick()  # 中键点击

#%% 鼠标拖动
pyautogui.dragRel(100, 0, button='left', duration=0.5)  # 拖动到指定的位置
pyautogui.dragTo(100, 0, button='left', duration=0.5)  # 拖动到指定的位置区域内容

#%% 滚动
pyautogui.scroll(200)  # 向上滚动200个单位
pyautogui.scroll(-200)  # 向下滚动200个单位