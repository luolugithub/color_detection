# -*- coding: utf-8 -*-
# @Time : 2020/3/6 上午10:35
# @Author : LuoLu
# @FileName: color_img_transparent.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

from PIL import Image

img = Image.open('result/mask1Quartz.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0:
        newData.append((0, 0, 0, 0))
    else:
        if item[0] < 150:
            newData.append((0, 0, 0, 255))
        else:
            newData.append(item)
            print(item)


img.putdata(newData)
img.save("result/mask1Quartz_transparent.png", "PNG")