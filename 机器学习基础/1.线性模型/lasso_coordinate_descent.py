# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np

class LassoCorrdinateDescent():
    
    def __init__(self, alpha=1.0):
        self.coef_ = None
        self.intercept_ = 0
        self.alpha = alpha
        
    def fit(self, X, y, maxIter=1000):
        """ linear regression with OLS 
        """
        # data process: w*X+b ==> w_*X_temp, that is w_ = [w,b], X_temp=[X,1]
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        
        W_temp = np.random.randn(X_temp.shape[1]) # zero initialization?
        z = np.sum(X_temp*X_temp, axis=0)
        for _ in range(maxIter):
            for d in range(X_temp.shape[1]):
                W_temp[d] = 0
                p = X_temp[:,d].dot(y - X_temp.dot(W_temp))
                if p < -self.alpha/2:
                    w = (p + self.alpha/2) / z[d]
                elif p > self.alpha/2:
                    w = (p - self.alpha/2) / z[d]
                else:
                    w = 0
                W_temp[d] = w
        self.coef_ = W_temp[:-1]
        self.intercept_ = W_temp[-1]
        
    def predict(self, X):
        if self.coef_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return self.coef_.dot(X.T) + self.intercept_
                