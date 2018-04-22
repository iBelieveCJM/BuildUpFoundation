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
        print('--- {}ing starting...'.format(func.__name__))
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
        self.method = {
                'OLS':lambda X,_: X.T.dot(X),
                'ridge':lambda X,lambda_: X.T.dot(X) + lambda_*np.eye(np.shape(X)[1])
                }
        
    @time_test
    def fit(self, X, y, method_='OLS', lambda_=0.2):
        """fit the data
        method_:
            'OLS'  : ordinary least squares
            'ridge': ridge regressioin
        """
        # input check
        if method_ not in self.method:
            print('error: unknow method')
            return
        # data process: w*X+b ==> w_*X_temp, that is w_ = [w,b]
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        # XTX checks
        XTX = self.method[method_](X_temp, lambda_)
        if np.linalg.det(XTX) == 0:
            print('error: the X.T.dot(X) is singular')
            return
        # if XTX is not singular, it has the closed form solution.
        print('Call {} regression'.format(method_))
        self.__closed_form(XTX, X_temp, y)
        
    @time_test
    def predict(self, X):
        if self.w_ is None:
            print('error: the model had not been trainedd')
            return #should raise the expection
        return self.w_.dot(X.T) + self.b_
    
    def __closed_form(self, XTX, X, y):
        W_temp = np.linalg.inv(XTX).dot(X.T).dot(y)
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
    n_train = 10
    
    ## load data
    start = time.clock()
    iris = load_iris()   # the shape of iris.data is (150,4)
    print('--- loading data costs {}'.format(time.clock()-start))
    
    ## processing data
    start = time.clock()
    shuffle_data(iris)
    x_train, y_train, x_test, y_test = split_data(iris, n_train)
    print('--- processing data costs {}'.format(time.clock()-start))
    
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