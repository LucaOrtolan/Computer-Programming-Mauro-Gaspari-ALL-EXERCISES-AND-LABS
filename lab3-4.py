##Square root: Newton method
##● If x approximates the square root of a number a, a best
##approximation is y obtained as follows: y=(x+(a/x))/2
##● Write a function square_root(a) that iterates this behaviour until
##the square root is computed.
##● Hint stop the iteration when y is equal to x this can be
##implemented checking if (abs(x-y)<0.00001)

def square_root(a):
    x=a/2
    while True:
        y=(x+(a/x))/2
        if abs(x-y)<0.00001:
            return y
        x=y
            

       

print(square_root(144))
        
