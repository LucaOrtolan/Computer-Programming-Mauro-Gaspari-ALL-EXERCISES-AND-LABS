##● Write a function that takes as input a list of both lower case and
##upper case strings and returns an ordered list.
##● Write a user interface that asks the user for the length of the list
##and for the strings, creates the list and executes the ordering
##function.
##● Hint: use the functions compare_strings and bubblesort previously
##defined.

def compare_string(string1,string2):
    L_string1=string1.lower()
    L_string2=string2.lower()
    if L_string1<L_string2:
        return True
    else:
        return False

def bubblesort(a):
    flag=True   
    while flag:
        flag=False
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                flag=True
    return a

n=int(input("Insert lenght of the list: "))
a=[]
for i in range(0,n):
    string=input("Insert string: ")
    a.append(string)

print(a)
    
def order(a):
    i=0
    while i<len(a):
        a[i]=a[i].lower()
        i+=1
    return bubblesort(a)

    
print(order(a))
