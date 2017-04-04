import cv2
import sys
import numpy as np
from PIL import Image
import pytesseract
from pytesseract import image_to_string
from matplotlib import pyplot as plt

im = cv2.imread('sample1.jpg')#sample6
#im = cv2.resize(im, (im.shape[1]*2, im.shape[0]*2))
im3 = im


#grayscale conversion
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#bluring
#blur = cv2.GaussianBlur(gray,(5,5),0)

#thresholding
ret,thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY_INV)
#ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#erosion and dilation
kernel = np.ones((3,3),np.uint8)
#thresh = cv2.dilate(thresh,kernel,iterations = 1)
#thresh = cv2.erode(thresh,kernel,iterations = 1)

#showing preprocessed image
cv2.imshow('Thresh',thresh)
cv2.waitKey(0)
im = thresh

img = Image.fromarray(im)
print pytesseract.pytesseract.tesseract_cmd
print image_to_string(img)#,config='-psm 7')


#****************************************SEGMENTING CHARACTERS********************************************
x, y = im.shape
#print x, y
horz_hist=np.sum(im==255, axis=0)
vert_hist=np.sum(im==255, axis=1)
print horz_hist
print vert_hist

def charactersegment(vert_hist, im)	:
	#print vert_hist
	count = 0
	x_temp = 0
	threshold = 5
	last_h = 0
	size = 0
	x1, y1 = im.shape
	print ""
	for x in np.nditer(vert_hist):
		size = size + 1
		if( x == 0):
			count = count + 1
		elif( count > threshold ):
			if last_h-1 < 0:
				last_h = 0
			i_temp = im[0:x1, (last_h ):size-(count/2) ]
			i_temp = 255 - i_temp
			word_image = cv2.copyMakeBorder(i_temp, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255,255,255]) 
			
			#print i_temp
			cv2.imshow('res\Character.png', word_image)
			img = Image.fromarray(word_image)
			#print "OUTPUT : "
			print image_to_string(img),#,config='-psm 10'), #psm = 10 is for reading the single characters instead of full page
			cv2.waitKey(0)
			last_h = size-(count/2)+1
			count = 0
		else:
			count = 0
		
#initializing values		
count = 0
x_temp = 0
threshold = 2
last_h = 0
size = 0

for x in np.nditer(vert_hist):
	size = size + 1
	if( x_temp == 0 and x == 0):
		count = count + 1
	elif( count > threshold ):
		i_temp = im[last_h:size-(count/2), 0:y]
		#print i_temp
		#cv2.imshow('Temp',i_temp)
		#cv2.waitKey(0)
		x1,y1 = i_temp.shape
		#print x1, y1
		horz_hist_t = np.sum(i_temp == 255, axis = 0 ) 
		print ''
		charactersegment(horz_hist_t,  i_temp )
		cv2.waitKey(0)
		last_h = size-(count/2)+1
		count = 0
	x_temp = x
		

	
plt.rcParams['figure.figsize'] = 10,4
fig = plt.figure()
plt.title(' horz. and vert. histogram respectively')
#fig.add_subplot(131)
#fig.imshow(im, plt.get_cmap('gray'))
fig.add_subplot(131)
plt.hist(vert_hist, range(0,x),alpha=0.8)
fig.add_subplot(132)
_=plt.hist(vert_hist, range(0,y),alpha=0.8 )
plt.show()


