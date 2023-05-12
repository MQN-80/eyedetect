import cv2
import numpy as np
import os
from PIL import Image
import re
# 读入图像
input=r'Nankai/train/image'
input_label=r'Nankai/train/label/num_label'
out=r'Nankai/train/image_tile/'
output_label=r'Nankai/train/label/tile_label/'
if not out:
    os.makedirs(out)
if not output_label:
    os.makedirs(output_label)

# 获取输入图像的尺寸
def tile(img,outdir,filename,output_label):
    height, width, channels = img.shape
    # 指定每个图像块的大小
    block_size = 512

    # 计算在宽度和高度上应该分成多少个块
    num_blocks_wide = int(np.ceil(width / block_size))
    num_blocks_high = int(np.ceil(height / block_size))
    # 计算宽度和高度上需要填充的像素数
    pad_width = ((0, num_blocks_high * block_size - height),
                (0, num_blocks_wide * block_size - width),
                (0, 0))
    # 对图像进行镜像填充
    padded_img = np.pad(img, pad_width, mode='reflect')
    # 切割图像并保存到磁盘
    for i in range(num_blocks_high):
        for j in range(num_blocks_wide):
            # 计算当前块在填充后图像中的位置
            start_x = j * block_size
            start_y = i * block_size
          
            # 切割出当前块
            block = padded_img[start_y:start_y+block_size, start_x:start_x+block_size, :]
            if len(block[block!=0])<100*100:
                continue
            #print(outdir+'output_image_{i*num_blocks_wide+j}.jpg')
            # 将当前块保存到磁盘
            cv2.imwrite(outdir+f'{filename}_{i*num_blocks_wide+j}.jpg', block)
            cv2.imwrite(output_label+f'{filename}_{i*num_blocks_wide+j}.png', block)
win_size = 64
step =64
def Spilt():
# 打开待切割的图像文件
    img = Image.open('result.jpg')

    # 获取图像大小
    width, height = img.size

    # 遍历图像并切割为指定大小的图像块
    for i in range(0, height-win_size, step):
        for j in range(0, width-win_size, step):
            # 切割出当前位置的图像块
            box = (j, i, j+win_size, i+win_size)
            img_block = img.crop(box)

            # 判断当前图像块中黑色像素占比是否超过一半
            img_data = np.array(img_block)
            if np.mean(img_data == 0) <= 0.1:
                # 将当前图像块保存到指定路径中
                img_block.save(os.path.join('Nankai/label', f'block_{i}_{j}.jpg'))
Spilt()
