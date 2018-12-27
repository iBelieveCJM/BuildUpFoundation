# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np

def eucl_dist(x, y):
    """ Compute Pairwise Squared Euclidean Distance
    Input:
        x.shape(M, D)
        y.shape(N, D)
    Output:
        dist.shape(M, N)
    """
    x2 = np.tile(np.sum(x**2, axis=1, keepdims=True), (1,y.shape[0]))
    y2 = np.tile(np.sum(y**2, axis=1, keepdims=True), (1,x.shape[0])).T
    xy = x.dot(y.T)
    return x2 - 2*xy + y2

def rbf(sigma):
    """rbf"""
    def warpper(data1, data2):
        dist = eucl_dist(data1, data2)
        return np.exp(-0.5* dist / sigma**2)
    return warpper

def linear():
    def warpper(data1, data2):
        return data1.dot(data2.T)
    return warpper