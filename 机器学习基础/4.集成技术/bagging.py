# -*- coding: utf-8 -*-
"""
@author: CJM
"""

import numpy as np
import pandas as pd

class Bagging:
    
    def __init__(self, baseModel, model_n):
        self._buildModel = baseModel
        self.model_n = model_n
        self.model = []
        
    def predict(self, data):
        predList = []
        for base in self.model:
            predList.append(base.predict(data))
        predMat = np.stack(predList).astype(np.int64)
        return np.apply_along_axis(lambda x: np.argmax(np.bincount(x)),
                                   axis=0, arr=predMat)
    def fit(self, data, labels):
        for i in range(self.model_n):
            rIdx = self.bootstrap(labels.shape[0])
            cur_data, cur_labels = data.iloc[rIdx], labels.iloc[rIdx]
            weights = pd.Series(np.ones(cur_labels.shape[0])/cur_labels.shape[0],
                                index=cur_labels.index)
            base = self._buildModel()
            base.fit(cur_data, cur_labels, weights)
            self.model.append(base)
            ## oob error
            oobIdx = list(set(list(range(labels.shape[0]))) - set(rIdx))
            oob_data, oob_labels = data.iloc[oobIdx], labels.iloc[oobIdx]
            acc = np.sum(base.predict(oob_data)==oob_labels)/oob_labels.shape[0]
            print('{}-th model done, oob Acc. {}'.format(i, acc))
                
    def bootstrap(self, n_sample):
        return np.random.randint(n_sample, size=n_sample)