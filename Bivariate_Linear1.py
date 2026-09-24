import numpy as np 
import math as mt

x = np.array([34,108,64,88,99,51])   # Total bill 
y = np.array([5,17,11,8,14,5])       # Tip Amount($)

mean_x = np.mean(x)
mean_y = np.mean(y)
print(mean_x)
print(mean_y)

bill_deviation = x-mean_x
# print(bill_deviation)

Tip_deviation = y-mean_y
# print(Tip_deviation)

Deviation_Products = bill_deviation*Tip_deviation

sum_dev_pro = np.sum(Deviation_Products)
print(sum_dev_pro)

Bill_dev_squared = bill_deviation**2

sum_dev_squ = np.sum(Bill_dev_squared)
print(sum_dev_squ)

# slope (b1)-----------------------------------------------------------------------------
b1 = sum_dev_pro/sum_dev_squ
print("b1 : ",b1)

# Intercept (b0)---------------------------------------------------------------
b0 = mean_y - b1*mean_x
print("b0 : ",b0)

# Your Regression Line---------------------------------------------
yi = b0 + b1*x
print("Yi",yi)





print("==============================Calculation=========================")
print("Total bill : ",x)
print("Tip amount: ",y)
print("Bill_deviation: ",bill_deviation)
print("Tip_deviation: ",Tip_deviation)
print("Deviation_Products: ",Deviation_Products)
print("Bill deviation squared: ",Bill_dev_squared)
print("sum_dev_products: ",sum_dev_pro)
print("sum_bill_dev_squ: ",sum_dev_squ)
print("===============================================================")

# Correlation============================================================

n = len(x)
xy = x*y
sumxy = np.sum(xy)
sumx = np.sum(x)
sumy = np.sum(y)
sq_x = x**2
sq_y = y**2
sum_sq_x = np.sum(sq_x)
sum_sq_y = np.sum(sq_y)
sq_sumx = sumx**2
sq_sumy = sumy**2
v = (n*(sum_sq_x)-(sq_sumx))*(n*(sum_sq_y)-(sq_sumy))
r = (n*(sumxy)-(sumx)*(sumy)) / mt.sqrt(v)
print("Correlation",r)


# Yi b0 b1 ===============================================================

yi = b0 + b1*xi