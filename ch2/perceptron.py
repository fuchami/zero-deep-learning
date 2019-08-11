# coding: utf-8
"""
パーセプトロンの実装
"""

import numpy as np

# ANDゲートの実装
def AND(x1, x2): 
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# NANDゲートの実装
def NAND(x1, x2): 
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# NANDゲートの実装
def OR(x1, x2): 
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    inputs = [(0,0), (1,0), (0,1), (1,1)]

    print("--- AND GATE ---")
    for i in inputs:
        y = AND(i[0], i[1])
        print (str(i) + " => " + str(y))

    print("--- NAND GATE ---")
    for i in inputs:
        y = NAND(i[0], i[1])
        print (str(i) + " => " + str(y))

    print("--- OR GATE ---")
    for i in inputs:
        y = OR(i[0], i[1])
        print (str(i) + " => " + str(y))
