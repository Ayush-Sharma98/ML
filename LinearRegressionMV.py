import numpy as np 
import pandas as pd 
import MLLib

class LinearRegression:
    def loadFile(self,filename):
        self.data = pd.read_csv(filename)

    def dataCleaning(self,categorial,numerical):
        self.data=MLLib.encoder(self.data,categorial)
        # print(self.data)
        self.data = self.data.dropna()

    def fit():
        # x_train=
    

model = LinearRegression()
model.loadFile("d:/Coding/All PPTs & Assignments/Machine Learning/mumbai.csv")
cat = ['locality','city','property_type','furnished']
# model.dataCleaning(cat,num)
print(model.data['furnished'])



    
    