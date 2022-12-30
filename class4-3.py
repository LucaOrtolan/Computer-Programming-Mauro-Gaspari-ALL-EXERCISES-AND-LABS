def GCD(A,B):
    if A<B:
        C=B
        B=A
        A=C
    R=A%B
    if R==0:
        print(B)
    else:
        GCD(B,R)

GCD(16,20)
    