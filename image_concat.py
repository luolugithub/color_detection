# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 下午4:23
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : image_concat.py
# @Software: PyCharm\

import numpy as np
import PIL
from PIL import Image
from PIL.ImageFile import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

list_im = ['image/yashi.png',
           'result/kuang7.png']
imgs = [PIL.Image.open(i) for i in list_im]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))

# save that beautiful picture horizon
imgs_comb = PIL.Image.fromarray(imgs_comb)
imgs_comb.save('result/kuang7_extract.png')

# for a vertical stacking it is simple: use vstack
imgs_comb = np.vstack((np.asarray(i.resize(min_shape)) for i in imgs))
imgs_comb = PIL.Image.fromarray(imgs_comb)
# imgs_comb.save('ys_index.png')
