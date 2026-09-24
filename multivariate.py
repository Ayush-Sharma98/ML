import numpy as np 

# pro_x1 = [1,2,3,4]
# pro_x2 = [4,5,8,2]

# -------------creating Matrix---------------------

X = np.array([[1,2,3,4],[4,5,8,2]])
Y = np.array([1,6,8,12])
print(X)
print(Y)
print("=========================================================")
ones = np.ones((X.shape[0], 1))
X = np.hstack(ones, X)
print(X)
print(ones)