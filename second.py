from Linear_Regretion1 import LinearRegretion

amount = [34,108,64,88,99,51]  # Total bill 
tip = [5,17,11,8,14,5]
model = LinearRegretion(amount,tip)
model.fit()
print(model.intercept,model.slope)
test = [70,2000]
p = model.predict(test)
print(p)
# p=model.predict(amount)
# print(p)

K = model.MSE(p)
print(K)