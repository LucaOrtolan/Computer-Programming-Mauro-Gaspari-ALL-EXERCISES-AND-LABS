## Write (using the for statament) a function that
##gets a string of digits and compute the sum, the
##average, the maximun and the minimum of them
##transforming them into integers.


def calc(s):
    summ=0
    for i in range(len(s)):
        n=int(s[i])
        summ=summ+n
    print("Max= ",max(s))
    print("Min= ",min(s))
    print("Sum= ",summ)
    print("Average= ",summ/len(s))

        
    

s=input("Insert string of digits: ")
calc(s)
