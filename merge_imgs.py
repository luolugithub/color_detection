# -*- coding: utf-8 -*-
# @Time : 2020/3/5 上午10:13
# @Author : LuoLu
# @FileName: merge_imgs.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com

from PIL import Image
# your loop here
img = Image.open('result/mask_w_blue.png')
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("mod_img1.png", "PNG")
# Then do your usual paste as you are doing in your code.

background = Image.open("mod_img1.png")
foreground = Image.open("result/mask_w_green.png")

background.paste(foreground, (0, 0), foreground)
background.show()


# convert mask_w_blue.png                                \
#    \( mask_w_green.png -transparent white \) -composite \
#    \( mask_w_red.png -transparent white \) -composite result.png
