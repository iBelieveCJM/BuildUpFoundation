# -*- coding: utf-8 -*-
"""
@author: CJM

Here I want to pre-process the Titanic dataset, view the data first

RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64    # (drop)     one-based id
Survived       891 non-null int64    # (label)    {0,1}, 0:die; 1:survived
Pclass         891 non-null int64    # (discrete) {1,2,3}, the class of cabin
Name           891 non-null object   # (drop)
Sex            891 non-null object   # (discrete) {male,female}, gender of passenger
Age            714 non-null float64  # (continue)
SibSp          891 non-null int64    # (continue) the number of brothers and sisters
Parch          891 non-null int64    # (continue) the number of parents and children
Ticket         891 non-null object   # (drop)     the id of ticket
Fare           891 non-null float64  # (continue)
Cabin          204 non-null object   # (drop)     the id of cabin
Embarked       889 non-null object   # (discrete) {S,C,Q}, the port where the passenger got on the ship
dtypes: float64(2), int64(5), object(5)

the pre-process procedure is as follow:
    1. Drop some features. Here I drop "PassengerId", "Name", "Ticket", "Cabin". Then I have 8 features left.
    2. Using "Survived" as label, then another 7 features are data.
    3. Simply drop all nan values.
    
Finally, I have 3 discrete features and 4 continue featurs.
"""

import pandas as pd

def dataDrop(data):
    for i in ["PassengerId", "Name", "Ticket", "Cabin"]:
        data.pop(i)

def process(filePath):
    data = pd.read_csv(filePath)
    dataDrop(data)
    data = data.dropna()
    data['Pclass'] = data['Pclass'].astype('category')
    labels = data.pop('Survived')
    return data, labels