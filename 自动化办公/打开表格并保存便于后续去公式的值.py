import time
import os
import win32com.client
from win32com.client import Dispatch

def just_open(filename):
    try:
        xlApp = Dispatch("Excel.Application")
        xlApp.Visible = False
        xlBook = xlApp.Workbooks.Open(filename)
        xlBook.Save()
        xlBook.Close()
        xlApp.Quit()
        print(f"文件 {filename} 处理成功。")
    except Exception as e:
        print(f"处理文件 {filename} 时出现错误: {e}")

def operate_excel_file(file_path):
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            print(f"错误：文件 '{file_path}' 不存在")
            return False

        # 创建Excel应用实例
        print("正在启动Excel...")
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = True  # 使Excel可见

        # 打开指定文件
        print(f"正在打开文件: {file_path}")
        workbook = excel.Workbooks.Open(file_path)

        # 保存文件
        print("正在保存文件...")
        workbook.Save()
        time.sleep(1)  # 等待保存完成

        # 关闭文件
        print("正在关闭文件...")
        workbook.Close(SaveChanges=False)  # 已经保存过，不需要再次保存

        # 退出Excel应用
        excel.Quit()

        # 释放COM对象
        del workbook
        del excel

        print("操作完成")
        return True

    except Exception as e:
        print(f"发生错误: {e}")
        return False


if __name__ == "__main__":
    file_path = r"C:\Users\Administrator\测试项目\项目管理委员会周报\02_pmo例会机制材料v1 20250701公司整体1.xlsx"
    operate_excel_file(file_path)    