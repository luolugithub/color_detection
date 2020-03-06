# -*- coding: utf-8 -*-
# @Time : 2020/3/5 上午9:46
# @Author : LuoLu
# @FileName: single_color_replace.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

from PIL import Image
import numpy as np

im = Image.open('result/mask_light_fen.png')
im = im.convert('RGBA')

data = np.array(im)  # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability

# Replace white with red... (leaves alpha values alone...)
white_areas = (red == 255) & (blue == 255) & (green == 255)
data[..., :-1][white_areas.T] = (192, 192, 255)  # Transpose back needed

im2 = Image.fromarray(data)
im2.save("result/maskLightFen.png")
im2.show()
