# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd

DEBUG = False
eps = 1e-8

class AdaBoost:
    
    def __init__(self, baseModel, model_n):
        self._buildModel = baseModel
        self.model_n = model_n
        self.model = {}
        
    def predict(self, data):
        prob = np.zeros(data.shape[0])
        for coef, base in self.model.items():
            prob += coef* base.predict(data)
        return np.sign(prob)
    
    def fit(self, data, labels):
        weights = np.ones(labels.shape[0])/labels.shape[0]
        for i in range(self.model_n):
            print('{}-th model training...'.format(i))
            base = self._buildModel()
            base.fit(data, labels, pd.Series(weights,index=labels.index))
            # classification error
            acc = np.dot(weights, base.predict(data)==labels)
            err = 1.0 - acc
            # coef
            coef = 0.5*np.log(acc/(1.0-acc) +eps)
            print('acc:', acc, ' err: ', err, ' coef: ', coef)
            # update whole model
            self.model[coef] = base
            # update weights
            EXP = np.exp(-coef* labels* base.predict(data))
            Z = weights.dot(EXP)
            weights = weights*EXP / Z
            if DEBUG: print('weight sum: ', weights.sum())
            if DEBUG: print('weight num: ', (weights>eps).sum())
        