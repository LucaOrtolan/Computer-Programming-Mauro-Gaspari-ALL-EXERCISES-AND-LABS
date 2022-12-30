#Cash dispenser with dictionary

BANK ={"pippo":["pippo","1234",39999],"pluto":["pluto","5555",30000]}

def atm(B):
    while True:
        tag=False              #user not yet found
        print(B)
        user=input("Enter your name: ")
        if not (user in B):
            print("the user isn't correct")
            continue
        myaccount=B[user]
    
        
        
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

atm(Bank)
