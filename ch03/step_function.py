#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x>0,dtype=int)

x = np.arange(-6.0,6.0,0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)  #限制y轴的范围
plt.show()