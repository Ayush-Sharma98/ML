import pandas as pd 
import numpy as np

def test_train_splits(data_x,data_y):
    L = len(data_x)
    train_size = int(L*0.8)
    # test_size = int(L*0.2)
    return [data_x.loc[0:train_size],data_x.loc[train_size:L],data_y.loc[0:train_size],data_y.loc[train_size:L]]

def encoder(data,col_list):
    for col in col_list:
        T = data[col].unique()
        T.sort()
        mapping={}
        for i,V in enumerate(T):
            mapping[V] = i

        data[col]=data[col].map(mapping)
        print(data['furnished'])
        return data