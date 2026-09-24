import numpy as np 
import pandas as pd 
from Linear_Regretion1 import LinearRegretionM

class LinearRegression:
    def loadFile(self,filename):
        self.data = pd.read_csv(filename)

    def dataCleaning(self,categorial,numerical):
        self.data=LinearRegretionM.encoder(self.data,categorial)
        print(self.data)
    

model = LinearRegretionM()
model.loadFile("d:/Coding/All PPTs & Assignments/Machine Learning/mumbai.csv")
column = ['locality','city','property_type','furnished']
model.datacleaning(column)
print(model)



    
    