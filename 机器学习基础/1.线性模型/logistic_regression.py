# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def sigmod(z):
    return 1.0/(1+np.exp(-z))

class logistic_regression():
    
    def __init__(self):
        self.coef_ = None
        self.intercept_ = 0
        
    def gradW(self, X, y, W):
        """grad = (1/n) * X.T * (sigmod(WX+b) - y)
        X.shape(n, d)
        y.shape(n,)
        """
        z = W.dot(X.T)
        return X.T.dot(sigmod(z)-y)/X.shape[0]
    
    def fit(self, X, y, lr=0.1, maxIter=100):
        """gradient descent"""
        # data process: w*X+b ==> w_*X_temp, that is w_=[w,b], X_temp=[X,1]
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        W_temp = np.random.randn(X_temp.shape[1]) # zero initialization?
        ## XTX checks is necessary ?
        # gradient descent
        for _ in range(maxIter):
            W_temp -= lr*self.gradW(X_temp, y, W_temp)
        self.coef_ = W_temp[:-1]
        self.intercept_ = W_temp[-1]
        
    def fit_visual(self, X, y, lr=0.1, maxIter=100):
        assert np.shape(X)[1]==2
        num_x = np.shape(X)[0]
        X_temp = np.concatenate((X, np.ones((num_x, 1))), axis=1)
        W_temp = np.random.randn(X_temp.shape[1])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim([-3,3]); ax.set_ylim([-3, 3])
        ax.scatter(X[y==1][:,0], X[y==1][:,1], c='red')
        ax.scatter(X[y==0][:,0], X[y==0][:,1], c='green')
        line, = ax.plot([], [])
        def init():
            line.set_data([], [])
            return line,
        def animate(i):
            nonlocal W_temp
            W_temp -= lr*self.gradW(X_temp, y, W_temp)
            xx = np.linspace(-3.0, 3.0, num=100)
            yy = (-W_temp[2]-W_temp[0]*xx)/W_temp[1]  # w0*x+w1*y+b=0 ==> y=(-b-w0*x)/w1
            line.set_data(xx, yy)
            return line,
        #important! the function must return, otherwise there no line to be show
        _ = animation.FuncAnimation(fig, animate, init_func=init,
                                    frames=maxIter, interval=2, blit=True)
        self.coef_ = W_temp[:-1]
        self.intercept_ = W_temp[-1]
        plt.show()
        
    def predict(self, X):
        if self.coef_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return sigmod(self.coef_.dot(X.T) + self.intercept_)
            