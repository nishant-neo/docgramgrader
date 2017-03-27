import sys

import numpy as np
import cv2

from matplotlib import pyplot as plt

im = cv2.imread('highway2.png')
im3 = im

# Convert BGR to HSV

im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(im, cv2.GRAY2HSV)

#thresholding
ret,im = cv2.threshold(im,127,255,cv2.THRESH_BINARY)

# define range of white color in HSV
lower_blue = np.array([0,0,0])
upper_blue = np.array([0,0,255])

# Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(im,im, mask= mask)

cv2.imshow('frame',im)
key = cv2.waitKey(0)
cv2.imshow('mask',mask)
key = cv2.waitKey(0)
cv2.imshow('res',res)
key = cv2.waitKey(0)



cv2.destroyAllWindows()