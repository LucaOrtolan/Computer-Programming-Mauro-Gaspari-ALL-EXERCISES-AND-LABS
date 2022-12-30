#Write a script that takes one integer N as an input and computes
#using recursion the sum of the factorials from 1 to N.

def fact(N):
    if N==0:
        return 1
    else:
        return N*fact(N-1)

def sumfact(N):
    if N==1:
        return 1
    else:
        return fact(N)+sumfact(N-1)
        
N=int(input("Insert number: "))
print(sumfact(N))

