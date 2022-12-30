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
