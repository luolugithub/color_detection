# -*- coding: utf-8 -*-
# @Time : 2020/3/10 上午11:17
# @Author : LuoLu
# @FileName: rightColor_detection.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

import cv2
import numpy as np
import imutils

img = cv2.imread('image/1.BMP')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([0, 136, 126])
upper_range = np.array([176, 255, 200])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

while (True):
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
