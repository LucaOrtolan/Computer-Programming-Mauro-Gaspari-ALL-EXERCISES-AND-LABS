import math
def trig(degree):
    rad=degree*2*math.pi/360
    s=math.sin(rad)
    c=math.cos(rad)
    t=math.tan(rad)
    return(s,c,t)
y=trig(75)
print(y)
