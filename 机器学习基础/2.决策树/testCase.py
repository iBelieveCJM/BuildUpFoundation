# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd
from id3 import ID3Tree
from C4_5 import C45Tree

def test1(t):
    print('-'*30, '\ntest1\n', '-'*30)
    data = np.array(
            [[1,1,1],
             [1,1,1],
             [1,2,2],
             [2,1,2],
             [2,1,2]])
    data = pd.DataFrame(data, columns=list('abc'))
    data = data.apply(lambda x: x.astype('category'))
    #for col in list('abc'):
    #    data[col] = data[col].astype('category')
    print(data)
    labels = pd.Series(np.array([1,1,2,0,0]), name='labels')
    print(labels)
    
    t.fit(data, labels)
    print(t.tree)
    pred = t.predict(data)
    print(pred)
    print('Acc.: ', np.sum(pred==labels)/labels.shape[0])
    
def test2(t):
    print('-'*30, '\ntest2\n', '-'*30)
    data = np.array(
            [[1,1],
             [1,1],
             [1,2],
             [2,1],
             [2,1]])
    data = pd.DataFrame(data, columns=list('ab'))
    data = data.apply(lambda x: x.astype('category'))
    print(data)
    labels = pd.Series(np.array([1,1,2,0,0]), name='labels')
    print(labels)
    
    t.fit(data, labels)
    print(t.tree)
    pred = t.predict(data)
    print('Acc.: ', np.sum(pred==labels)/labels.shape[0])
                
def testTitanicDiscrete(t):
    print('-'*30, '\ntestTitanicDiscrete\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless and continue features
    for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
        trd.pop(i)
    trd = trd.dropna()        # drop nan values
    trl = trd.pop("Survived") # using "Survived" as labels
    
    t.fit(trd, trl)
    print(t.tree)
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
#    # test test data
#    ttd = pd.read_csv('Titanic_dataset/test.csv')
#    for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
#        ttd.pop(i)
#    ttd = ttd.dropna()
#    pred = t.predict(ttd)
    
def testTitanicC4_5(t):
    print('-'*30, '\ntestTitanicC4_5\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless features
    for i in ["PassengerId", "Name", "Ticket", "Cabin"]:
        trd.pop(i)
    trd = trd.dropna()        # drop nan values
    trd['Pclass'] = trd['Pclass'].astype('category')
    #trd = trd[:100]
    print(trd.shape)
    trl = trd.pop("Survived") # using "Survived" as labels
    t.fit(trd, trl)
    print(t.tree)
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
#    # test test data
#    ttd = pd.read_csv('Titanic_dataset/test.csv')
#    for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
#        ttd.pop(i)
#    ttd = ttd.dropna()
#    pred = t.predict(ttd)
    
if __name__ == '__main__':
    #t = ID3Tree()
    t = C45Tree()
    #test1(t)
    #test2(t)
    #testTitanicDiscrete(t)
    testTitanicC4_5(t)