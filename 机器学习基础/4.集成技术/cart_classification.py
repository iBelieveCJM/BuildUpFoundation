
#j# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd
from collections import Counter
from pandas.api.types import is_integer, is_categorical_dtype, is_object_dtype, is_string_dtype

DEBUG = False
eps = 1e-8

class CART_weight_classifier():
    
    def __init__(self):
        self.tree = None
        self.continueFeatVals = None
        self.labelDtype = None
    
    def fit(self, data, labels, weights=None):
        if weights is None:
            weights = np.ones(labels.shape[0])/labels.shape[0]
        self.labelDtype = labels.dtype
        featName = self.makeFeatName(data)
        if DEBUG: print(featName)
        if DEBUG: print(self.continueFeatVals)
        self.tree = self.createTree(data, labels, weights, featName)
        
    def predict(self, data):
        #ret = pd.Series(-1, range(len(data)), dtype=self.labelDtype)
        ret = np.zeros(data.shape[0])
        for idx in range(len(data)):
            ret[idx] = self.classify(self.tree, data.iloc[idx])
        return ret
        
    def classify(self, tree, sample):
        if is_integer(tree):
            return tree
        else:
            feat = list(tree.keys())[0]
            if sample[feat] > tree[feat]['splitVal']:
                return self.classify(tree[feat]['>'], sample)
            else:
                return self.classify(tree[feat]['<='], sample)
        
    def calcGini(self, labels, weights):
        unique_labels = Counter(labels)
        datalen = labels.shape[0]
        gini_sum = 0.0
        for label, num in unique_labels.items():
            prob = num/datalen
            gini_sum += prob*prob
        return np.sum(weights)*(1-gini_sum)
    
    def calcContinueGiniIndex(self, featData, labels, weights):
        values = featData.unique()
        if values.shape[0] == 1:
            if DEBUG: print('--', values)
            return self.calcGini(labels, weights), values[0]
        midVals = (values[:-1]+values[1:])/2.0
        bestGiniIndex, bestVal = self.calcGini(labels, weights), midVals[0]
        for val in midVals:
            # greater than
            gini_greater = self.calcGini(labels[featData>val], weights[featData>val])
            gini_greater *= np.sum(featData>val)/featData.shape[0]
            # less and equal than
            gini_lessEqual = self.calcGini(labels[featData<=val], weights[featData<=val])
            gini_lessEqual *= np.sum(featData<=val)/featData.shape[0]
            # gini index
            gini_index = gini_greater + gini_lessEqual
            if gini_index < bestGiniIndex:
                bestGiniIndex = gini_index
                bestVal = val
        return bestGiniIndex, bestVal
    
    def bestFeat(self, data, labels, weights, featName):
        if DEBUG: print('-'*30, '\nall name: ', featName)
        bestFeatVal, bestGiniIndex = -1, self.calcGini(labels, weights)+eps
        bestFeatName = None
        for col in featName:
            giniIndex, val = self.calcContinueGiniIndex(data[col], labels, weights)
            if DEBUG: print(giniIndex, val, bestGiniIndex)
            if giniIndex < bestGiniIndex:
                bestGiniIndex = giniIndex
                bestFeatName, bestFeatVal = col, val
        return bestFeatName, bestFeatVal
    
    def createTree(self, data, labels, weights, featName):
        #End condition 1: only one class left.
        if len(set(labels))==1:
            return labels.iloc[0]
            #return labels[0]
        #End condition 2: not feature left to split.
        if len(featName)==0:
            return Counter(labels).most_common(1)[0][0] #majority voting
        # choose best feature
        bestFeatName, bestFeatVal = self.bestFeat(data, labels, weights, featName)
        if DEBUG: print('best feature: ', bestFeatName, ' val: ', bestFeatVal)
        #if the number of possible value of feature less than 3, then delete the feature.
        if data[bestFeatName].unique().shape[0] < 3:
            del featName[bestFeatName]
        #End condition 3: only one feature value left.
        if data[bestFeatName].unique().shape[0] == 1:
            return Counter(labels).most_common(1)[0][0]
        #Recursive create tree
        tree = {bestFeatName:{}}
        tree[bestFeatName]['splitVal'] = bestFeatVal
        lessEqIdx = data[bestFeatName]<=bestFeatVal
        tree[bestFeatName]['<='] = self.createTree(data[lessEqIdx], labels[lessEqIdx],
                                                   weights[lessEqIdx], featName.copy())
        greaterIdx = data[bestFeatName]>bestFeatVal
        tree[bestFeatName]['>'] = self.createTree(data[greaterIdx], labels[greaterIdx],
                                                  weights[greaterIdx], featName.copy())
        return tree
    
    def makeFeatName(self, data):
        featName = {}
        for col in data:
            if is_categorical_dtype(data[col]) or\
               is_object_dtype(data[col]) or\
               is_string_dtype(data[col]):
                featName[col] = 'discrete'
            else:
                featName[col] = 'continue'
        return featName