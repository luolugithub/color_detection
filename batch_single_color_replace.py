# -*- coding: utf-8 -*-
# @Time : 2020/3/5 上午9:46
# @Author : LuoLu
# @FileName: single_color_replace.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import glob
import os

import cv2 as cv
import numpy as np
from PIL import Image
import numpy as np

# im = Image.open('result/mask_1Illite.png')
# im = im.convert('RGBA')
#
# data = np.array(im)  # "data" is a height x width x 4 numpy array
# print(data.shape)
# red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability
#
# # Replace white with red... (leaves alpha values alone...)
# white_areas = (red == 255) & (blue == 255) & (green == 255)
# data[..., :-1][white_areas.T] = (0, 192, 0)  # Transpose back needed
#
# #
# im2 = Image.fromarray(data)
# im2.save("result/mask1Illite.png")
# im2.show()

if __name__ == '__main__':
    for filename in glob.glob('/home/luolu/PycharmProjects/color_detection/data/result_qaak/lb/*.png'):
        img = cv.imread(filename)
        # print(filename)
        base_name = os.path.basename(filename)
        print(base_name)
        im = Image.open(filename)
        im = im.convert('RGBA')

        data = np.array(im)  # "data" is a height x width x 4 numpy array
        print(data.shape)
        red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability

        # Replace white with red... (leaves alpha values alone...)
        white_areas = (red == 255) & (blue == 255) & (green == 255)
        data[..., :-1][white_areas.T] = (0, 255, 255)  # Transpose back needed

        #
        im2 = Image.fromarray(data)
        im2.save("/home/luolu/PycharmProjects/color_detection/data/result_qaak/lightblue_mask/" + base_name)
