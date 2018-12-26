# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np

class simpleSMO():
    
    def __init__(self, C, eps):
        self.alphas = None
        self.w_ = None
        self.b_ = 0
        self.C = C
        self.eps = eps
        
    def predict_prob(self, data):
        if self.w_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return self.w_.dot(data.T) + self.b_
    
    def predict(self, data):
        if self.w_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return np.sign(self.predict_prob(data))
        
    def fit(self, data, labels, maxIter=100):
        etaFunc = lambda xi,xj: 2.0*xi.dot(xj) - xi.dot(xi) - xj.dot(xj)
        nSample, dim = data.shape
        self.alphas = np.zeros(nSample)
        loop = 0
        while(loop < maxIter):
            alphaPairsChanged = 0
            for i in range(nSample):
                Ei = self.predictAlpha(data,labels,data[i])-labels[i]
                if ((labels[i]*Ei<-self.eps)and(self.alphas[i]<self.C))\
                   or((labels[i]*Ei>self.eps)and(self.alphas[i]>0)):
                    # select j-th alphas
                    j = self.selectJrand(i, nSample)
                    Ej = self.predictAlpha(data,labels,data[j])-labels[j]
                    # the limit for alphas[j]
                    alphaIold = self.alphas[i].copy()
                    alphaJold = self.alphas[j].copy()
                    L, H = self.bound(labels[i], labels[j], self.alphas[i], self.alphas[j])
                    if L == H:
                        print("L==H")
                        continue
                    # eta for uncutted alphas[j]
                    eta = etaFunc(data[i], data[j])
                    if eta >= 0:
                        print("eta >= 0")  # why eta must less than 0
                        continue
                    # Update alphas[j]
                    self.alphas[j] -= labels[j]*(Ei-Ej)/eta
                    self.alphas[j] = self.clipAlpha(self.alphas[j], L, H)
                    if np.abs(self.alphas[j]-alphaJold) < 1e-5:
                        print("j not moving enough")
                        continue
                    # Update alphas[i]
                    self.alphas[i] += labels[j]*labels[i]*(alphaJold-self.alphas[j])
                    # Update b
                    self.b_ = self.updateB(Ei, Ej, self.alphas[i], self.alphas[j], alphaIold, alphaJold,
                                          data[i], data[j], labels[i], labels[j])
                    alphaPairsChanged += 1
                    print(f"iter: {loop}, i: {i}, pairs changed {alphaPairsChanged}")
                #end_if
            #end_for
            if alphaPairsChanged == 0:
                loop += 1
            else:
                print(f"iteratoin: {loop}")
        #end_while
        self.w_ = np.dot(self.alphas*labels, data)
                    
    def updateB(self, Ei, Ej, ai, aj, aio, ajo, xi, xj, yi, yj):
        b1 = self.b_ - Ei - yi*xi.dot(xi)*(ai-aio) - yj*xj.dot(xi)*(aj-ajo)
        b2 = self.b_ - Ej - yi*xi.dot(xj)*(ai-aio) - yj*xj.dot(xj)*(aj-ajo)
        if (0 < ai) and (self.C > ai):
            return b1
        elif (0 < aj) and (self.C > aj):
            return b2
        else:
            return (b1+b2)*.5
                    
    def clipAlpha(self, aj, L, H):
        aj = H if aj > H else aj
        aj = L if aj < L else aj
        return aj
                    
    def bound(self, yi, yj, ai, aj):
        if yi != yj:
            L = max(0, aj - ai)
            H = min(self.C, self.C + aj - ai)
        else:
            L = max(0, aj + ai -self.C)
            H = min(self.C, aj + ai)
        return L, H
            
    def predictAlpha(self, data, labels, d):
        w = np.dot(self.alphas*labels, data)
        return w.dot(d) + self.b_ #b is important! forget it will be wrong!
    
    def selectJrand(self, i, m):
        j = i
        while(j == i):
            j = int(np.random.uniform(0,m))
        return j