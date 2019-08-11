# coding:utf-8

"""
XORの実装
"""

import numpy as np
from perceptron import AND, NAND, OR

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y =  AND(s1, s2)
    return y

if __name__ == "__main__":
    inputs = [(0,0), (1,0), (0,1), (1,1)]

    print("--- XOR GATE ---")
    for i in inputs:
        y = XOR(i[0], i[1])
        print (str(i) + " => " + str(y))
