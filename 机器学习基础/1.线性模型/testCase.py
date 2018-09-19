# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

from timeTest import time_test
from linear_regression import LinearReg
from linear_regression_l2 import LinearRegL2

def shuffle_data(data):
    indexs = np.arange(len(data.target))
    np.random.shuffle(indexs)
    data.data = data.data[indexs]
    data.target = data.target[indexs]

def split_data(data, n_train):
    x_train = data.data[:n_train]
    y_train = data.target[:n_train]
    x_test = data.data[n_train:]
    y_test = data.target[n_train:]
    return x_train, y_train, x_test, y_test
    
@time_test
def load_data(load_data_func, n_train, is_shuffle=True):
    iris = load_data_func()   # the shape of iris.data is (150,4)
    if is_shuffle:
        shuffle_data(iris)
    return split_data(iris, n_train)


def testModel(model, x_train, y_train, x_test, y_test):
    ## training model
    wrap_fit = time_test(model.fit)
    wrap_fit(x_train, y_train)
    print('w:',model.coef_)
    print('b:',model.intercept_)
    
    ## testing model
    wrap_predict = time_test(model.predict)
    y_pred = wrap_predict(x_test)
    print( 'mean squared error: {}'.format(mean_squared_error(y_test, y_pred)) )
    print( 'Variance score: {}'.format(r2_score(y_test, y_pred)) )
    
if __name__ == '__main__':
    ## load data
    n_train = 10
    print('the number of train data is {}'.format(n_train))
    data = load_data(load_iris, n_train)
    
    ## sklearn linear regression
    print('\nsklearn linear regression')
    reg = linear_model.LinearRegression()
    testModel(reg, *data)
    
    ## my linear regression
    print('\nmy linear regresssion')
    #myReg = LinearReg()
    myReg = LinearRegL2()
    testModel(myReg, *data)