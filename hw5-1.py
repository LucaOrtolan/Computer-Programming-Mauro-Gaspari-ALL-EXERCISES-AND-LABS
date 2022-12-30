# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 19:02:04 2022

@author: Luca
"""

# Terminate the exercise done in class implementing the single accounts as an
# oblect adding operations for printing accounts.
# ● Add an option to the cash dispenser that would allow to activate a management
# interface used to print the status of accounts and add new users. This option
# will be activated entering admin as an user name and a password.

class account:
    def __init__(self,user,pswd,amount,admin):
        self.user=user
        self.pswd=pswd
        self.amount=amount
        self.admin=admin
        

   
accLuca=account("Luca","1234",5000,"no")
accMauro=account("Mauro","9999",20000,"yes")

BANK={"Luca":accLuca, "Mauro":accMauro}


def atm(B):
    while True:
        user=input("Enter your name: ")
        try:
            a=0 
            tag2=False        
            while a<3:
                pswd=input("Enter password: ")
                if pswd==BANK[user].pswd:
                    if BANK[user].admin=="yes":
                        k=input("Type 'add' to add new accounts, type 'show' to show all the accounts, type anything else to withdraw: ")
                        if k=="add":
                            u=input("Type username: ")
                            p=input("Type PIN: ")
                            am=int(input("Insert amount "))
                            ad=input("Is admin? ('yes' or 'no') ")
                            BANK[u]=account(u,p,am,ad)
                            atm(B)
                        if k=="show":
                            for user in BANK:
                                print(BANK[user].user,BANK[user].pswd,BANK[user].amount,BANK[user].admin)
                            atm(B)
                        else:
                            pass
                    money=int(input("How much: "))
                    if BANK[user].amount>money:
                        BANK[user].amount-=money
                        print("Withdraw succesful")
                        tag2=True
                        break
                    else:
                        print("Not enough funds")
                        break
                else:
                    a+=1
                if not tag2:
                    print("Incorrect password")
        except:
            print("the user isn't correct")
            continue

atm(BANK)
