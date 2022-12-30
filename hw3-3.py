##Emulate a cash dispenser which is able to deal with 1 account only
##and is always ready for withdraw money.
## The cash dispenser asks for a name, then asks for a password, checks
##if the password is correct. If the password is correct asks the user for
##an amount to withdraw, otherwise asks the user to type the password
##again (only 3 attempt should be supported). If the amount is available
##the cash dispenser prints done and the updated amount, otherwise it
##prints transaction cancelled. When the operation is completed the task
##dispenser asks for a name again and repeats the process.
## Hint: store the data of the account using the following variables:
## name, paswd, amount

paswd="gauro maspari"
amount=1000

def atm():
    name=input("Welcome to PythonBank, please enter your name: ")
    ipaswd=input("Enter your password: ")
    if ipaswd==paswd:
        corrpaswd()
    else:
        for i in range(1,3):
            print("Incorrect password,",3-i,"attempts remaining.")
            ipaswd=input("Try again: ")
            if ipaswd==paswd:
                corrpaswd()
        print("You have reached the maximum number of attempts. Disconnecting the service.")
        
            
            
            
def corrpaswd():
    print("Your available savings are:",amount,"€")
    withdraw=float(input("How much would you like to withdraw? "))
    if withdraw>amount:
        print("Insufficient funds, transaction canceled")
        atm()
    else:
        print("Operation completed, your deposit is now:",amount-withdraw,"€")
        atm()
    
                       
    
atm()
