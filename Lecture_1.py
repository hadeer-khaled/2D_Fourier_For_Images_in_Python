from matplotlib import pyplot as plt
from math import sqrt
from skimage.color import rgb2gray
from skimage.io import imread
import cv2
import numpy as np

fig, axs = plt.subplots(1,3) #axs is an array of axis
fig.set_size_inches(15, 10)


#===============Plot the Original Image==================#
im = cv2.imread("pepers.png")
#plt.imshow(im)
print(im.shape)
axs[0].imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))  #to convert from BGR to RGB


#===============Plot the Gray Image==================#

im_gray = rgb2gray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
print(im_gray.shape)
axs[1].imshow(im_gray, cmap=plt.get_cmap('gray'))


#===============Plot the MYGray Image==================#

im_gray_mine = np.full_like(im_gray, 0)#fill with Zeros
print('hello')
for x in range(im.shape[0]): #loop over the first index in shape tuple which is rows
    for y in range(im.shape[1]):#loop over the first index in shape tuple which is columns        
        im_gray_mine[x,y]=np.average(im[x,y,:])
axs[2].imshow(im_gray_mine, cmap=plt.get_cmap('gray'))

plt.show()

#===============Plot the All Image Versions==================#

fig1, axs1 = plt.subplots(2,3)
axs1[0,0].imshow(im)# im STILL in BGR
axs1[0,0].imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
axs1[0,1].imshow(im_gray,cmap=plt.get_cmap('gray'))#output of rgb2gray
axs1[1,0].imshow(im[:,:,0],cmap=plt.get_cmap('gray'))#b
axs1[1,1].imshow(im[:,:,1],cmap=plt.get_cmap('gray'))#g
axs1[1,2].imshow(im[:,:,2],cmap=plt.get_cmap('gray'))#r

plt.show()

fig1.set_size_inches(15, 10)

#=============== Plot the Histogram ==================#
# hist , edge_bin = np.histogram(data , numOfBins) 
# default number of bins = 10
# hist  gives the array of values of the 
# edge_bin which is an array of float datatype containing the bin edges

hist_gray, bins_gray=np.histogram(255*im_gray) 
hist_r, bins_r=np.histogram(im[:,:,2]) #r component....take care of the reversal of rgb #OpenCV
hist_g, bins_g=np.histogram(im[:,:,1]) #g component....take care of the reversal of rgb #OpenCV
hist_b, bins_b=np.histogram(im[:,:,0]) #b component....take care of the reversal of rgb #OpenCV

#.hist ==> plot a histogram.

fig, axs = plt.subplots(2,2, figsize=(15, 10))

axs[0,0].hist(255*im_gray, bins=bins_gray) 
axs[0,1].hist(im[:,:,0], bins=bins_b) 
axs[1,0].hist(im[:,:,1], bins=bins_g) 
axs[1,1].hist(im[:,:,2], bins=bins_r) 

plt.show()