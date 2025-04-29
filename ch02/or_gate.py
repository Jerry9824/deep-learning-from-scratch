#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def OR(x1,x2):
    x = np.array([x1,x2])
    w = [1,1]
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp > 0.0:
        return 1
    else:
        return 0
if __name__=='__main__':
    print(OR(0,0))
    print(OR(0,1))
    print(OR(1,0))
    print(OR(1,1))