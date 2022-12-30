 def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))
    else:
        return("Please give a positive integer")
m=int(input("Insert number for m: "))
n=int(input("Insert number for n: "))
print(A(m,n))
