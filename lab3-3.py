####Write fib_i: the iterative version of the Fibonacci
####function.
####● Write a script that compares the iterative and
####recursive versions
##Extend the solution of exercise 3 so that the result
##is exported to a csv file.



def rfib(n):
    if n<=1:
        return n
    else:
        return rfib(n-1)+rfib(n-2)
            

def ifib(n):
    if n==0:
        return 0
    F_n1=1
    F_n2=0
    for i in range(1,n):
        summ=F_n1+F_n2
        F_n2=F_n1
        F_n1=summ
    return F_n1
 

n=int(input("Insert positive integer: "))
print("Iterative: ",ifib(n),"Recursive: ",rfib(n))
