# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:WeiFeng Liu
# @Time: 2021/12/9 下午6:41

import cv2
import numpy as np
import os
from PIL import Image
def tif_to_png(image_path,save_path):
    """
    :param image_path: *.tif image path
    :param save_path: *.png image path
    :return:
    """
    img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    # print(img)
    # print(img.dtype)
    filename = image_path.split('/')[-1].split('_')[0]
    filename=filename.split('.')[0]
    save_path = save_path + '/' + filename + '.png'
    cv2.imwrite(save_path,img)
def changePixel():
    path = r'E:/setup/UNet_Demo/UNet_Demo/NanKai/train/label/EX_new/'
    savedpath = r'E:/setup/UNet_Demo/UNet_Demo/NanKai/train/label/EX_res/'
    filelist = os.listdir(path)
    for item in filelist:
        im = Image.open(path + item) #打开图片
        width = im.size[0] #获取宽度
        height = im.size[1] #获取长度
        for x in range(width):
            for y in range(height):
                r,g,b = im.getpixel((x,y))	
                if r+g+b>0:
                   im.putpixel((x,y),(1,1,1))
        im = im.convert('RGB')
        im.save(savedpath + item)
def gray():
    path = r'E:/setup/UNet_Demo/UNet_Demo/NanKai/train/image/'
    savepath = r'E:/setup/UNet_Demo/UNet_Demo/NanKai/train/new_image/'
    filelist=os.listdir(path)
    for item in filelist:
        image = cv2.imread(path+item, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(savepath+item, image)
def hw(strJpgFile, strSaveDir, width=512, height=512):
    img_src = Image.open(strJpgFile)
    img_dst = img_src.resize((width, height), Image.LANCZOS) # 得到的图像在抗锯齿和保留锐利边缘的效果较好
    img_dst.save(os.path.join(strSaveDir, os.path.basename(strJpgFile)))
def mergeData(ex_data,ha_data,se_data,ma_data,pic_name,save_path):
    ex=np.array(Image.open(ex_data+pic_name))
    ha=np.array(Image.open(ha_data+pic_name))
    se=np.array(Image.open(se_data+pic_name))
    ma=np.array(Image.open(ma_data+pic_name))
    ex=ex+ha*2+se*3+ma*4
    ex=Image.fromarray(ex)
    ex.save(save_path+pic_name)
    
def merge():
    ex_path="E:\\setup\\UNet_Demo\\eyedetect\\NanKai\\train\\label\\EX_01\\"
    ha_path="E:\\setup\\UNet_Demo\\eyedetect\\NanKai\\train\\label\\HE_01\\"
    se_path="E:\\setup\\UNet_Demo\\eyedetect\\NanKai\\train\\label\\SE_01\\"
    ma_path="E:\\setup\\UNet_Demo\\eyedetect\\NanKai\\train\\label\\MA_01\\"
    save_path="E:\\setup\\UNet_Demo\\eyedetect\\NanKai\\train\\label\\num_label\\"
    image_files=os.listdir(ex_path)
    for item in image_files:
        mergeData(ex_path,ha_path,se_path,ma_path,item,save_path)

    
if __name__ == '__main__':
    root_path = r'E:/setup/UNet_Demo/eyedetect/NanKai/train/label/SE/'
    save_path = r'E:/setup/UNet_Demo/eyedetect/NanKai/train/label/SE_new'
    image_files = os.listdir(root_path)
    merge()
    #for item in image_files:
    #    tif_to_png(root_path+item,save_path)
    #gray()