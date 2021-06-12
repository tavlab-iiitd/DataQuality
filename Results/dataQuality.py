# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:34:38 2021

@author: DELL
"""
import pandas as pd
from sklearn.metrics import pairwise_distances

df = pd.read_csv('MLmodelTrainingDataset.csv')

df.drop('DatasetName',axis='columns', inplace=True)
pd.to_numeric(df['MetadataCoupling'])

Values=df.iloc[:,:-1]
cosinMatrix = 1-pairwise_distances(Values, metric="cosine")

for i in range(1,cosinMatrix.shape[0]):
    sim=cosinMatrix[i][0]
    df['DataQuality'][i]=sim*100
    
df.to_csv('cosineRESULTS2.csv')


print(type(df['MetadataCoupling'][1]))
        
        