
import numpy as np 
import pandas as pd

class Kmean:
    def __init__(self,k):
        self.k=k
        self.centroid=None
        self.clusters = None
    def fit(self,data):
        self.centroid=[4,11]

        for i in range(100):
            clusters=[[] for i in range(self.k)]   # we can take 2 in place of self.k means how many value we want 
            for v in data:
                distance=[]
                for c in self.centroid:
                    dis = abs(v-c)
                    distance.append(dis)
                cluster_index=distance.index(min(distance))
                clusters[cluster_index].append(v)
            # print(clusters)
            nc=[]   # new cluster 
            for cluster in clusters:
                if(len(cluster) > 0):
                    nc.append(sum(cluster)/len(cluster))
                else:
                    nc.append(0)
            # print(nc)
            if(nc==self.clusters):
                break
            self.centroid=nc
        self.clusters=clusters 
    def show(self):
        print("Clusters:")
        print(self.clusters)
        print("centroid:")
        print(self.centroid)
    def predict(self,value):
        distance=[]
        for centroid in self.centroid:
            dis=abs(value-centroid)
            distance.append(dis)
        return distance.index(min(distance))

model = Kmean(2)
data=[2,4,10,12,3,20,30,11,25]
model.fit(data)
model.show()
value= int(input("Enter Your Value : "))
# value = 30
p=model.predict(value)
print(value,"Belongs to cluster",model.clusters[p])
