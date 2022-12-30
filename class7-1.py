##Write a script that takes a string of digits as an
##input and returns the max the min and the average
##values

def stats(string):
    print("Max= ",max(string))
    print("Min= ",min(string))
    k=0
    for i in range(0,len(string)):
        n=int(string[i])
        k=k+n
        average=k/len(string)
    print("Average= ",average)


string=input("Insert a sequence of numbers: ")
stats(string)


