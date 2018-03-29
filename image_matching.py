import numpy as np 
import cv2

img=cv2.imread('stones.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Image Capture
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#In case we need the image frame from video continuously
'''
i=0
while i<=0:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    i=i+1
'''

#Template matching
w,h=img2.shape[::-1]
res=cv2.matchTemplate(img1,img2,cv2.TM_CCOEFF_NORMED)
#threshold for image to match=80%
threshold=0.80

#Checking if Image is in the frame
while(True):
    if np.any(res>=threshold):
        loc=np.where(res>=threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h), (0,255,255),2)
        cv2.imshow('detected',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('Image in the frame')

    else:
        print('Image not found')
