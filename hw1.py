#Esercizio1
def time(years,weeks,days):
    d=years*365+weeks*7+days
    h=d*24
    m=h*60
    s=m*60
    return (d,h,m,s)
q= time(15,7,5)
print(q)

#Esercizio2
import math
def Pyt(leg1,leg2):
    hyp=math.sqrt(leg1**2+leg2**2)
    return(hyp)
h= Pyt(32,46)
print(h)

#Esercizio3
import math
def cir(D):
    per=(D/math.sqrt(2))*4
    dia=per
    area=((dia/2)**2)*math.pi
    return(area)

D=float(input("insert diagonal's value:"))
print("the area of the circle is:", cir(D))

def time(N):
    hours=N*24
    seconds=hours*3600
    return(hours,seconds)

N=int(input("insert number of years:"))
print("the number of hours and seconds are respectively:", time(N))
