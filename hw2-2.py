import math
def circle(c1,c2,x1,y1,x2,y2):
    rad2=math.sqrt((c1+x2)**2+(c2+y2)**2)
    rad1=math.sqrt((c1+x1)**2+(c2+y1)**2)
    perim1=(rad1*2*math.pi)
    perim2=(rad2*2*math.pi)
    if perim1>perim2:
        print("Circle 1 is the largest with perimeter=",perim1)
    elif perim1<perim2:
        print("Circle 2 is the largest with perimeter=",perim2)
    else:
        print("The two circles are equals")

c1=float(input("Insert x of center: "))
c2=float(input("Insert y of center: "))
x1=float(input("Insert x of point 1: "))
y1=float(input("Insert y of point 1: "))
x2=float(input("Insert x of point 2: "))
y2=float(input("Insert y of point 2: "))
circle(c1,c2,x1,y1,x2,y2)
