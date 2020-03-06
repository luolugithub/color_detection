# -*- coding: utf-8 -*-
# @Time : 2020/3/6 上午11:22
# @Author : LuoLu
# @FileName: composite_img.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import numpy
from PIL import Image
import cv2 as cv

background = Image.new('RGB', (1001, 1001), color='black').convert('RGBA')

foreground1 = Image.open("result/red_mask_transparent.png").convert('RGBA')
foreground2 = Image.open("result/green_mask_transparent.png").convert('RGBA')
foreground3 = Image.open("result/maskBlue_transparent.png").convert('RGBA')
foreground4 = Image.open("result/maskFen_transparent.png").convert('RGBA')
foreground5 = Image.open("result/maskShenzi_transparent.png").convert('RGBA')
foreground6 = Image.open("result/maskCaolv_transparent.png").convert('RGBA')
foreground7 = Image.open("result/maskLightFen_transparent.png").convert('RGBA')


background.paste(foreground1, (0, 0), foreground1)
background.paste(foreground2, (0, 0), foreground2)
background.paste(foreground3, (0, 0), foreground3)
background.paste(foreground4, (0, 0), foreground4)
background.paste(foreground5, (0, 0), foreground5)
background.paste(foreground6, (0, 0), foreground6)
background.paste(foreground7, (0, 0), foreground7)

# result = Image.fromarray(background, mode='RGBA')
background.save("result/kuang7.png")
background.show()
