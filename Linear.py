import numpy as np

#-------------------------------------------------------------------------------------------------------------------
#                                               Calculation
#-------------------------------------------------------------------------------------------------------------------
x = np.array([34,108,64,88,99,51])
y = np.array([5,17,11,8,14,5])

mean_x = np.mean(x)
mean_y = np.mean(y)
print(mean_x)
print(mean_y)

xi = x-mean_x
print(xi)
# xi means sum of all values of x
yi = y-mean_y
print(yi)

mult_xiyi=xi*yi
print(mult_xiyi)


sumss=np.sum(mult_xiyi)
print(sumss)

square=xi**2
add=np.sum(square)
print(add)
print(square)

































# Bill_deviation = xi - mean_x
# Tip_deviation = yi - mean

# Deviation_Products = (Bill_deviation)*(Tip_deviation)

# Bill_dev_squared = Bill_deviation**2

# sum_dev_products= np.sum(Deviation_Products)
# sum_bill_dev_squ = np.sum(Bill_dev_squared)

# print("Total bill : ",xi)
# print("Tip amount: ",yi)
# print("Bill_deviation: ",Bill_deviation)
# print("Tip_deviation: ",Tip_deviation)
# print("Deviation_Products: ",Deviation_Products)
# print("Bill deviation squared: ",Bill_dev_squared)
# print("sum_dev_products: ",sum_dev_products)
# print("sum_bill_dev_squ: ",sum_bill_dev_squ)
