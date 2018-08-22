import cv2
import numpy as np

face_cas=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cas=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cas.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+w),(200,120,12),2)
        roi_gray=gray[y:y+h,x:x+h]
        roi_color=img[y:y+h,x:x+h]
        eyes=eye_cas.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(225,200,120),2)

    cv2.imshow('img',img)
    k=cv2.waitKey(30)&0xFF
    if k==27:
        break;
cap.release()
cv2.destroyAllWindows()

