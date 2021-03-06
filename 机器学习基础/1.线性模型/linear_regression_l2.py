# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np

class LinearRegL2():
    
    def __init__(self, lambda_=0.2):
        self.coef_ = None;
        self.intercept_ = 0;
        self.lambda_ = lambda_;
        
    def fit(self, X, y):
        # data process
        #   w*X+b ==> w_*X_temp, that is w_=[b,w], X_temp=[1,X]
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((np.ones((num_x, 1)), X), axis=1)
        
        # singular checks
        identity = np.eye(np.shape(X_temp)[1])
        identity[0,0] = 0
        XTX = X_temp.T.dot(X_temp) + self.lambda_*identity
        if np.linalg.det(XTX) == 0:
            print('error: the X.T.dot(X) is singular')
            return #should raise the expection
            
        # if XTX is not singular, it has the closed form solution.
        W_temp = np.linalg.inv(XTX).dot(X_temp.T).dot(y)
        self.coef_ = W_temp[1:]
        self.intercept_ = W_temp[0]
        
    def predict(self, X):
        if self.coef_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return self.coef_.dot(X.T) + self.intercept_
        