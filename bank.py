import pygame
pygame.init()

class bank:
    def __init__(self):
            self.balance=100
            
   
            
    def display(self):
        print("Your total balance is",self.balance)
        
    def deposit(self):
        depositamount=int(input("How much do u want to deposit?"))
        self.balance+=depositamount
        print("Kaching! ",depositamount," has been added to your balance")
    def withdraw(self):
        withdrawamount=int(input("How much do u want to withdraw?"))
        if self.balance-withdrawamount<0:
             print("Sorry! Your bankaccount doesnt have enough money to withdraw")
        else:
            self.balance-=withdrawamount
            print("Beep! ",withdrawamount, " Money succesfully withdrawn")
    
    

bank1=bank()   
bank1.display()
ans=input("Would you like to deposit anything? (y/n)")
if ans=="y":
    bank1.deposit()
    bank1.display()
    ans3=input("Would you like to withdraw anything? (y/n)")
    if ans3=="y":

        bank1.withdraw()
        print("Have a nice day!")
        bank1.display()
        print("Bye!")
    else:
         print("Ok! Have a nice day!")
         bank1.display()
         print("Bye!")
         
         
else:
    ans1=input("Ok! Would you like to withdraw anything? (y/n)")
    if ans1=="y":
         bank1.withdraw()
         bank1.display()
    else:
        print("Ok! Have a nice day!")
        bank1.display()
        print("Bye!")