import numpy as np 
import pandas as pd 
import MLLib

class LinearRegression:
    def loadFile(self,filename):
        self.data = pd.read_csv(filename)

    def dataCleaning(self,categorial):
        self.data=MLLib.encoder(self.data,categorial)
        print(self.data)
    

model = LinearRegression()
model.loadFile("d:/Coding/All PPTs & Assignments/Machine Learning/mumbai.csv")
column = ['locality','city','property_type','furnished']
model.dataCleaning(column)
print(model.data['furnished'])



    
    