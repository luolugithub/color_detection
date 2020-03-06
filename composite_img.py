# -*- coding: utf-8 -*-
# @Time : 2020/3/6 上午11:22
# @Author : LuoLu
# @FileName: composite_img.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

from PIL import Image

background = Image.new('RGB', (1001, 1001), color='black').convert('RGBA')

foreground1 = Image.open("result/red_mask_transparent.png").convert('RGBA')
foreground2 = Image.open("result/green_mask_transparent.png").convert('RGBA')
foreground3 = Image.open("result/blue_mask_transparent.png").convert('RGBA')


background.paste(foreground3, (0, 0), foreground3)
background.paste(foreground2, (0, 0), foreground2)
background.paste(foreground1, (0, 0), foreground1)
background.show()
