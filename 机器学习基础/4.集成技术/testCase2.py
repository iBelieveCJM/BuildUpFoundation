# -*- coding: utf-8 -*-
"""
@author: CJM
"""
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

import numpy as np
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import  train_test_split
from sklearn.model_selection import cross_val_score, cross_validate

from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier as Tree
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.ensemble import AdaBoostClassifier as AdaBoost
from sklearn.naive_bayes import GaussianNB

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA

if __name__ == '__main__':
#    X, y = make_classification(n_samples=200,
#                               n_features=2,
#                               n_redundant=0,
#                               n_informative=2,
#                               n_classes=2,
#                               random_state=1,
#                               n_clusters_per_class=1,
#                               shuffle=True)
    
#    X, y = make_moons(n_samples=200,
#                      noise=0.2,
#                      random_state=1,
#                      shuffle=True)
    
    X, y = make_circles(n_samples=200,
                        noise=0.05,
                        random_state=1,
                        shuffle=True)
    
    ## split the data
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.25)
    ## pre-processing
    scaler = StandardScaler().fit(X_train)
    X_train, X_test = scaler.transform(X_train), scaler.transform(X_test)
    
    clf = KNN(3)
    #clf = SVC(gamma=2, C=1)
    #clf = Tree(max_depth=5)
    #clf = RF(max_depth=5, n_estimators=10, max_features=1)
    #clf = AdaBoost()
    #clf = GaussianNB()
    #clf = LDA()
    #clf = QDA()
    
#    ## training model
#    clf.fit(X_train, y_train)
#    y_tr_pred = clf.predict(X_train)
#    ## testing model
#    y_tt_pred = clf.predict(X_test)
#    
#    ## plot the orgial data
#    fig = plt.figure()
#    # orginal training data
#    ax1 = fig.add_subplot(221)
#    ax1.plot(X_train[y_train==0,0], X_train[y_train==0,1], '*r', 
#            X_train[y_train==1,0], X_train[y_train==1,1], '*b')
#    ax1.set_title('orginal training data')
#    # orginal testing data
#    ax2 = fig.add_subplot(222)
#    ax2.plot(X_test[y_test==0,0], X_test[y_test==0,1], '*r', 
#             X_test[y_test==1,0], X_test[y_test==1,1], '*b')
#    ax2.set_title('orginal testing data')
#    # predictional training data
#    ax3 = fig.add_subplot(223)
#    ax3.plot(X_train[y_tr_pred==0,0], X_train[y_tr_pred==0,1], '*r', 
#             X_train[y_tr_pred==1,0], X_train[y_tr_pred==1,1], '*b')
#    ax3.set_title('predictional training data')
#    # predictional training data
#    ax4 = fig.add_subplot(224)
#    ax4.plot(X_test[y_tt_pred==0,0], X_test[y_tt_pred==0,1], '*r', 
#             X_test[y_tt_pred==1,0], X_test[y_tt_pred==1,1], '*b')
#    ax4.set_title('predictional testing data')
#    
#    ## show the figure
#    plt.show()
    
    ## cross validation score
    #scores = cross_val_score(clf, X, y, cv=5)
    #print(scores, scores.mean())
    scores = cross_validate(clf, X, y, cv=5)
    for k,v in scores.items():
        print(k, v)