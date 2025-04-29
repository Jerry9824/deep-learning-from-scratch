#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label='sin(x)')
plt.plot(x,y2,label='cos(x)',linestyle='--')
plt.legend()   #将标签画在图上
plt.show()

