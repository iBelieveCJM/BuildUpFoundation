# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:26:20 2020

@author: CJM
"""

import numpy as np

def softmax(z):
    z_exp = np.exp(z)
    if len(z_exp.shape)==2:
        return z_exp / z_exp.sum(axis=1, keepdims=True)
    else:
        return z_exp / z_exp.sum()

class SoftmaxClassifierSGD:
    
    def __init__(self, class_num):
        self.coef_ = None
        self.intercept_ = None
        self.nClass_ = class_num
        
    def gradW(self, X, y, W):
        """softmax(W*X) ==> X.T * softmax_grad
        """
        num_x = X.shape[0]
        # if i==y, then softmax_grad = preds_i-1;
        # otherwise, softmax_grad = preds_i
        preds = softmax(np.matmul(X, W)) #preds.shape(N,C)
        preds[list(range(num_x)), y] -= 1
        # grad = X.T*softmax_grad
        return np.matmul(X.T, preds)/num_x
    
    def fit(self, X, y, lr=0.1, maxIter=100):
        """gradient descent"""
        # data process: w*X+b ==> w_*X_temp, that is w_=[w,b], X_temp=[X,1]
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        W_temp = np.random.randn(X_temp.shape[1], self.nClass_) # zero initialization?
        # gradient descent
        for _ in range(maxIter):
            W_temp -= lr*self.gradW(X_temp, y, W_temp)
        self.coef_ = W_temp[:-1]
        self.intercept_ = W_temp[-1]
    
    def predict(self, X):
        if self.coef_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return softmax(np.matmul(X, self.coef_) + self.intercept_)