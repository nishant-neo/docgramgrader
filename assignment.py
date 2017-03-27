import sys

import numpy as np
import cv2

from matplotlib import pyplot as plt

im = cv2.imread('sample5.jpg')
im3 = im
im4 = im.copy()

#grayscale conversion
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#bluring
#blur = cv2.GaussianBlur(gray,(7,7),0)

#thresholding
ret,thresh = cv2.threshold(gray,110,255,cv2.THRESH_BINARY)

#erosion and dilation
kernel = np.ones((8,2),np.uint8)#3,2 and 8,5
#thresh = cv2.dilate(thresh,kernel,iterations = 4)
cv2.imshow('Dilated',thresh)
cv2.waitKey(0)




#################      Now finding Contours         ###################
mser = cv2.MSER_create()
regions = mser.detectRegions(thresh)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
cv2.polylines(im3, hulls, 3, (0,255,0)) 
cv2.imshow('norm',im3)
key = cv2.waitKey(0)

