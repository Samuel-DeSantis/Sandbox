# Thresholding Example: 05-08-2020
# Static thresholding using global value
# cv2.threshold('image', threshold value, maxVal, thresholding style)
# 1 image should be in greyscale
# 2 threshold value is used to classify the pixel value
# 3 maxVal represents the val given if the pixel is < threshold val
# 4 thresholding style: Bin., Bin Inv. Trunc, To Zero, To Zero Inv.
# generates retval and thresholded images

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# Adaptive Thresholding Example: 05-08-2020
# thresholding using dynamic thresholding value
# 3 special input params and one output params
