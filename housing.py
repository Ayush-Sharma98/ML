import pandas as pd 
import numpy as np


def encoder(data,col_list):
    for col in col_list:
        T = data['furnished'].unique()
        T.sort()
        mapping={}
        for i,V in enumerate(T):
            mapping[V] = i

        data[col]=data[col].map(mapping)





encoder(data,column)
print(data['furnished'])

        