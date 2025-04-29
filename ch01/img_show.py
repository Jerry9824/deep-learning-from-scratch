#!/user/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('../dataset/lena.png')
plt.imshow(img)  #准备好图像
plt.show()   #真正把图像窗口打开/刷新