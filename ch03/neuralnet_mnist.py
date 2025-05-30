#!/user/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import sys,os

sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from sigmoid import sigmoid
from softmax import softmax

def get_data():
    (x_train, y_train), (x_test, y_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, y_test

def init_network():
    with open('sample_weight.pkl','rb')as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1,W2,W3 = network['W1'],network['W2'],network['W3']
    b1,b2,b3 = network['b1'],network['b2'],network['b3']

    a1 = np.dot(x,W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1,W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2,W3) + b3
    y = softmax(a3)
    return y

x,t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y_pred = predict(network,x[i])
    y = np.argmax(y_pred)  #获取概率最高的元素索引
    if y == t[i]:
        accuracy_cnt += 1
accuracy = accuracy_cnt / len(x)
print("Accuracy:",accuracy)