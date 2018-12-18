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
from linear_regression_sgd import LinearRegSGD
from linear_regression_l2 import LinearRegL2
from lasso_coordinate_descent import LassoCorrdinateDescent

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
    iris = load_data_func()
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
    
def test_sklearn_linear_regression(*data):
    """sklearn linear regression (OLS)"""
    print('\nsklearn linear regression (OLS)')
    reg = linear_model.LinearRegression()
    testModel(reg, *data)
    
def test_my_linear_regression(*data):
    """my linear ridge regression (OLS)"""
    print('\nmy linear regresssion (OLS)')
    myReg = LinearReg()
    testModel(myReg, *data)
    
def test_my_linear_regression_sgd(*data):
    """my linear ridge regression (SGD)"""
    print('\nmy linear regresssion (SGD)')
    myReg = LinearRegSGD()
    testModel(myReg, *data)
    
def test_sklearn_ridge_regression(alpha, *data):
    """sklearn linear ridge regression"""
    print('\nsklearn linear ridge regression')
    reg = linear_model.Ridge(alpha=alpha)
    testModel(reg, *data)
    
def test_my_ridge_regression(alpha, *data):
    """my linear ridge regression"""
    print('\nmy linear ridge regresssion')
    myReg = LinearRegL2(lambda_=alpha)
    testModel(myReg, *data)
    
def test_sklearn_lasso_regression(alpha, *data):
    """sklearn lasso regression"""
    print('\nsklearn lasso regression')
    reg = linear_model.Lasso(max_iter=100, alpha=alpha)
    testModel(reg, *data)
    
def test_my_lasso_cd(alpha, *data):
    """my linear ridge regression"""
    print('\nmy lasso regresssion with coordinate descent')
    myReg = LassoCorrdinateDescent(alpha=alpha)
    testModel(myReg, *data)
    
if __name__ == '__main__':
    ## load data
    n_train = 10
    print('the number of train data is {}'.format(n_train))
    data = load_data(load_iris, n_train)    # the shape of iris.data is (150,4)
    
    test_sklearn_linear_regression(*data)
    test_my_linear_regression(*data)
    test_my_linear_regression_sgd(*data)
    
    lam = 0.2
    test_sklearn_ridge_regression(lam, *data)
    test_my_ridge_regression(lam, *data)
    
    alpha = 1.0
    test_sklearn_lasso_regression(alpha, *data)
    test_my_lasso_cd(alpha, *data)