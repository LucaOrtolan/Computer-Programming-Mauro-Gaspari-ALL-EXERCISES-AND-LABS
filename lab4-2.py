##Write a script that asks the user for an integer N and creates two
##lists of integer that represent two vectors having length N, filling
##them with random numbers in the interval [1.100].
##● Use the random module to generate random numbers as follow:
##import random
##newNumber = random.randint(1,100)
##● Compute a list of their multiplication, remove from the list the odd
##numbers and print it.
##● For example: N=3 → [2,4,5] [1,3,5]→[2,12,25]→ [2.12]

import random

N=int(input("Insert lenght of vector: "))
vec1=[]
vec2=[]
i=0

while i<N:
    vec1.append(random.randint(1,100))
    vec2.append(random.randint(1,100))
    i+=1

print(vec1,vec2)


M=[]
j=0
while j<len(vec1):
    m=vec1[j]*vec2[j]
    M.append(m)
    j+=1

print(M)

k=0
while k<len(M):     #don't use for k in range: the lenght of the string is variable! If there are odd numbers the index will be out of range
    if M[k]%2!=0:
        del M[k]
    k+=1

print(M)
