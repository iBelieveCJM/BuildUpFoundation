# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:45:04 2018

@author: CJM
"""

import numpy as np
import time
from functools import wraps

####################################################################
# shuffle data
####################################################################

def shuffle_data(data):
    indexs = np.arange(len(data.target))
    np.random.shuffle(indexs)
    data.data = data.data[indexs]
    data.target = data.target[indexs]

####################################################################
# split data
####################################################################

def split_data(data, n_train):
    x_train = data.data[:n_train]
    y_train = data.target[:n_train]
    x_test = data.data[n_train:]
    y_test = data.target[n_train:]
    return x_train, y_train, x_test, y_test

####################################################################
# decorater to test the execution time
####################################################################

def time_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('{}ing starting...'.format(func.__name__))
        start = time.clock()    # use clock() instead of time() in windows
        result = func(*args, **kwargs)
        end = time.clock()
        print('--- {} costs {}'.format(func.__name__, end-start))
        return result
    return wrapper

####################################################################
# my linear regression model
####################################################################

class myLinearReg():
    
    def __init__(self):
        self.w_ = None;
        self.b_ = 0;
        
    @time_test
    def fit(self, X, y):
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        self.__closed_form(X_temp, y)
        
    @time_test
    def predict(self, X):
        return self.w_.dot(X.T) + self.b_
    
    def __closed_form(self, X, y):
        W_temp = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        self.w_ = W_temp[:-1]
        self.b_ = W_temp[-1]

####################################################################
# main
####################################################################

from sklearn.datasets import load_iris
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == '__main__':
    ########## load data ##########
    n_train = 100
    
    ## load data
    start = time.clock()
    iris = load_iris()
    end = time.clock()
    print('--- loading data costs {}'.format(end-start))
    
    ## processing data
    start = time.clock()
    shuffle_data(iris)
    x_train, y_train, x_test, y_test = split_data(iris, n_train)
    end = time.clock()
    print('--- processing data costs {}'.format(end-start))
    
    ## data info
    print('the number of train data is {}'.format(n_train))
    
    ########## sklearn linear regression ##########
    print('\nsklearn linear regression')
    reg = linear_model.LinearRegression()
    
    ## training model
    wrap_fit = time_test(reg.fit)
    wrap_fit(x_train, y_train)
    print('w:',reg.coef_)
    print('b:',reg.intercept_)
    
    ## testing model
    wrap_predict = time_test(reg.predict)
    y_pred = wrap_predict(x_test)
    print( 'mean squared error: {}'.format(mean_squared_error(y_test, y_pred)) )
    print( 'Variance score: {}'.format(r2_score(y_test, y_pred)) )
    
    ########## my linear regression ##########
    print('\nmy linear regresssion')
    myReg = myLinearReg()
    
    ## training model
    myReg.fit(x_train, y_train)
    print('w:',myReg.w_)
    print('b:',myReg.b_)
    
    ## testing model
    y_pred = myReg.predict(x_test)
    print( 'mean squared error: {}'.format(mean_squared_error(y_test, y_pred)) )
    print( 'Variance score: {}'.format(r2_score(y_test, y_pred)) )