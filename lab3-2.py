##A palindrome is a string that can be read in the
##same way left to right or right to left.
##● Write a function palindrome that gets a string as
##input and returns True if it is a palindrome,
##otherwise it returns false.

def palin():
    s=input("Insert string: ")
    i=len(s)
    for position in range(i//2):
        opposite=i-position-1
        if s[position]!=s[opposite]:
            return False
    return True
        
    
print(palin()) 
        
    
        
              
    

