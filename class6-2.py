##Write a function indent_string(n,string) which
##prints the string n+1 times indenting it from 0 to
##n as follows: indent_string(5,”duffy”)
##duffy
## duffy
##  duffy
##   duffy
##    duffy
##     duffy
##Hint: use the expression ' '*i to print i blanks.

def indent_string(n,string):
    i=0
    while i<n:
        print(" "*i,string)
        i=i+1

indent_string(30,"matteo")
    
