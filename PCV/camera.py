
import cv2 as cv
import numpy as np
import random
import math as mt 



cap = cv.VideoCapture(3)

while True:
    ret, frame = cap.read()
    cv.imshow('frame3', frame)
  
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
