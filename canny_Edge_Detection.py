# -*- coding: utf-8 -*-
# @Time : 2020/3/5 上午11:18
# @Author : LuoLu
# @FileName: canny_Edge_Detection.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cmap = plt.cm.gray
cmap.set_bad((1, 0, 0, 1))

img = cv.imread('result/mask_blue.png', 0)
edges = cv.Canny(img, 1001, 1001, edges=200, apertureSize=7)
plt.axis('off')


# plt.imshow(edges,  cmap='Blues')
cv.imwrite("result/canny_edge_blue.png", edges)

