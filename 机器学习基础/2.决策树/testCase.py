# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd
from id3 import ID3Tree
from C4_5 import C45Tree
from sklearn import tree
import graphviz

DEBUG = False

def testTitanicsklearn():
    print('-'*30, '\testTitanicsklearn\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless and continue features
    for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
        trd.pop(i)
    trd = trd.dropna()        # drop nan values
    # convert non-digits to digits
    trd = pd.get_dummies(trd, columns=['Sex'])
    Embarked_map = {val:idx for idx, val in enumerate(trd['Embarked'].unique())}
    trd['Embarked'] = trd['Embarked'].map(Embarked_map)
    if DEBUG: print(trd[:5])
    # create train data
    trdd = trd.sample(frac=1.0)
    # using "Survived" as labels
    trl = trd.pop("Survived")
    trll = trdd.pop("Survived")
    # training tree
    t = tree.DecisionTreeClassifier(criterion='entropy')
    t.fit(trdd, trll)
    # prediction
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    # visulize the tree
    dot_data = tree.export_graphviz(t, out_file=None, 
                  feature_names=trdd.columns)
    graph = graphviz.Source(dot_data)
    graph.view()

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
    if DEBUG: print(data)
    labels = pd.Series(np.array([1,1,2,0,0]), name='labels')
    if DEBUG: print(labels)
    
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
    if DEBUG: print(data)
    labels = pd.Series(np.array([1,1,2,0,0]), name='labels')
    if DEBUG: print(labels)
    
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
    trd = pd.get_dummies(trd, columns=['Sex'])
    Embarked_map = {val:idx for idx, val in enumerate(trd['Embarked'].unique())}
    trd['Embarked'] = trd['Embarked'].map(Embarked_map)
    if DEBUG: print(trd[:5])
    # create train data
    trdd = trd.sample(frac=0.4)
    trl = trd.pop("Survived")   # using "Survived" as labels
    trll = trdd.pop("Survived")
    
    t.fit(trdd, trll)
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
def testTitanic(t):
    print('-'*30, '\ntestTitanicC4_5\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless features
    for i in ["PassengerId", "Name", "Ticket", "Cabin"]:
        trd.pop(i)
    trd = trd.dropna()        # drop nan values
    trd = pd.get_dummies(trd, columns=['Sex'])
    Embarked_map = {val:idx for idx, val in enumerate(trd['Embarked'].unique())}
    trd['Embarked'] = trd['Embarked'].map(Embarked_map)
    if DEBUG: print(trd[:5])
    # create train data
    trdd = trd.sample(frac=0.4)
    trl = trd.pop("Survived")   # using "Survived" as labels
    trll = trdd.pop("Survived") # using "Survived" as labels
    
    t.fit(trdd, trll)
    print(t.tree)
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
if __name__ == '__main__':
    t = ID3Tree()
    #t = C45Tree()
    #test1(t)
    #test2(t)
    testTitanicDiscrete(t)
    #testTitanic(t)