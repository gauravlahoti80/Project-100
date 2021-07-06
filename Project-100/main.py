#importing modules
import pyttsx3

#initialising pyttsx3
input_say = pyttsx3.init()

#defining class ATM
class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

#making function to check the balance
    def check_balance(self):
        input_say.say("Your balance is 50000")
        input_say.runAndWait()
        print("Your balance is 50000")

#making function to withdraw the money
    def withdrawl(self,amount):
        new_amount = 50000 - amount
        input_say.say("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
        input_say.runAndWait()
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

#main function
def main():

#taking input for the card number
    input_say.say("insert your card number:- ")
    input_say.runAndWait()
    Card_number = input("insert your card number:- ")

#taking input for the pin number 
    input_say.say("enter your pin number")
    input_say.runAndWait()
    pin_number  = input("enter your pin number:- ")

#assigning values to the atm class
    new_user =  Atm(Card_number ,pin_number)

#getting the activity of the user
    input_say.say("Choose your activity")
    input_say.runAndWait()
    print("Choose your activity ")

#getting the activity of the user
    input_say.say("1.Balance Enquriy   2.withdrawl")
    input_say.runAndWait()
    print("1.Balance Enquriy   2.withdrawl")

#getting the activity of the user
    input_say.say("enter activity number :- ")
    input_say.runAndWait()
    activity = int(input("enter activity number :- "))

#defining the activities
    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        input_say.say("enter the amount: ")
        input_say.runAndWait()
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        input_say.say("enter a valid amount")
        input_say.runAndWait()
        print("enter a valid number")

#calling the main function
if __name__ == "__main__":
    main()