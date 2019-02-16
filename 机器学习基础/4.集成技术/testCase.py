# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd
#from id3 import ID3Tree
#from C4_5 import C45Tree
from sklearn.tree import DecisionTreeClassifier as Tree
from cart_classification import CART_weight_classifier
from adaboost import AdaBoost
from bagging import Bagging

DEBUG = False
    
def testTitanicCART():
    print('-'*30, '\ntestTitanicCART\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless and continue features
    #for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
    for i in ["PassengerId", "Name", "Ticket", "Cabin"]:
        trd.pop(i)
    trd = trd.dropna()        # drop nan values
    # convert non-digits to digits
    trd = pd.get_dummies(trd, columns=['Sex'])
    Embarked_map = {val:idx for idx, val in enumerate(trd['Embarked'].unique())}
    trd['Embarked'] = trd['Embarked'].map(Embarked_map)
    if DEBUG: print(trd[:5])
    # create train data
    trdd = trd.sample(frac=0.4)
    # using "Survived" as labels
    trl = trd.pop("Survived")
    trll = trdd.pop("Survived")
    # training tree
    t = CART_weight_classifier()
    t.fit( trdd, trll, pd.Series(np.ones(trdd.shape[0])/trdd.shape[0], index=trll.index) )
    print(t.tree)
    # prediction
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
def testTitanicCARTAdaBoost():
    print('-'*30, '\ntestTitanicCARTAdaBoost\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless and continue features
    #for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
    for i in ["PassengerId", "Name", "Ticket", "Cabin"]:
        trd.pop(i)
    trd = trd.dropna()        # drop nan values
    # convert non-digits to digits
    trd = pd.get_dummies(trd, columns=['Sex'])
    Embarked_map = {val:idx for idx, val in enumerate(trd['Embarked'].unique())}
    trd['Embarked'] = trd['Embarked'].map(Embarked_map)
    if DEBUG: print(trd[:5])
    # create train data
    trdd = trd.sample(frac=0.4)
    # using "Survived" as labels
    trl = trd.pop("Survived")
    trl[trl==0] = -1
    trll = trdd.pop("Survived")
    trll[trll==0] = -1
    # training tree
    t = AdaBoost(CART_weight_classifier, 10)
    t.fit( trdd, trll )
    # prediction
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
def testTitanicCARTBagging():
    print('-'*30, '\ntestTitanicCARTBagging\n', '-'*30)
    trd = pd.read_csv('Titanic_dataset/train.csv')
    # drop useless and continue features
    #for i in ["PassengerId", "Name", "Ticket", "Cabin", "Age", "SibSp", "Parch", "Fare"]:
    for i in ["PassengerId", "Name", "Ticket", "Cabin"]:
        trd.pop(i)
    trd = trd.dropna()        # drop nan values
    # convert non-digits to digits
    trd = pd.get_dummies(trd, columns=['Sex'])
    Embarked_map = {val:idx for idx, val in enumerate(trd['Embarked'].unique())}
    trd['Embarked'] = trd['Embarked'].map(Embarked_map)
    if DEBUG: print(trd[:5])
    # create train data
    trdd = trd.sample(frac=0.4).reset_index(drop=True)
    # using "Survived" as labels
    trl = trd.pop("Survived")
    trll = trdd.pop("Survived")
    # training tree
    t = Bagging(CART_weight_classifier, 10)
    t.fit( trdd, trll )
    # prediction
    pred = t.predict(trd)
    print('Acc.: ', np.sum(pred==trl.reset_index(drop=True))/trl.shape[0])
    
if __name__ == '__main__':
    #testTitanicCART()
    #testTitanicCARTAdaBoost()
    testTitanicCARTBagging()