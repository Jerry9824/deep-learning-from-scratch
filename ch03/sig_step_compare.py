#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def step_function(x):
    #return int(x>0)  python本身不具有广播功能
    return np.array(x>0,dtype=int)

x = np.arange(-6.0,6.0,0.1)
y1 = sigmoid(x)
y2 = step_function(x)
plt.plot(x,y1,label="sigmoid")
plt.plot(x,y2,label="step_function",linestyle="--")
plt.legend()
plt.show()
