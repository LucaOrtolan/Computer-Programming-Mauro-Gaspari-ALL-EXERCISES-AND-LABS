def semifact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*semifact(n-2)
n=int(input("Insert number: "))
print(semifact(n))

