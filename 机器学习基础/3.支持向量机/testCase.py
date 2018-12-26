# -*- coding: utf-8 -*-
"""
@author: CJM
"""
import time
import numpy as np
from simple_smo import simpleSMO
from platt_smo import plattSMO
from platt_kernel_smo import plattKernelSMO
from sklearn.svm import SVC

from functools import wraps
def time_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('--- {}ing starting...'.format(func.__name__))
        start = time.clock()    # use clock() instead of time() in windows
        result = func(*args, **kwargs)
        end = time.clock()
        print('--- {} costs {}s'.format(func.__name__, end-start))
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
    y = np.concatenate((np.ones(n//2), -1.0*np.ones(n//2)))
    return x, y

def load_data(n_train, n_test):
    x_train, y_train = generate_data(n_train)
    x_train, y_train = shuffle_data(x_train, y_train)
    x_test, y_test = generate_data(n_test)
    x_test, y_test = shuffle_data(x_test, y_test)
    return x_train,y_train, x_test,y_test

def test_svm(x_train,y_train, x_test,y_test, is_visual=False):
    #svm = simpleSMO(C=1.0, eps=1e-3)
    svm = plattSMO(C=0.9, eps=1e-3)
    #svm = plattKernelSMO(C=1.0, eps=1e-3, kernelArgs='linear')
    #svm = SVC(gamma='auto')
    wrap_fit = time_test(svm.fit)
    wrap_fit(x_train, y_train)
    
    pred = svm.predict(x_train)
    print(np.sum(pred==y_train.astype(np.int32)))
    
    pred = svm.predict(x_test)
    print(np.sum(pred==y_test.astype(np.int32)))
    
    print(svm.suportVecIdx())
    print(svm.w_)
    print(svm.b_)
    
if __name__ == "__main__":
    data = load_data(n_train=10000, n_test=100)
    test_svm(*data)