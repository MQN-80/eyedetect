import os
import shutil

## 新建目标文件夹
IsExists = os.path.exists('G:\\Infrared\\Video_2022915\\Visibel Choose')    ##在目录中新建一个文件夹
if not IsExists:
    os.makedirs("G:\\Infrared\\Video_2022915\\Visibel Choose")
else:
    print("目录已存在")
new_img_folder = "G:\\Infrared\\Video_2022915Visibel Choose"

## 遍历读取文件夹筛选符合标准的图片
dir_path = "G:/Infrared/Video_2022915/Images/Visible_Images"       ## 将原始的数据集文件路径加载进来
for root,dirs,files in os.walk(dir_path):
    for file in files:
        num_name = file.rstrip(".jpg")   ## 将图片名末尾的.jpg去掉
        num_name_int = int(num_name)
        if num_name_int % 3 == 0:
            shutil.copy(os.path.join(root, file), new_img_folder)
