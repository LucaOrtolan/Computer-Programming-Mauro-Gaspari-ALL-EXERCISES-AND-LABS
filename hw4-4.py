##● Consider a list that represents a bank with the following structure:
##● BANK = [[NAME1,PIN2,AMOUNT1], [NAME2,PIN2,AMOUNT2],
##….]
##● Write a script that asks to the user the number of accounts in the
##bank N, and then fills the data asking them to the user.
##● Update the simple cash dispenser developed the last week so that
##it works with this extended version of the BANK data structure.

N=int(input("How many accounts do you want to register? "))

BANK=[]

for i in range(0,N):
    BANK.append([input("Insert username: "), input("Insert PIN: "), float(input("Insert amount: "))])

#UPDATE

def atm(B):
    while True:
        tag=False              #user not yet found
        print(B)
        user=input("Enter your name: ")
        for account in B:
            if account[0]==user:
                tag=True                 #user found
                myaccount=account
                break
            
        if not tag:      #incorrect user
            print("User not correct")
            continue
        
        a=0  #number of attempts
        tag2=False          #password not yet found
        while a<3:
            pswd=input("Enter password: ")
            if pswd==myaccount[1]:
                money=int(input("How much: "))
                if myaccount[2]>money:
                    myaccount[2]-=money
                    print("Withdraw succesful")
                    tag2=True          #correct pswd
                    break
                else:
                    print("Not enough funds")
                    break
            else:
                a+=1
            if not tag2:         #pswd not correct
                print("Incorrect password")
                
atm(BANK)

