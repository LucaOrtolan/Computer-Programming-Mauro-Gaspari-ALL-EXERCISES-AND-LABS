#Get an integer from the user
#Create a list of n random numbers ranging from 1 to 100
#Write a function that get this list as an input and returns the maximum
#Write a function that returns the sum of the elements of the list
#wrote a function that takes the list and sorts it from smallest to largest
#hint: just use m.sort()

import random

n=int(input("Insert positive integer: "))

i=1
m=[]
while i<=n:
    m.append(random.randrange(1,101)) #add a random number from 1 to 100 to the list everytime
    i+=1
print(m)
    
        
def maximum(m):
    return max(m)

def addition(m):
    s=0
    for k in m:
        s=s+k
    return s

def average(m):
    avg= addition(m)/len(m)
    return avg
        
print("Maximum is: ",maximum(m))
print("Sum is: ",addition(m))
print("Average is: ",average(m))
        
def sort_list(m):
    
