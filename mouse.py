#listen to mouse events
import numpy as np 
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event,x,y,fkags,param):#how mouse event handler functions are defined
    if event==cv2.EVENT_LBUTTONDOWN:
        print(str(x)+ ", "+str(y))
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Hello',(x,y),font,3,(255,0,0),3,cv2.LINE_AA)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        print(str(red)+ ", "+str(blue))
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Hello',(x,y),font,3,(255,255,0),3,cv2.LINE_AA)
        cv2.imshow('image',img)
        

img = cv2.imread('lena.png',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()