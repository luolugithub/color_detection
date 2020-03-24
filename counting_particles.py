# -*- coding: utf-8 -*-
# @Time : 2020/3/20 上午10:08
# @Author : LuoLu
# @FileName: counting_particles.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

import cv2
import pylab
from scipy import ndimage

im = cv2.imread('data/result_qaak/caol/2_mask_caolv.png')
pylab.figure(0)
pylab.imshow(im)
# cv2.imshow("src_img", im)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
maxValue = 255
adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C  # cv2.ADAPTIVE_THRESH_MEAN_C #cv2.ADAPTIVE_THRESH_GAUSSIAN_C
thresholdType = cv2.THRESH_BINARY  # cv2.THRESH_BINARY #cv2.THRESH_BINARY_INV
blockSize = 11  # odd number like 3,5,7,9,11
C = -3  # constant to be subtracted
im_thresholded = cv2.adaptiveThreshold(gray, maxValue, adaptiveMethod, thresholdType, blockSize, C)
labelarray, particle_count = ndimage.measurements.label(im_thresholded)
print('particle_count:', particle_count)
pylab.figure(1)
pylab.imshow(im_thresholded)
pylab.show()
