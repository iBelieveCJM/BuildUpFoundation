# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd
from collections import Counter
from pandas.api.types import is_integer, is_categorical_dtype, is_object_dtype, is_string_dtype

DEBUG = True
eps = 1e-8

class C45Tree():
    
    def __init__(self):
        self.tree = None
        self.continueFeatVals = None
        self.labelDtype = None
    
    def fit(self, data, labels):
        self.labelDtype = labels.dtype
        featName = self.makeFeatName(data)
        self.continueFeatVals = {feat:0 for feat, dtype in featName.items()
                                  if dtype=='continue'}
        print(featName)
        print(self.continueFeatVals)
        self.tree = self.createTree(data, labels, featName)
        
    def predict(self, data):
        ret = pd.Series(-1, range(len(data)), dtype=self.labelDtype)
        for idx in range(len(data)):
            ret[idx] = self.classify(self.tree, data.iloc[idx])
        return ret
        
    def classify(self, tree, sample):
        if is_integer(tree):
            return tree
        else:
            feat = list(tree.keys())[0]
            if feat in self.continueFeatVals:
                if sample[feat] > self.continueFeatVals[feat]:
                    return self.classify(tree[feat]['>'], sample)
                else:
                    return self.classify(tree[feat]['<='], sample)
            else:
                ret = None
                try:
                    ret = self.classify(tree[feat][sample[feat]], sample)
                except KeyError:
                    print('feat: ', feat, ' feat value: ', sample[feat])
                    print('tree: ', tree[feat])
                    ret = 0
                return ret
        
    def calcEnt(self, labels):
        unique_labels = Counter(labels)
        datalen = labels.shape[0]
        ent = 0.0
        for label, num in unique_labels.items():
            prob = num/datalen
            ent -= prob*np.log(prob)
        return ent
    
    def calcDiscreteEntIncRate(self, featData, labels, origin_ent):
        values = set(featData)
        ent_for_partition, ent_split = 0.0, 0.0
        for val in values:
            ent_for_val = self.calcEnt(labels[featData==val])
            prob_for_val = np.sum(featData==val)/featData.shape[0]
            ent_for_partition += (prob_for_val * ent_for_val)
            ent_split -= prob_for_val*np.log(prob_for_val)
        ent_inc_rate = (origin_ent - ent_for_partition) / (ent_split+eps)
        return ent_inc_rate, None
    
    def calcContinueEntIncRate(self, featData, labels, origin_ent):
        values = featData.unique()
        if values.shape[0] == 1:
            return 0.0, values[0]
        midVals = (values[:-1]+values[1:])/2.0
        bestEntIncRate, bestVal = 0.0, midVals[0]
        for val in midVals:
            ent_for_partition, ent_split = 0.0, 0.0
            # greater than
            ent_greater = self.calcEnt(labels[featData>val])
            prob_greater = np.sum(featData>val)/featData.shape[0]
            ent_for_partition += prob_greater*ent_greater
            ent_split -= prob_greater*np.log(prob_greater+eps)
            # less and equal than
            ent_lessEqual = self.calcEnt(labels[featData<=val])
            prob_lessEqual = np.sum(featData<=val)/featData.shape[0]
            ent_for_partition += prob_lessEqual*ent_lessEqual
            ent_split -=  prob_lessEqual*np.log(ent_lessEqual+eps)
            # entropy increase rate
            ent_inc_rate = (origin_ent - ent_for_partition) / (ent_split+eps)
            if ent_inc_rate > bestEntIncRate:
                bestEntIncRate = ent_inc_rate
                bestVal = val
        return bestEntIncRate, bestVal
    
    def bestFeat(self, data, labels, featName):
        if DEBUG: print('-'*30, '\nall name: ', featName)
#        if len(featName)==1:
#            return featName[0], 0
        bestFeatVal, bestEntIncRate = -1, -0.1
        origin_ent = self.calcEnt(labels)
        bestFeatName = None
        for col, dtype in featName.items():
            if dtype == 'discrete':
                ent_inc_rate, val = self.calcDiscreteEntIncRate(data[col], labels, origin_ent)
                if DEBUG: print('discrete feat: ', col, ' rate: ', ent_inc_rate)
            else:                
                ent_inc_rate, val = self.calcContinueEntIncRate(data[col], labels, origin_ent)
                if DEBUG: print('continue feat: ', col, ' rate: ', ent_inc_rate, ' val: ', val)
            if ent_inc_rate > bestEntIncRate:
                bestEntIncRate = ent_inc_rate
                bestFeatName, bestFeatVal = col, val
        return bestFeatName, bestFeatVal
    
    def createTree(self, data, labels, featName):
        #End condition 1: only one class left.
        if len(set(labels))==1:
            return labels.iloc[0]
        #End condition 2: not feature left to split.
        if len(featName)==0:
            return Counter(labels).most_common(1)[0][0] #majority voting
        #Recursive create tree
        bestFeatName, bestFeatVal = self.bestFeat(data, labels, featName)
        if bestFeatName in self.continueFeatVals: 
            self.continueFeatVals[bestFeatName]=bestFeatVal
        if DEBUG: print('best feature: ', bestFeatName, ' val: ', bestFeatVal)
        del featName[bestFeatName]
#        #End condition 3: only one feature value left.
#        if len(values)==1:
#            return Counter(labels).most_common(1)[0][0]
        tree = {bestFeatName:{}}
        if bestFeatVal is None:
            values = set(data[bestFeatName])
            if DEBUG: print('best feature valuse: ', values)
            for val in values:
                tree[bestFeatName][val] = self.createTree(data[data[bestFeatName]==val],
                                                          labels[data[bestFeatName]==val],
                                                          featName.copy())
        else:
            tree[bestFeatName]['<='] = self.createTree(data[data[bestFeatName]<=bestFeatVal],
                                                       labels[data[bestFeatName]<=bestFeatVal],
                                                       featName.copy())
            if not data[bestFeatName].unique().shape[0]==1:
                tree[bestFeatName]['>'] = self.createTree(data[data[bestFeatName]>bestFeatVal],
                                                          labels[data[bestFeatName]>bestFeatVal],
                                                          featName.copy())
            else:
                tree[bestFeatName]['>'] = Counter(labels).most_common(1)[0][0] #majority voting
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