import math
#def pythagoras(leg1,leg2):
    #hypo=math.sqrt(leg1**2+leg2**2)
    #return hypo
#leg1=float(input("Insert lenght of first leg: "))
#leg2=float(input("Insert lenght of second leg: "))
#print("The hypothenuse is: ",pythagoras(leg1,leg2))

triangle=str(input("Is it right angled or equilateral?: "))
def perimeter(triangle):
    if triangle=="right angled":
        leg1=int(input("Insert first leg: "))
        leg2=int(input("Insert second leg: "))
        hypo=math.sqrt(leg1**2+leg2**2)
        perim=leg1+leg2+hypo
        print("Perimeter is: ",perim)
    elif triangle=="equilateral":
        leg1=int(input("Insert leg: "))
        perim=leg1*3
        print("Perimeter is: ",perim)
    else:
        print("Type right angle or equilateral")
perimeter(triangle)
 

    
    
