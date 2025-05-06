#!/user/bin/env python3
# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.path.pardir)
import pickle
from PIL import Image
import numpy as np
from dataset.mnist import load_mnist

def img_save(img,path='mnist0.png'):
    img = Image.fromarray(np.uint8(img))
    img.save(path)
    print(f"Save to {path}")

(x_train,t_train),(x_test,t_test) = load_mnist(normalize=False,flatten=True)
img = x_train[0]
label = t_train[0]
print(label)
print(img.shape)
img=img.reshape(28,28)
print(img.shape)

img_save(img)