##Write a functions that takes as parameter a lists of integers L, an
##integer N, and an integer R and returns True if in L there are
##exactly R occurrences of N, and False otherwise.

##L=[1,2,2,3]
##N=2
##R=2
##TRUE

L=list(input("Digit a list of numbers: "))
L=[int(i) for i in L]
N=int(input("Insert a number that appears on the list: "))
R=int(input("Insert how many times the number occurs in the list: "))

def occurences(L,N,R):
    if N not in L:
        return False
    occ=0
    for i in L:
        if i==N:
            occ+=1
    if occ==R:
        return True
    else:
        return False

print(occurences(L,N,R))

#Teacher's version

def testc(L,N,R):
    cn=0
    for A in L:
        if A==N:
            cn+=1
    if cn==R:
        return True
    else:
        return False

