##Celsius to Fahrenheit Conversion Tables.
##– For values of Celsius from -20 to +30 in steps of 5, produce
##the equivalent Fahrenheit temperature. The following formula
##converts C (Celsius) to F (Fahrenheit).
##F = C * 9/5 + 32
##– For values of Fahrenheit from -10 to 100 in steps of 5, produce
##the equivalent Celsius temperatures. The following formula
##converts F (Fahrenheit) to C (Celsius).
##C = (F - 32) * 5/9


def CtoF():
    C=-20
    while C<=30:
        F=C*9/5+32
        print("C=",C,"F=",F)
        C+=5

CtoF()

def FtoC():
    F=-10
    while F<=100:
        C=(F-32)*5/9
        print("C=",C,"F=",F)
        F+=5

FtoC()

#Export into csv
file_name = 'ex_6 part_1.csv'
f = open(file_name, 'w')

f.write('degree celsius,degree fahrenheit\n')

initial_temperature_celsius = -20
final_temperature_celsius = 30
step = 5

current_temperature_celsius = initial_temperature_celsius

while current_temperature_celsius <= final_temperature_celsius:
    current_temperature_fahrenheit = CtoF()
    f.write('%f,%f\n' % (current_temperature_celsius, current_temperature_fahrenheit))
    current_temperature_celsius += step

f.close()


    
