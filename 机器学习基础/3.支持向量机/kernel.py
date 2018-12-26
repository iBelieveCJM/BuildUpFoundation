# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np

def rbf(data, sigma):
    """rbf"""
    dist = eucl_dist(data, data)
    return np.exp(-0.5* dist / sigma**2)

def linear(data):
    return data.dot(data.T)

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