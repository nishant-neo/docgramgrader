import cv2
import Image
import numpy as np
from pytesseract import image_to_string


img = cv2.imread('sample5.jpg')
img = img[5:-5,5:-5,:]
mser = cv2.MSER_create()

#Resize the image so that MSER can work better
img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im = gray
ret,thresh = cv2.threshold(im,200,255,cv2.THRESH_BINARY)
#kernel = np.ones((1,1),np.uint8)
#kerne = np.ones((2,2),np.uint8)
#thresh = cv2.erode(thresh,kernel,iterations = 5)
#thresh = cv2.dilate(thresh,kerne,iterations = 2)
gray = thresh
cv2.imshow('img', gray)
cv2.waitKey(0)
vis = img.copy()

regions = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
#print hulls

cv2.polylines(vis, hulls, 1, (0,255,0)) 

cv2.namedWindow('img', 0)
cv2.imshow('img', vis)
while(cv2.waitKey()!=ord('q')):
    continue
cv2.destroyAllWindows()