##Write a function that takes as parameters two lists of integers of
##any length respectively containing bases and exponents and
##returns the list of exponentiation for any index if both the base and
##the exponent exists.

##bases=list(input("Insert bases: "))
##bases=[int(i) for i in bases]
##exponents=list(input("Insert exponents: "))
##exponents=[int(i) for i in exponents]
##
##def exponentiation(bases,exponents):
##    exp_list=[]
##    for i in bases:
##        for j in exponents:
##            e=i**j
##            exp_list.append(e)
##    return exp_list
##            
##
##
##print(exponentiation(bases,exponents))

#Teacher's version


def exponentiation(L1,L2):
    LE=[]
    M=min(len(L1),len(L2))
    i=0
    while i<M:
        LE.append(L1[i]**L2[i])
        i+=1
    return LE

print(exponentiation([2,3,4,4],[3,4,5,6,7,8]))


#With dictionary
#key is the base. If I have just one key, the exponentiation is the value
#if I have more elements with the same base in the list I will have all list of values in the dictionary
#d[3]=xxx (3 occurs just one time)
#d[2]=[x,y] if 2 occurs 2 times

def expn(L1,L2):
    LE={}
    M=min(len(L1),len(L2))
    i=0
    while i<M:
        if L1[i] in LE:
            if type([])==type(LE[L1[i]]):
                LE[L1[i]].append(L1[1]**L2[i])
            else:
                LE[L1[i]]=[LE[L1[i]**L2[i]]]
                LE[L1[i]].append{L1[i]**L2[i]}
        else:
            LE[L1[i]]=L1[i]**L2[i]
        i+=1
    return LE

print(expn([2,3,4,4],[3,4,5,6,7,8]))


