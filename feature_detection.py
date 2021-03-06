import cv2
import numpy as np
from pylab import *
from numpy import *

filename = 'stones.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Check corners using Harris Corner Detection
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,7,0.1)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

print(dst)

cv2.imshow('stones',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

