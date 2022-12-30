##Write a dummy python interpreter using while
##and break to exit.
##The dummy interpeter returns False when reads
##True and viceversa, otherwise always returns
##“syntax error”



while True:
    line=input(">>")
    if line=="True":
        print("False")
    elif line=="False":
        print("True")
    elif line=="stop":
        print("Stopped")
        break
    else:
        print("Syntax Error")
        

