#how to set properties to captured images
import cv2
cap = cv2.VideoCapture(0)# 3 and 4 are width and height properties
cap.set(3,1208)
cap.set(4,720)#set properties
#not supported resolutions will not work
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()