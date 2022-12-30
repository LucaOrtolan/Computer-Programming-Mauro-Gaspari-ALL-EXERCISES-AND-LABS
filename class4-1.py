
#def myinter():
    #m=int(input("Integer: "))
    #if m<0:
        #if m==-1:
            #return
        #else:
            #print("Positive only: ")
    #else:
        #print(fibo(m))
    #myinter()
    
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
            
print(fibo(10))
