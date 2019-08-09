# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:02:17 2019

@author: CJM
"""

import numpy as np

class KMeans:
    
    def __init__(self, k, dist='eucl', eps=1e-5, nIter=50):
        self.eps = eps
        self.nIter = nIter
        self._k = k
        self._centroids = None
        self._labels = None
        
    def _init_centroids(self, data):
        ridx = np.random.randint(data.shape[0], size=self._k,)
        self._centroids = data[ridx].copy()
        
    def fit_once(self, data):
        diff = data[np.newaxis,...] - self._centroids[:,np.newaxis,:]
        norm_diff = np.linalg.norm(diff, 2, axis=2)
        self._labels = np.argmin(norm_diff, axis=1)
        for i in self.labels.unique():
            self._centroids[i] = np.sum(data[self.labels==i], axis=0)
            
    def fit(self, data):
        self._init_centroids(self, data)
        old_cents = self._centroids.copy()
        
        it, err = 0, self.eps+1
        while err > self.eps or it < self.nIter:
            self.fit_once(data)
            it +=1
            err = np.linalg.norm(self._centroids-old_cents, 2)