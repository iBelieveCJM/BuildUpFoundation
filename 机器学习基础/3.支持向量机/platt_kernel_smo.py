# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import kernel
from kernel import rbf

class plattKernelSMO():
    
    def __init__(self, C, eps, kernelArgs=('rbf', 1.0)):
        self.alphas = None
        self.eCache = None
        self.w_ = None
        self.supportVecs = None
        self.supportVecLabels = None
        self.kernelTrans = self.kernel(kernelArgs)
        self.b_ = 0
        self.C = C
        self.eps = eps
        
    def predict_prob(self, data):
        if self.alphas is None:
            print('error: the model had not been trained')
            return #should raise the expection
        wx = np.dot(self.alphas[self.supportVecIdx()]*self.supportVecLabels, 
                    self.kernelTrans(self.supportVecs, data))
        return wx + self.b_
    
    def predict(self, data):
        if self.w_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return np.sign(self.predict_prob(data))
    
    def supportVecIdx(self):
        if self.w_ is None:
            print('error: the model had not been trained')
            return #should raise the expection
        return np.nonzero(self.alphas)[0]
        
    def fit(self, data, labels, maxIter=100):
        nSample = data.shape[0]
        self.alphas = np.zeros(nSample)
        self.eCache = np.zeros(nSample)
        K = self.kernelTrans(data, data)
        entireSet, alphaPairsChanged = True, 0
        loop = 0
        while(loop<maxIter) and ((alphaPairsChanged>0)or(entireSet)):
            alphaPairsChanged = 0
            if entireSet:
                for i in range(nSample):
                    alphaPairsChanged += self.alphaPairOptim(labels, K, i)
                    print(f"[EntireSet]iter: {loop}, i:{i}, pairs changed: {alphaPairsChanged}")
            else:
                nonBoundIdx = np.nonzero((self.alphas>0)*(self.alphas<self.C))[0]
                for i in nonBoundIdx:
                    alphaPairsChanged += self.alphaPairOptim(labels, K, i)
                    print(f"[Non-bound]iter: {loop}, i:{i}, pairs changed: {alphaPairsChanged}")
            loop += 1
            if entireSet:
                entireSet = False
            elif alphaPairsChanged == 0:
                entireSet = True
            else:
                print(f"iteratoin: {loop}")
        #end_while
        self.w_ = np.dot(self.alphas*labels, data)
        self.supportVecs = data[self.supportVecIdx()]
        self.supportVecLabels = labels[self.supportVecIdx()]
        
    def alphaPairOptim(self, labels, K, i):        
        Ei = self.predictAlpha(labels,K[:,i])-labels[i]
        if ((labels[i]*Ei<-self.eps)and(self.alphas[i]<self.C))\
           or((labels[i]*Ei>self.eps)and(self.alphas[i]>0)):
            # select j-th alphas
            j, Ej = self.selectJ(i, Ei)
            # the limit for alphas[j]
            alphaIold = self.alphas[i].copy()
            alphaJold = self.alphas[j].copy()
            L, H = self.bound(labels[i], labels[j], self.alphas[i], self.alphas[j])
            if L == H:
                print("L==H")
                return 0
            # eta for uncutted alphas[j]
            eta = 2.0*K[i,j] - K[i,i] - K[j,j]
            if eta >= 0:
                print("eta >= 0")  # why eta must less than 0
                return 0
            # Update alphas[j]
            self.alphas[j] -= labels[j]*(Ei-Ej)/eta
            self.alphas[j] = self.clipAlpha(self.alphas[j], L, H)
            if np.abs(self.alphas[j]-alphaJold) < 1e-5:
                print("j not moving enough")
                return 0
            # Update alphas[i]
            self.alphas[i] += labels[j]*labels[i]*(alphaJold-self.alphas[j])
            # Update b
            self.b_ = self.updateB(Ei, Ej, self.alphas[i], self.alphas[j], alphaIold, alphaJold,
                                  labels[i], labels[j], K[i,i], K[i,j], K[j,j])
            # Update E
            self.eCache[i] = self.predictAlpha(labels,K[:,i])-labels[i]
            self.eCache[j] = self.predictAlpha(labels,K[:,j])-labels[j]
            return 1
        else:
            return 0
        
    def updateB(self, Ei, Ej, ai, aj, aio, ajo, yi, yj, k11, k12, k22):
        b1 = self.b_ - Ei - yi*k11*(ai-aio) - yj*k12*(aj-ajo)
        b2 = self.b_ - Ej - yi*k12*(ai-aio) - yj*k22*(aj-ajo)
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
            
    def predictAlpha(self, labels, kd):
        wx = np.dot(self.alphas*labels, kd)
        return wx + self.b_ #b is important! forget it will be wrong!
    
    def selectJ(self, i, Ei):
        self.eCache[i] = 0
        validEcacheList = np.nonzero(self.eCache)[0] #the index of nonzero
        self.eCache[i] = Ei
        if validEcacheList.shape[0]!=0:
            deltaEs = np.abs(Ei-self.eCache[validEcacheList])
            maxIdx = validEcacheList[np.argmax(deltaEs)]
            return maxIdx, self.eCache[maxIdx]
        else:
            j = self.selectJrand(i, self.eCache.shape[0])
            return j, self.eCache[j]
            
    def selectJrand(self, i, m):
        j = i
        while(j == i):
            j = int(np.random.uniform(0,m))
        return j
    
    def kernel(self, args):
        if isinstance(args, tuple):
            method = args[0]
        else:
            method = args
        if method == 'linear':
            return kernel.linear()
        elif method == 'rbf':
            assert len(args)==2
            return kernel.rbf(args[1])
        else:
            return kernel.linear()