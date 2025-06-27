import os
import pyautogui
import uiautomation as auto
import time
import pyperclip
import schedule
def wechat_auto_send(friends, message):
    """
    给多个微信好友发送相同消息

    参数:
    friends (list): 好友名称列表
    message (str): 需要发送的消息内容
    """
    # 启动或连接微信
    wechat_window = auto.WindowControl(Name="微信")
    # 激活微信窗口并最大化
    wechat_window.SetActive()

    # 遍历好友列表发送消息
    success_count = 0
    failed_friends = []

    for friend in friends:

        print(f"正在给 {friend} 发送消息...")
        # 搜索好友
        search_box = wechat_window.EditControl(Name="搜索")
        if not search_box.Exists(1, 0.5):
            print("错误: 未找到搜索框")
            failed_friends.append(friend)
            continue
        search_box.Click()
        search_box.SendKeys(friend)

        # 选择好友
        contact_item = wechat_window.ListItemControl(Name=friend)
        if not contact_item.Exists(2, 0.5):
            print(f"错误: 未找到好友 - {friend}")
            failed_friends.append(friend)
            continue
        contact_item.Click()

        # 发送消息
        input_box = wechat_window.EditControl()
        if not input_box.Exists(1, 0.5):
            print(f"错误: 未找到输入框 - {friend}")
            failed_friends.append(friend)
            continue
        input_box.Click()  # 点击输入框并输入消息

        pyperclip.copy(message)# 将消息复制到剪贴板

        pyautogui.hotkey('ctrl', 'v') # 使用 pyautogui 执行 Ctrl+V

        # 发送消息
        input_box.SendKeys("{Enter}")

        print(f"✓ 成功发送消息至 {friend}")
        success_count += 1

    # 输出结果统计
    print("\n===== 发送结果 =====")
    print(f"成功: {success_count}/{len(friends)}")
    if failed_friends:
        print(f"失败: {', '.join(failed_friends)}")
    return success_count == len(friends)

if __name__ == "__main__":
    # 好友列表
    friends_list = ["文件传输助手","小生"]

    # 要发送的消息内容
    message_content = """
        【关于发动学生参与“人工智能+”专项赛的补充通知】
    """
    # 程序执行
    wechat_auto_send(friends_list, message_content)

    # 每日定时执行
    # schedule.every().day("08:00").do(wechat_auto_send, friends_list, message_content)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)

