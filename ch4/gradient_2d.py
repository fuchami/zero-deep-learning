# coding:utf-8

import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

""" 勾配の計算 """
def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # xと同じ形状の配列を生成

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) の計算
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)

        # f(x-h) の計算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 値を元に戻す
    
    return grad

def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        
        return grad


def function_2(x):
    return np.sum(x**2)
    # return x[0]**2 + x[1]**2 でも可


res = numerical_gradient(function_2, np.array([3.0, 4.0]))
print(res)
res = numerical_gradient(function_2, np.array([0.0, 2.0]))
print(res)
res = numerical_gradient(function_2, np.array([3.0, 0.0]))
print(res)


if __name__ == "__main__":
    x0 = np.arange(-2, 2.5, 0.25)
    x1 = np.arange(-2, 2.5, 0.25)
    X,Y = np.meshgrid(x0, x1)

    X = X.flatten()
    Y = Y.flatten()

    grad = numerical_gradient(function_2, np.array([X, Y]).T).T

    plt.figure()
    plt.quiver(X, Y, -grad[0], -grad[1], angles="xy", color="#666666")
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.xlabel('x1')
    plt.grid()
    plt.draw()
    plt.show()
