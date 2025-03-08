# Author: 邵世昌
# CreatTime: 2024/11/23
# FileName: 批量识别图片中的文字
import pytesseract
from PIL import Image
import os
def ocr_on_image_folder(folder_path):
    pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
    if not os.path.exists(folder_path):
        print('提供的路径不是一个目录')
        return
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg','.png','.jpeg')):
            image_path = os.path.join(folder_path, filename)
            print(f'正在识别图片：{image_path}')
            text = pytesseract.image_to_string(Image.open(image_path),lang='chi_sim')
            print(text)
image_folder_path = r'C:\Users\25782\Desktop\图片'
ocr_on_image_folder(image_folder_path)