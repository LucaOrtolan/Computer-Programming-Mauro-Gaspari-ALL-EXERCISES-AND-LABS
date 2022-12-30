#Esercizio 1
import math
def trig(degree):
    rad=degree*2*math.pi/360
    s=math.sin(rad)
    c=math.cos(rad)
    t=math.tan(rad)
    return(s,c,t)
x=trig(75)
print(x)




#Esercizio 2
def sec(N):
    d=N*365
    h=24*d
    m=60*h
    s=60*m
    return(s)

N=int(input("instert number of years:"))
print("the number of seconds is:", sec(N))





#Esercizio 3
def hello(name):
    print("hello",name,",")
    print("how are you?")

name=str(input("insert name:"))
print(hello(name))




#Esercizio 4
import math
def cost(diam_cm,price):
    diam_m=diam_cm/100
    area=(diam_m/2)**2*math.pi
    pmq=area/price
    return(pmq)

diam_cm=int(input("insert pizza's diameter in cm:"))
price= float(input("insert pizza's price:"))
print("price of pizza per square meter is:", cost(diam_cm,price))
             


