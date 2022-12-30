##Write using while a function tree(n) which prints
##a n levels tree having the form:
##       x
##      xxx
##     xxxxx
##    xxxxxxx
##   xxxxxxxxx

def tree(n):
    i=0
    k=1
    while i<=n:
        print(" "*(n-i),"x"*k)
        i+=1
        k+=2

n=int(input("Insert a positive integer: "))
if n<0:
    print("Positive integers only")
tree(n)
