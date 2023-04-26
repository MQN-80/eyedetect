
#showPixelValue.py

import cv2
import sys

def getMousePos(imgName):
  def onmouse(event, x, y, flags, param):   
    cv2.imshow("img",img)
    #if event==cv2.EVENT_MOUSEMOVE:     
      #print(img[y,x], " pos: ", x, " x ", y) 
      
    #双击左键，显示鼠标位置
    if event == cv2.EVENT_MBUTTONDBLCLK:
      strtext = "(%s,%s)"%(x,y)
      print(img[y,x])
 	
  cv2.namedWindow("img", cv2.WINDOW_NORMAL)   
  img= cv2.imread(imgName)
  print(img[img>4]) 
  print(img.shape)  
    
  cv2.setMouseCallback("img", onmouse)   
  
  if cv2.waitKey() & 0xFF == 27: #按下‘q'键，退出
    cv2.destroyAllWindows()         
	
	
def showPixelValue(imgName):

  img= cv2.imread(imgName)          
  def onmouse(event, x, y, flags, param):   
    if event==cv2.EVENT_MOUSEMOVE:     
      print(img[y,x]) 
      
  cv2.namedWindow("img")         
  cv2.setMouseCallback("img", onmouse)   
  cv2.imshow("img",img)        
  if cv2.waitKey() == ord('q'): #按下‘q'键，退出
    cv2.destroyAllWindows()         
  
if __name__ == '__main__':          
  arg1 = 'E:\\setup\\UNet_Demo\\eyedetect\\NanKai\\train\\label\\num_label\\007-6361-400.png'
  #E:\\setup\\UNet_Demo\\eyedetect\\NanKai\\train\\label\\EX_01\\007-1774-100.png
  #E:\\setup\\UNet_Demo\\eyedetect\\miou_out\\HE_res\\007-6361-400.png
  getMousePos(arg1)
