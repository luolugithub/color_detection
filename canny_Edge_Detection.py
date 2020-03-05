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

img = cv.imread('image/tedt.jpg', 0)
edges = cv.Canny(img, 480, 384)
plt.axis('off')
# plt.imshow(img, cmap='gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.imshow(edges,  cmap='Blues')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.savefig("result/edge_blue.png")
plt.show()
