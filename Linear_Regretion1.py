import numpy as np 
import math as mt
class LinearRegretionM:
    def __init__(self,x,y):
        self.__x = np.array(x)
        self.__y = np.array(y)

    def cofficient_of_coreletion(self):
        '''
        sum_of_X = sum(self.__x)
        sum_of_Y = sum(self.__y)
        Mean_x = np.mean(self.__x)
        Mean_y = np.mean(self.__y)
        bill_deviations = self.__x - Mean_x
        tip_devialtions =  self.__y - Mean_y
        deviation_product = (bill_deviations)*(tip_devialtions)
        sum_deviattion_product = sum(deviation_product)
        r = (N * SXY - SX * SY)/mt.sqrt((N*SXY - SX * SX) * (N * SYY - SY * SY))
        return r
        '''
        n = len(self.__x)
        xy = self.__x*self.__y
        sumxy = np.sum(xy)
        sumx = np.sum(self.__x)
        sumy = np.sum(self.__y)
        sq_x = self.__x**2
        sq_y = self.__y**2
        sum_sq_x = np.sum(sq_x)
        sum_sq_y = np.sum(sq_y)
        sq_sumx = sumx**2
        sq_sumy = sumy**2
        v = (n*(sum_sq_x)-(sq_sumx))*(n*(sum_sq_y)-(sq_sumy))
        r = (n*(sumxy)-(sumx)*(sumy)) / mt.sqrt(v)
        # print("Correlation",r)
        return r

def encoder(data,col_list):
    for col in col_list:
        T = data['furnished'].unique()
        mapping={}
        for i,V in enumerate(T):
            mapping[V] = i

        data[col]=data[col].map(mapping)

    def fit(self):   # b1 means slope   and b0 means intercept
        self.slope = sum((self.__x-np.mean(self.__x))*(self.__y-np.mean(self.__y)))/sum((self.__x-np.mean(self.__x))**2)
        # print("Slope (b1):",self.slope)
        self.intercept = np.mean(self.__y)-self.slope*np.mean(self.__x)
        # print("Intercept (b0):",self.intercept)

    def predict(self,input):
        R = []
        for v in input:
            r = self.intercept+self.slope*v
            R = np.append(r)
            return np.array(R)

    def MSE(self,PY):    # Predicted  value Input 
        diff = self.__y-PY
        sq = diff**2
        mse = sq.sum()
        return mse



