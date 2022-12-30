def GCD(a,b):
    if a<b:
        c=a 
        a=b 
        b=c
    R=a%b
    if R==0:
        return b
    else:
        a=b
        b=R
        return GCD(a,b)
a=int(input("a= "))
b=int(input("b= "))
print(GCD(a,b))
    
    
