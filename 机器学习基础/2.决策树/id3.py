# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
from collections import Counter

class ID3Tree():
    
    def __init__(self):
        self.tree = None
    
    def fit(self, data, labels):
        self.tree = self.createTree(data, labels, [])
        
    def predict(self, data):
        ret = np.zeros(data.shape[0])
        for idx, sample in enumerate(data):
            ret[idx] = self.classify(self.tree, sample)
        return ret
        
    def classify(self, tree, sample):
        if isinstance(tree, np.int32):
            return tree
        else:
            axis = list(tree.keys())[0]
            return self.classify(tree[axis][sample[axis]], sample)
        
    def calcEnt(self, data, labels):
        unique_labels = Counter(labels)
        datalen = labels.shape[0]
        ent = 0.0
        for label, num in unique_labels.items():
            prob = num/datalen
            ent -= prob*np.log(prob)
        return ent
    
    def bestFeat(self, data, labels, order):
        bestFeatAxis, bestEnt = -1, 0.0
        origin_ent = self.calcEnt(data, labels)
        num, axises = data.shape
        for axis in range(axises):
            if axis not in order:
                values = set(data[:,axis])
                ent_for_partition = 0.0
                for val in values:
                    ent_for_val = self.calcEnt(data[data[:,axis]==val],
                                               labels[data[:,axis]==val])
                    prob_for_val = np.sum(data[:,axis]==val)/num
                    ent_for_partition += (prob_for_val * ent_for_val)
                ent_inc = origin_ent - ent_for_partition
                if ent_inc > bestEnt:
                    bestEnt = ent_inc
                    bestFeatAxis = axis
        return bestFeatAxis
    
    def createTree(self, data, labels, order):
        #End condition 1: only one class left.
        if len(set(labels))==1:
            return labels[0]
        bestFeature = self.bestFeat(data, labels, order)
        order.append(bestFeature)
        values = set(data[:,bestFeature])
        #End condition 2: only one feature left.
        if len(values)==1:
            return Counter(data[:,bestFeature]).most_common(1)[1] #majority voting
        tree = {bestFeature:{}}
        for val in values:
            tree[bestFeature][val] = self.createTree(data[data[:,bestFeature]==val],
                                                     labels[data[:,bestFeature]==val],
                                                     [x for x in order])
        return tree