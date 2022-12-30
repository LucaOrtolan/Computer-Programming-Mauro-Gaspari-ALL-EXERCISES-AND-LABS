##● Given a recursive function that returns the
##fibonacci number of an integer n.
##● Write a script that gets as input an integer n and
##returns a list containing the first n fibonacci
##numbers.


n=int(input("Give me an integer: "))

def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
r=[]
i=0
while i<n:
    r.append(fib(i))
    i+=1
print(r)

#Other approach

r1=[0]*n

for i in range(n):
    r1[i]=fib(i)

print(r1)


#Random list
import random
L(i)=random.
