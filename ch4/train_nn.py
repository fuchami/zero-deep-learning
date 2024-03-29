# coding:utf-8

import sys, os
sys.path.append(os.pardir)
import numpy as np
import matplotlib.pylab as plt
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# データの読み込み
(x_train , y_train), (x_test, y_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

iters_num = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_late = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

# 1エポックあたりn繰り返し数
iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = y_train[batch_mask]

    # 勾配の計算
    grad = network.gradient(x_batch, t_batch)

    # パラデータ更新
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_late * grad[key]
    
    # 学習経過の記録
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    # 1エポックごとに認識精度を計算
    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, y_train)
        test_acc = network.accuracy(x_test, y_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test_acc | " + str(train_acc) + ", " + str(test_acc))
        print("loss:" + str(loss))

markers = {'train': 'o', 'test' : 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()