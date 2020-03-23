import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('Output_file.avi',fourcc,20.0,(640,480)) #to store the video being captured fourcc
cap = cv2.VideoCapture(0) #can be 0,1,-1
while(True): #You can us cap.isOpened() to check if video path is right or wrong
    ret,frame= cap.read() #return true if frame is available and store in frame 
    if ret==True:
        out.write(frame) #writing the video to output file
        cap.get(cv2.CAP_PROP_FRAME_WIDTH) #width of frame
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #height of frame
        print(cap.get(cv2.CAP_PROP_FPS)) #fps

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #getting grayscale image
        cv2.imshow('Name_of_Window',gray) #showing the captured frame
        if cv2.waitKey(1) & 0xFF == ord('q'): #taking user input
            break
    else:
        break

cap.release() #releasing the resources
out.release() #releasing the resources