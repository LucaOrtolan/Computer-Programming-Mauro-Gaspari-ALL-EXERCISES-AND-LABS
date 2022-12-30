##● It is a sorting algorithm define as follows: It works by repeatedly swapping the
##adjacent elements if they are in wrong order. For example starting from ( 5 1 4
##2 8 ):
##– First Pass: ( 5 1 4 2 8 )→( 1 5 4 2 8 )→( 1 4 5 2 8 )→( 1 4 2 5 8 ).
##– Second Pass: ( 1 4 2 5 8 ) →( 1 2 4 5 8 )
##– Now, the array is already sorted, but the algorithm does not know, one
##whole pass without any swap is needed as a stop condition.
##● Write a Python function bublesort that takes as parameter a list of integers and
##sorts using this algorithm.
##HINT: move the big numbers to the end instead of the small ones.

L=[5,2,3,1,4]

def bubblesort(L):
    flag=True    #Creates a switch
    while flag:     #While the switch is True...  
        flag=False   #... set the switch off
        for i in range(0,len(L)-1):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
                flag=True   #Switch is set on when the condition above is met. When the switch is on for all i in the range, the switch returns to False.
                print(L)
    return L

bubblesort(L)
