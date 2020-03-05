# -*- coding: utf-8 -*-
# @Time : 2020/3/5 下午2:22
# @Author : LuoLu
# @FileName: contour_detection.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

import cv2
import matplotlib.pyplot as plt

# read the image
image = cv2.imread("result/mask_red.png")
height, width, channels = image.shape
print("src h w c:", height, width, channels)
plt.axis('off')

# # convert to RGB
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#
# # create a binary thresholded image
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
print("binary h w :", binary.shape)
# # show it
# plt.imshow(binary, cmap="gray")
# plt.show()

# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 2)

# show the image with the drawn contours
# plt.imshow(image)
cv2.imwrite("result/contour_red.png", image)
# plt.show()
