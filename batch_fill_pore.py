# -*- coding: utf-8 -*-
# @Time : 2020/3/24 上午11:13
# @Author : LuoLu
# @FileName: batch_fill_pore.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

import glob
import os

import numpy as np
import cv2 as cv
from PIL import Image
from matplotlib import pyplot as plt

root_path = '/home/luolu/PycharmProjects/color_detection'

if __name__ == '__main__':
    base_name = ''
    for filename in glob.glob(root_path + '/data/result_qaak/caol/*.png'):
        img = cv.imread(filename)
        base_name = os.path.basename(filename)
        height, width, channels = img.shape
        print(base_name)
        print(height, width, channels)
        # Load in image, convert to grayscale, and threshold
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

        # Close contour
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 1))
        close = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=1)

        # Find outer contour and fill with white
        cnts = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        cv.fillPoly(close, cnts, [255, 255, 255])

        # save
        cv.imwrite(root_path + "/data/result_qaak/pore_filled_caol/" + base_name, close)
