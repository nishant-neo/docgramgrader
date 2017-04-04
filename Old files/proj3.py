import sys
import numpy as np
import cv2
from PIL import Image
from pytesseract import image_to_string

from matplotlib import pyplot as plt
i = 171
while i > 0:
	#print i
	im = cv2.imread("res/" +  str(i) + ".jpg")
	im = cv2.resize(im, (im.shape[1]*3, im.shape[0]*3))
	im3 = im

	#grayscale conversion
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

	#bluring
	#blur = cv2.GaussianBlur(gray,(5,5),0)

	#thresholding
	#thresh = cv2.adaptiveThreshold(gray,  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,10) 
	ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#ret,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
	t = thresh.copy()

	#erosion and dilation
	kernel = np.ones((1,3),np.uint8)
	kernel1 = np.ones((2,1),np.uint8)
	#kernel1 = np.ones((1,1),np.uint8)
	#t = cv2.dilate(t,kernel,iterations = 1)
	#t = cv2.erode(t,kernel,iterations = 1)
	#thresh = cv2.dilate(thresh,kernel,iterations = 6)
	#thresh = cv2.erode(thresh,kernel1,iterations = 5)

	#sharpening the image
	t = 255-t
	ker = np.array(([0,-1,0],[-1,5,-1],[0,-1,0]), dtype = "int")
	rob_x = cv2.filter2D(t, -1, ker)
	#cv2.imshow('Thresholded Image inv',t)
	#cv2.waitKey(0)


	#output of tessrect
	img = Image.fromarray(t)
	print image_to_string(img),
	print " ",
	i = i - 1
	#cv2.waitKey(0)

