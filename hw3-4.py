##Considering this exercise.
## Wind chill is used by meteorologists to describe the effect of cold and
##wind combined. Consider the following formula:
## Tw =13.127+0.6215T-11.362v^0,16)+0,396Tv^(0,16)
##where Tw = wind chill in °C   v = wind velocity in km/hrs^(-1)   T = temperature in °C
##Write a script that exports in csv file a wind chill table which includes
##all the values of v (wind speed) from 0 to 70 km hr in steps of 5, and
##all values of T (temperature) from -25 to 10 in steps of 5.Write a
##script that exports in csv file a wind chill table.



import sys #system facility module: allows us to preview the file we're writing


def windchill(T,v):
    tw=13.127+0.6215*T-11.362*v**(0.16)+0.396*T*v**(0.16)
    return tw

#L=lower bound
#H=higher bound
#S=step
#v in rows, T in columns

def rchill(f,L,H,S,v):
    f.write(str(v)+" ;")  
    for t in range(L,H+1,S): #last number is the step #t is temperature
        Tw=round(windchill(t,v),2) #approx windchill by 2 decimals
##        f.write("%4f ;"% Tw)
        f.write(str(Tw)+" ;")  #prints tw with 2 decimals 
    f.write("\n") #writes a new line
            
##rchill(sys.stdout, -25, 10, 5, 5) preview

#write a function that prints the full table: need higher and lower bound for both variables

def tchill(f,Lv,Hv,Sv,Lt,Ht,St):
    f.write("v/T ;")  #first cell is going to be v/T
    for t in range(Lt,Ht+1,St): #first column is going to be the values of t
        f.write(str(t)+" ;")
    f.write("\n")
    for v in range(Lv,Hv+1,Sv):
        rchill(f,Lt,Ht,St,v)

##tchill(sys.stdout,0,70,5,-25,10,5)

#CSV export

filename="windchill.csv"
f=open(filename,"w")
tchill(f,0,70,5,-25,10,5) #puts table into the file
    
        

f.close()
    
    
    
