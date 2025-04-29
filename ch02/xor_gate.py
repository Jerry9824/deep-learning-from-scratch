#!/user/bin/env python3
# -*- coding: utf-8 -*-

from or_gate import OR  #会执行整个模块，不仅仅是把函数“拿进来”
from nand_gate import NAND
from and_gate import AND

def XOR(x1,x2):
    s1 = OR(x1,x2)
    s2 = NAND(x1,x2)
    y = AND(s1,s2)
    return y
if __name__=='__main__':
    for xr in [[0,0],[0,1],[1,0],[1,1]]:
        print(str(xr)+'-->'+str(XOR(xr[0],xr[1])))