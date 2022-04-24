import cv2
from cv2 import waitKey
import numpy as np

video=cv2.VideoCapture('D:\VSC\PCV\mbruh.mp4')
image=cv2.imread("D:\VSC\PCV\ww2.jpg")

#def nothing():
   # pass

#cv2.namedWindow("Pengaturan warna")
#cv2.resizeWindow("Pengaturan warna",480,640)

#cv2.createTrackbar('L-H',"Pengaturan warna",0,179, nothing)
#cv2.createTrackbar('L-S',"Pengaturan warna",0,255, nothing)
#cv2.createTrackbar('L-V',"Pengaturan warna",0,255, nothing)
#cv2.createTrackbar('U-H',"Pengaturan warna",179,179, nothing)
#cv2.createTrackbar('U-S',"Pengaturan warna",255,255, nothing)
#cv2.createTrackbar('U-V',"Pengaturan warna",255,255, nothing)

while True:
    ret,frame=video.read()
    frame=cv2.resize(frame,(480,640))
    image=cv2.resize(image,(480,640))
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #l_h=cv2.getTrackbarPos('L-H',"Pengaturan warna")
    #l_s=cv2.getTrackbarPos('L-S',"Pengaturan warna")
    #l_v=cv2.getTrackbarPos('L-V',"Pengaturan warna")
    #u_h=cv2.getTrackbarPos('U-H',"Pengaturan warna")
    #u_s=cv2.getTrackbarPos('U-S',"Pengaturan warna")
    #u_v=cv2.getTrackbarPos('U-V',"Pengaturan warna")
    #l_white=np.array([l_h,l_s,l_v])
    #u_white=np.array([u_h,u_s,u_v])
    l_white=np.array([0,0,200])
    u_white=np.array([179,154,255])
    mask=cv2.inRange(hsv,l_white,u_white)
    res=cv2.bitwise_and(frame,frame,mask=mask )
    (framebaru)=frame-res
    hasil=np.where(framebaru==0,image,framebaru)
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("Hasil",hasil)
    cv2.imshow("framebaru",framebaru)
    k=cv2.waitKey(120) 
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()