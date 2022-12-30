import math
def cost(diam_cm,price):
    diam_m=diam_cm/100
    area=(diam_m/2)**2*math.pi
    pmq=area/price
    return(pmq)

diam_cm=int(input("insert pizza's diameter in cm:"))
price= float(input("insert pizza's price:"))
print("price of pizza per square meter is:", cost(diam_cm,price))
             

