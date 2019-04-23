import cv2

#start video capture from webcam
cap = cv2.VideoCapture(0)

#read first frame
ret,frame2=cap.read()
frame2=cv2.flip(frame2, +1);

while(True):
    #read each frame
    ret, frame = cap.read()
    print("captured")
    
    #flip image for proper direction
    frame=cv2.flip(frame, 1)
    
    #convert image to hsv for good color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    #Color detection
    sensitivity=10
    lower_green=(60 - sensitivity, 75, 50)
    upper_green=(60 + sensitivity, 255, 255)
    #mask 1 to detect green color and filter out green region
    mask=cv2.inRange(hsv,lower_green,upper_green)
    #inverse mask to keep regions with green and filter out rest
    mask_inv=cv2.bitwise_not(mask)
    
    #foreground video frame.. green is filtered out using mask 1
    fg=cv2.bitwise_and(frame,frame,mask=mask_inv)
    
    #still frame captured at first.. green region is kept and  rest is filtered out
    bg=cv2.bitwise_and(frame2,frame2,mask=mask)
    print("masked")
    
    #added both frames to create composite
    final=cv2.add(fg,bg)
    
    #show frame
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', (1000,1000))
    cv2.imshow('frame',final)
    print("out\n")
    
    #wait for q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release camera and destroy window
cap.release()
cv2.destroyAllWindows()