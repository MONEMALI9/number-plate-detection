'''
    monem
    number plate detection
'''

# libraries

import numpy as np
import cv2
import sys

frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height

'''
   file type : xml file  (haarcascade)
   purpose   : recognise number plate
   
'''
plate = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

minarea = 500

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,franeHeight)
cap.set(10,150)
count = 0


while True:
    success,img = cap.read()
    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
    
    numberplate = plate .detectMultiScale(imggray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    
    for(x,y,w,h) in numberplate:
        area = w*h
        if area > minarea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
        
    cv2.imshow("result",img)
    
    
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("E:/project/ali shalaby/video"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
    # cv2.imwrite('test_output'+img_path[i].split('/')[-1],orig_frame)   
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        sys.exit("System Exit ...... THANKS")
        break
