#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def softmax(a):
    c = np.max(a,axis=-1,keepdims=True) #axis=-1表示只对最后一维操作，keepdims=True表示不压扁操作的那一维
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a,axis=-1,keepdims=True)
    y = exp_a / sum_exp_a
    return y