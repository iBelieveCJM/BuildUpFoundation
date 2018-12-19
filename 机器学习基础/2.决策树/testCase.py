# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
from id3 import ID3Tree
from C4_5 import C45Tree

def testID31():
    data = np.array(
            [[1,1,1],
             [1,1,1],
             [1,2,2],
             [2,1,2],
             [2,1,2]])
    labels = np.array([1,1,2,0,0])
    
    #id3Tree = ID3Tree()
    id3Tree = C45Tree()
    id3Tree.fit(data, labels)
    print(id3Tree.tree)
    pred = id3Tree.predict(data)
    print(np.sum(pred.astype(np.int32)==labels)/labels.shape[0])
    
def testID32():
    data = np.array(
            [[1,1],
             [1,1],
             [1,2],
             [2,1],
             [2,1]])
    labels = np.array([1,1,0,0,0])
    
    #id3Tree = ID3Tree()
    id3Tree = C45Tree()
    id3Tree.fit(data, labels)
    print(id3Tree.tree)
    pred = id3Tree.predict(data)
    print(np.sum(pred.astype(np.int32)==labels)/labels.shape[0])
    
if __name__ == '__main__':
    testID31()
    testID32()