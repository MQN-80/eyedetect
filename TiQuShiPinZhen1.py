# '''
# 批量提取视频的所有帧
# '''
# import os
# import cv2
# #存放视频的地址
# videos_src_path = 'F:/Code/OpenCv_Python/Improve/Stripe/Images/XiaoBo/People/wh3/ExperimentalImage3/ZhiFanTuJunHenHua/Cheng_Teacher_Video/Short.avi'
# #存放图片的地址
# videos_save_path = 'F:/Code/OpenCv_Python/Improve/Stripe/Images/XiaoBo/People/wh3/ExperimentalImage3/ZhiFanTuJunHenHua/Cheng_Teacher_Video/Images'
# #返回videos_src_path路径下包含的文件或文件夹名字的列表（所有视频的文件名），按字母顺序排序
# videos = os.listdir(videos_src_path)
#
# for each_video in videos:
#     #获取每个视频的名称
#     each_video_name, _ = each_video.split('.')
#     #创建目录，来保存图片帧
#     os.mkdir(videos_save_path + '/' + each_video_name)
#     #获取保存图片的完整路径，每个视频的图片帧存在以视频名为文件名的文件夹中
#     each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'
#     #获取每个视频的完整路径
#     each_video_full_path = os.path.join(videos_src_path, each_video)
#     #读入视频
#     #cap = cv2.VideoCapture(each_video_full_path)
#     cap = cv2.VideoCapture(videos_src_path)
#     frame_count = 1
#     success = True
#     while (success):
#         #提取视频帧，success为是否成功获取视频帧（true/false），第二个返回值为返回的视频帧
#         success, frame = cap.read()
#         if success == True:
#             #存储视频帧
#             cv2.imwrite(each_video_save_full_path + "%06d.jpg" % frame_count, frame)
#         frame_count = frame_count + 1


'''
提取单个视频的所有帧
'''
import cv2
import numpy as np
def save_image(image,addr,num):
    #存储的图片路径
    address=addr+str(num)+'.jpg'
    #存储图片
    cv2.imwrite(address,image)
#读入视频
videoCapture=cv2.VideoCapture("G:/Code/Matalab/ColorTransfer/video/park.avi")
#读取视频帧
success,frame=videoCapture.read()
i=0
while success:
    i=i+1
    #保存图片
    # save_image(frame,'Images/photo/Images',i)
    save_image(frame, 'G:/Code/Matalab/ColorTransfer/Video_Images_Park/', i)
    if success:
        print('save image:',i)
    #读取视频帧
    sucess,frame=videoCapture.read()

