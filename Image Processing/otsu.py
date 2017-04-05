import matplotlib
import matplotlib.pyplot as plt
import cv2
from numpy import *


# all the image processing code comes from scipy and pylab
from pylab import *
from scipy.stats.stats import trim1
from multiprocessing import Pool
from scipy.ndimage import measurements,interpolation
from scipy.misc import imsave

import os,os.path
from pylab import *
from scipy.ndimage import measurements,interpolation,filters,morphology
import math

im = cv2.imread('sample3.jpg')
im = cv2.resize(im, (im.shape[1]*3, im.shape[0]*3))
image = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
def gsauvola(image,sigma=150.0,R=None,k=0.3,filter='uniform',scale=2.0):
    """Perform Sauvola-like binarization.  This uses linear filters to
    compute the local mean and variance at every pixel."""
    if image.dtype==dtype('uint8'): image = image / 256.0
    if len(image.shape)==3: image = mean(image,axis=2)
    if filter=="gaussian":
        filter = filters.gaussian_filter
    elif filter=="uniform":
        filter = filters.uniform_filter
    else:
        pass
    scaled = interpolation.zoom(image,1.0/scale,order=0,mode='nearest')
    s1 = filter(ones(scaled.shape),sigma)
    sx = filter(scaled,sigma)
    sxx = filter(scaled**2,sigma)
    avg_ = sx / s1
    stddev_ = maximum(sxx/s1 - avg_**2,0.0)**0.5
    s0,s1 = avg_.shape
    s0 = int(s0*scale)
    s1 = int(s1*scale)
    avg = zeros(image.shape)
    interpolation.zoom(avg_,scale,output=avg[:s0,:s1],order=0,mode='nearest')
    stddev = zeros(image.shape)
    interpolation.zoom(stddev_,scale,output=stddev[:s0,:s1],order=0,mode='nearest')
    if R is None: R = amax(stddev)
    thresh = avg * (1.0 + k * (stddev / R - 1.0))
    return array(255*(image>thresh),'uint8')

im = gsauvola(image)
cv2.imshow("dcd",image)
cv2.imshow("dcdee",im)
cv2.waitKey()