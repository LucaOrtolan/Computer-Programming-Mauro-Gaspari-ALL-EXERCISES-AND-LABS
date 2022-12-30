def sec(N):
    d=N*365
    h=24*d
    m=60*h
    s=60*m
    return(s)

N=int(input("insert number of years:"))
print("the number of seconds is:", sec(N))
