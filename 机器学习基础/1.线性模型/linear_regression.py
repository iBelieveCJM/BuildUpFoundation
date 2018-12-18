# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import time

class LinearReg():
    
    def __init__(self):
        self.coef_ = None;
        self.intercept_ = 0;
        
    def fit(self, X, y):
        """ linear regression with OLS 
        """
        # data process: w*X+b ==> w_*X_temp, that is w_ = [w,b], X_temp=[X,1]
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        
        # XTX checks
        XTX = X_temp.T.dot(X_temp)
        if np.linalg.det(XTX) == 0:
            print('error: the X.T.dot(X) is singular')
            return #should raise the expection
            
        # if XTX is not singular, it has the closed form solution.
        # let XTX*W_temp - X_temp.T*y = 0 ==> inv(XTX)*(X_temp.T)*y
        W_temp = np.linalg.inv(XTX).dot(X_temp.T).dot(y)
        self.coef_ = W_temp[:-1]
        self.intercept_ = W_temp[-1]
        
    def predict(self, X):
        if self.coef_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return self.coef_.dot(X.T) + self.intercept_
        