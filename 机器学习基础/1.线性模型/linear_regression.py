# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:45:04 2018

@author: CJM
"""

import numpy as np

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
# my linear regression model
####################################################################

class myLinearReg():
    
    def __init__(self):
        self.w_ = None;
        self.b_ = 0;
        
    def fit(self, X, y):
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        self.__closed_form(X_temp, y)
        
    def predict(self, X):
        return self.w_.dot(X.T) + self.b_
    
    def __closed_form(self, X, y):
        temp = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        self.w_ = temp[:-1]
        self.b_ = temp[-1]

####################################################################
# main
####################################################################

from sklearn.datasets import load_iris
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == '__main__':
    ## load data
    n_train = 100
    iris = load_iris()
    shuffle_data(iris)
    x_train,y_train, x_test,y_test = split_data(iris, n_train)
    print('loaded data.\nthe number of train data is {}'.format(n_train))
    
    ########## sklearn linear regression ##########
    print('\nsklearn linear regression')
    
    ## training model
    reg = linear_model.LinearRegression()
    reg.fit(x_train, y_train)
    print('w:',reg.coef_)
    print('b:',reg.intercept_)
    
    ## testing model
    y_pred = reg.predict(x_test)
    print( 'mean squared error: {}'.format(mean_squared_error(y_test, y_pred)) )
    print( 'Variance score: {}'.format(r2_score(y_test, y_pred)) )
    
    ########## my linear regression ##########
    print('\nmy linear regresssion')
    
    ## training model
    myReg = myLinearReg()
    myReg.fit(x_train, y_train)
    print('w:',myReg.w_)
    print('b:',myReg.b_)
    
    ## testing model
    y_pred = myReg.predict(x_test)
    print( 'mean squared error: {}'.format(mean_squared_error(y_test, y_pred)) )
    print( 'Variance score: {}'.format(r2_score(y_test, y_pred)) )