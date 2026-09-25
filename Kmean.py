import numpy as np 
import pandas as pd

class Kmean:
    def __init__(self,k):
        self.k=k
        self.centroid=None
        self.clusters = None
    def fit(self,data):
        self.centroid=[4,11]

        clusters=[[] for i in range(self.k)]   # we can take 2 in place of self.k means how many value we want 
        for v in data:
            distance=[]
            for c in self.centroid:
                dis = abs(v-c)
                distance.append(dis)
            cluster_index=distance.index(min(distance))
            clusters[cluster_index].append(v)
        print(clusters)

model = Kmean(2)
data=[2,4,10,12,3,20,30,11,25]
model.fit(data)
