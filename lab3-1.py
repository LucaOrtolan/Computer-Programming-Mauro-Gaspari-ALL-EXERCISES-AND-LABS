##Write an iterative function ifact that computes the
##factorial of a number n.
##● Remark: if f is the value of the factorial for some
##integer k-1, the value for k is f*k.
##● Write a script that compare ifact with the
##recursive factorial function for values insertet by
##the user


def ifact(n):
    if n<0:
        print("Positive integers only")
    else:
        i=1
        fact=1
        for i in range(1,n+1):
            fact=fact*i
            i+=1
        return fact

def rfact(n):
    if n<0:
        print("Positive integers only")
    elif n==0 or n==1:
        return 1
    else:
        return n*rfact(n-1)

n=int(input("Insert number: "))

print("Iterative: ",ifact(n),"Recursive: ",rfact(n))
        

