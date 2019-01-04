# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd
from id3 import ID3Tree
#from C4_5 import C45Tree

def testID31():
    print('-'*30, '\ntestID31\n', '-'*30)
    data = np.array(
            [[1,1,1],
             [1,1,1],
             [1,2,2],
             [2,1,2],
             [2,1,2]])
    data = pd.DataFrame(data, columns=list('abc'))
    data.apply(lambda x: x.astype('category'))
    #for col in list('abc'):
    #    data[col] = data[col].astype('category')
    print(data)
    labels = pd.Series(np.array([1,1,2,0,0]), name='labels')
    print(labels)
    
    id3Tree = ID3Tree()
    #id3Tree = C45Tree()
    id3Tree.fit(data, labels)
    print(id3Tree.tree)
    pred = id3Tree.predict(data)
    print(pred)
    print('Acc.: ', np.sum(pred==labels)/labels.shape[0])
    
def testID32():
    print('-'*30, '\ntestID32\n', '-'*30)
    data = np.array(
            [[1,1],
             [1,1],
             [1,2],
             [2,1],
             [2,1]])
    data = pd.DataFrame(data, columns=list('ab'))
    print(data)
    labels = pd.Series(np.array([1,1,2,0,0]), name='labels')
    print(labels)
    
    id3Tree = ID3Tree()
    #id3Tree = C45Tree()
    id3Tree.fit(data, labels)
    print(id3Tree.tree)
    pred = id3Tree.predict(data)
    print('Acc.: ', np.sum(pred==labels)/labels.shape[0])
                
def testTitanic():
    print('-'*30, '\ntestTitanic\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless and continue features
    for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
        trd.pop(i)
    # drop nan values
    trd = trd.dropna()
    # using "Survived" as labels
    trl = trd.pop("Survived")
    id3Tree = ID3Tree()
    #id3Tree = C45Tree()
    id3Tree.fit(trd, trl)
    print(id3Tree.tree)
    # test train data
    pred = id3Tree.predict(trd)
    #print(pred)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
#    # test test data
#    ttd = pd.read_csv('Titanic_dataset/test.csv')
#    for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
#        ttd.pop(i)
#    ttd = ttd.dropna()
#    pred = id3Tree.predict(ttd)
    
if __name__ == '__main__':
    testID31()
    testID32()
    testTitanic()