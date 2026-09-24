import pandas as pd 
import numpy as np 

df = pd.read_csv("D:/Coding/All PPTs & Assignments/Machine Learning/mumbai.csv")


T = df['furnished'].unique()
print(T)
mapping={}
for i,V in enumerate(T):
    mapping[V]=i
# print(mapping)
df['furnished']=df['furnished'].map(mapping)
print(df['furnished'])


# =====================================================
# creating def function of the above code. 
# ========================================================

def encoder(data,col_list):
    for col in col_list:
        T = data['furnished'].unique()
        mapping={}
        for i,V in enumerate(T):
            mapping[V] = i

        data[col]=data[col].map(mapping)
        
