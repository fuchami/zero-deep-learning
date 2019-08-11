#%% coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# -5から5までを0.1刻みの配列で表現
x = np.arange(-5.0, 5.0, 0.1) 
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y軸n範囲を指定
plt.show

#%%