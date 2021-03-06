# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np

from timeTest import time_test
from logistic_regression import logistic_regression
from linear_regression_sgd import LinearRegSGD

from functools import wraps
def time_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('--- {}ing starting...'.format(func.__name__))
        start = time.clock()    # use clock() instead of time() in windows
        result = func(*args, **kwargs)
        end = time.clock()
        print('--- {} costs {}'.format(func.__name__, end-start))
        return result
    return wrapper 

def shuffle_data(x, y):
    indexs = np.arange(y.shape[0])
    np.random.shuffle(indexs)
    return x[indexs], y[indexs]

def generate_data(n):
    x_0 = np.abs(np.random.randn(n//2, 2))
    x_1 = -1.0*np.abs(np.random.randn(n//2, 2))
    x = np.concatenate((x_0, x_1))
    y = np.concatenate((np.ones(n//2), np.zeros(n//2)))
    return x, y

def load_data(n_train, n_test):
    x_train, y_train = generate_data(n_train)
    x_train, y_train = shuffle_data(x_train, y_train)
    x_test, y_test = generate_data(n_test)
    x_test, y_test = shuffle_data(x_test, y_test)
    return x_train,y_train, x_test,y_test

def threshold(x, t):
    x[x>t] = 1
    x[x<=t] = 0
    return x.astype(np.int32)
    
def test_logistic(x_train,y_train, x_test,y_test, is_visual=True):
    logistic = logistic_regression()
    if is_visual:
        logistic.fit_visual(x_train, y_train)
    else:    
        wrap_fit = time_test(logistic.fit)
        wrap_fit(x_train, y_train)
    
    pred = logistic.predict(x_train)
    pred = threshold(pred, 0.5)
    print(np.sum(pred==y_train.astype(np.int32)))
    
    pred = logistic.predict(x_test)
    pred = threshold(pred, 0.5)
    print(np.sum(pred==y_test.astype(np.int32)))
    
if __name__ == '__main__':
    data = load_data(n_train=100, n_test=100)
    
    test_logistic(*data)