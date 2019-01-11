# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd
from collections import Counter
from pandas.api.types import is_integer

DEBUG = False

class ID3Tree():
    
    def __init__(self):
        self.tree = None
        self.labelDtype = None
    
    def fit(self, data, labels):
        self.labelDtype = labels.dtype
        self.tree = self.createTree(data, labels, list(data.columns))
        
    def predict(self, data):
        n_sample = len(data)
        ret = pd.Series(-1, range(n_sample), dtype=self.labelDtype)
        for idx in range(n_sample):
            ret[idx] = self.classify(self.tree, data.iloc[idx])
        return ret
        
    def classify(self, tree, sample):
        if is_integer(tree):
            return tree
        else:
            axis = list(tree.keys())[0]
            ret = None
            try:
                ret = self.classify(tree[axis][sample[axis]], sample)
            except KeyError:
                print('feat: ', axis, ' feat value: ', sample[axis])
                if DEBUG: print('tree: ', tree[axis])
                ret = -1
            return ret
        
    def calcEnt(self, labels):
        unique_labels = Counter(labels)
        datalen = len(labels)
        ent = 0.0
        for label, num in unique_labels.items():
            prob = num/datalen
            ent -= prob*np.log(prob)
        return ent
    
    def bestFeat(self, data, labels, featName):
        if len(featName)==1:
            return featName[0], 0
        bestFeatAxis, bestEnt = -1, 0.0
        origin_ent = self.calcEnt(labels)
        for axis in range(len(featName)):
            values = set(data[featName[axis]])
            ent_for_partition = 0.0
            for val in values:
                ent_for_val = self.calcEnt(labels[data[featName[axis]]==val])
                prob_for_val = np.sum(data[featName[axis]]==val)/len(data)
                ent_for_partition += (prob_for_val * ent_for_val)
            ent_inc = origin_ent - ent_for_partition
            if ent_inc > bestEnt:
                bestEnt = ent_inc
                bestFeatAxis = axis
        return featName[bestFeatAxis], bestFeatAxis
    
    def createTree(self, data, labels, featName):
        if DEBUG: print('-'*30, '\nall name: ', featName)
        #End condition 1: only one class left.
        if len(set(labels))==1:
            return labels.iloc[0]
        #End condition 2: not feature left ot split.
        if len(featName)==0:
            return Counter(labels).most_common(1)[0][0] #majority voting
        #Recursive create tree
        bestFeatName, featAxis = self.bestFeat(data, labels, featName)
        if DEBUG: print('best name: ', bestFeatName, ' axis: ', featAxis)
        del featName[featAxis]
        values = set(data[bestFeatName])
        if DEBUG: print(values)
#        #End condition 3: only one feature value left.
#        if len(values)==1:
#            return Counter(labels).most_common(1)[0][0]
        tree = {bestFeatName:{}}
        for val in values:
            tree[bestFeatName][val] = self.createTree(data[data[bestFeatName]==val],
                                                     labels[data[bestFeatName]==val],
                                                     featName[:])
        return tree