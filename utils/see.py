
#showPixelValue.py

import cv2
import sys

def getMousePos(imgName):
  def onmouse(event, x, y, flags, param):   
    cv2.imshow("img",img)
    #if event==cv2.EVENT_MOUSEMOVE:     
      #print(img[y,x], " pos: ", x, " x ", y) 
      
    #双击左键，显示鼠标位置
    if event == cv2.EVENT_LBUTTONDBLCLK:
      strtext = "(%s,%s)"%(x,y)
      print(img[y,x])
      cv2.circle(img,(x,y),2,(0,0,255),-1)
      cv2.putText(img, strtext, (x+2, y+15) ,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,200),2)
 	
  cv2.namedWindow("img", cv2.WINDOW_NORMAL)   
  img= cv2.imread(imgName)  
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
  arg1 = 'E:\\setup\\UNet_Demo\\UNet_Demo\\Medical_Datasets\\Labels\\0.png'
  arg1='E:\\setup\\UNet_Demo\\UNet_Demo\\NanKai\\train\\label\\EX_new\\007-3336-200.png'
  getMousePos(arg1)
