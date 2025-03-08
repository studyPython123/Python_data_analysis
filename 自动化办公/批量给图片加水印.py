# Author: 邵世昌
# CreatTime: 2024/11/23
# FileName: 批量给图片加水印
# 没有写入权限
from PIL import Image,ImageDraw,ImageFont, ImageEnhance
import os
# %%
def add_watermark(input_folder,output_folder,watermark_path,position=(0,0),opacity = 128):
    # input_folder 是输入图片所在地的文件夹路径
    # output_folder 是添加完水印后的图片保存路径
    # watermark_path 是水印的路径
    # position 是水印图片的位置，（0，0）是右下角
    # opacity 水印的不透明度0-255
    watermark = Image.open(watermark_path).convert('RGBA')
    # 调整水印不透明度
    if opacity < 255:
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity/255.0)
        watermark.putalpha(alpha)
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg','.jpeg','.png')):
            im = Image.open(os.path.join(input_folder,filename)).convert("RGBA")
            # 创建空图片
            layer = Image.new("RGBA", im.size, (0,0,0,0))
            # 在空图片上面添加图片和水印
            layer.paste(im,position)
            layer.paste(watermark,position,watermark)
            # 完成的图片保存为RGB，以便于保存为jpg
            final_im = layer.convert("RGB")
            # 如果没有输出文件夹则创建文件夹
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            # final_im.save(os.path.join(output_folder,filename))
            print(f'Processed {filename}')
#%%
input_folder = r'C:\Users\25782\Desktop\图片'
output_folder = r'C:\Users\25782\Desktop\水印\OIP-C.jpg'
watermark_path = r'C:\Users\25782\Desktop\图片'
add_watermark(input_folder,output_folder,watermark_path,position=(0,0),opacity=128)