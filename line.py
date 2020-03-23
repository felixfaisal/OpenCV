import numpy as no 
import cv2
img=cv2.imread('lena.png',1)#reading the image from file
img=cv2.line(img,(0,0),(2000,2000),(255,204,0),20) #BGR Format
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),26)
cv2.imshow('image',img)#showing the image
cv2.waitKey(0)
cv2.destroyAllWindows()