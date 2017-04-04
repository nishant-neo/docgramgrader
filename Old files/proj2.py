import sys
import numpy as np
import cv2
from PIL import Image
from pytesseract import image_to_string
from skimage.filters

from matplotlib import pyplot as plt

im = cv2.imread('sample5.jpg')
im = cv2.resize(im, (im.shape[1]*2, im.shape[0]*2))
im3 = im

#grayscale conversion
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#bluring
#blur = cv2.GaussianBlur(gray,(5,5),0)

#thresholding
#thresh = cv2.adaptiveThreshold(gray,  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,10) 
ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
t = thresh.copy()
#erosion and dilation
kernel = np.ones((0,3),np.uint8)
kernel1 = np.ones((2,1),np.uint8)
#kernel1 = np.ones((1,1),np.uint8)
#t = cv2.dilate(t,kernel,iterations = 1)
#t = cv2.erode(t,kernel,iterations = 1)
thresh = cv2.dilate(thresh,kernel,iterations = 4)
#thresh = cv2.erode(thresh,kernel1,iterations = 5)

#sharpening the image
t = 255-t
ker = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), dtype = "int")
rob_x = cv2.filter2D(t, -1, ker)
cv2.imshow('Thresholded Image inv',t)
cv2.waitKey(0)

cv2.imshow('Thresholded Image',thresh)
cv2.waitKey(0)

raw_input()

"""
t = thresh.copy()
t = 255-t
cv2.imshow('Thresholded Image inv',t)
img = Image.fromarray(t)
print image_to_string(img)
cv2.waitKey(0)
"""





#################      Now finding Contours         ###################

_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE,offset=(1, 1))
samples =  np.empty((0,100))
responses = []
keys = [i for i in range(48,58)]

i = 0
for cnt in contours:
    if cv2.contourArea(cnt)>100:
        [x,y,w,h] = cv2.boundingRect(cnt)
        cv2.rectangle(im,(x-2,y-5),(x+w+2,y+h+5),(0,255,0),1)
        roi = thresh[y:y+h,x:x+w]
        roismall = cv2.resize(roi,(10,10))	
        cv2.imwrite("res/"+ str(i)+".jpg",t[y-3:y+h+3,x:x+w])
        i = i + 1
		

           
cv2.imshow('Image with Bounding Boxes',im)
key = cv2.waitKey(0)
if key == 27:  # (escape to quit)
	sys.exit()
if key in keys:
    responses.append(int(chr(key)))
    sample = roismall.reshape((1,100))
    samples = np.append(samples,sample,0)

	
"""
#*************************************BLOB DETECTION***********************************************
im = gray
ret,thresh = cv2.threshold(im,90,255,cv2.THRESH_BINARY)
kernel = np.ones((1,1),np.uint8)
thresh = cv2.erode(thresh,kernel,iterations = 1)
im = thresh


# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

#color
params.blobColor = 0
params.filterByColor = True;
params.filterByConvexity = False;
params.filterByInertia = False;
params.filterByCircularity = False;
params.filterByArea = True;
params.minArea = 1; 
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
"""
