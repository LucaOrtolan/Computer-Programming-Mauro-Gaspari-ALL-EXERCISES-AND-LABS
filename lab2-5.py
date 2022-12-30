def GCD(a,b):
    if a<b:
        c=a 
        a=b 
        b=c
        return GCD(a,b)
    else:
        R=a%b
        if R==0:
            return b
        else:
            a=b
            b=R
            return GCD(a,b)
def LCM(a,b):
     m=(a*b)/GCD(a,b)
     return m
a=int(input("a= "))
b=int(input("b= "))
print("Least common multiple between",a,"and",b,"is:",LCM(a,b))
