# 将视频导出为若干帧图片
DATA_DIR = "‪G:\\Infrared\\2022.9.26\\1.avi"  # 视频存放路径
SAVE_DIR = "G:\\Infrared\\2022.9.26\\Images_1\\"  # 帧图片保存路径
# GAP = 30  # 每隔多少帧导出一张图片
GAP = 1  # 每隔多少帧导出一张图片

import cv2  # OpenCV库
import os

def getphoto(video_in, video_save):
    number = 0
    cap = cv2.VideoCapture(video_in)  # 打开视频文件
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 视频的帧数
    fps = cap.get(cv2.CAP_PROP_FPS)  # 视频的帧率
    dur = n_frames / fps  # 视频的时间
    num_frame = 0
    judge = cap.isOpened()
    while judge:
        flag, frame = cap.read()  # flag是读取状态，frame下一帧
        if cv2.waitKey(0) == 27:
            break
        if flag:
            num_frame += 1
            if num_frame % GAP == 0:
                print("正在保存第%d张照片" % number)
                cv2.imwrite(video_save + '/' + str(number) + '.jpg', frame)  # cv2.imwrite(‘路径’ + ‘名字’ + ‘后缀’， 要存的帧)
                number += 1
        else:
            break

    print("视频时长: %d 秒" % dur)
    print("视频共有帧数: %d 保存帧数为: %d" % (n_frames, number))
    print("每秒的帧数(FPS): %.1lf" % fps)


def main_1(path):
    video_in = path
    video_save = SAVE_DIR
    getphoto(video_in, video_save)

if __name__ == '__main__':
    paht = DATA_DIR  # 视频路径
    main_1(paht)
