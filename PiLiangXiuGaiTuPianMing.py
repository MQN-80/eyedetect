import os

class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = 'G:/Code/Matalab/ColorTransfer/Save_Images'  #表示需要命名处理的文件夹
        self.save_path='G:/Code/Matalab/ColorTransfer/Save_Images_2'#保存重命名后的图片地址
    def rename(self):
        filelist = os.listdir(self.path) #获取文件路径
        total_num = len(filelist) #获取文件长度（个数）
        i = 1  #表示文件的命名是从1开始的
        for item in filelist:
            print(item)
            if item.endswith('.jpg'):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)#当前文件中图片的地址
                dst = os.path.join(os.path.abspath(self.save_path), ''+str(i) + '.jpg')#处理后文件的地址和名称,可以自己按照自己的要求改进
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()

