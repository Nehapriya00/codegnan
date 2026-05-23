User_details={"Name":"Neha","Mobile no":" ","ATM PIN":"2255","Balance":"10000","Tranction_history":[]}
#to enter atm pin
print("Please insert your ATM Card")
Remaining_attempts=3
while Remaining_attempts>0:
    pin=input("Enter your 4 digit ATM PIN:")
    if len(pin)==4:
        if pin in User_details['ATM PIN']:
            print("Welcome to ATM")
            break
        else:
            Remaining_attempts-=1
            print(f"Enter correct pin you have {Remaining_attempts} left")
        
    else:
        print("Please enter 4 digit ")

choice=input("\n1.Withdraw \n2.Deposit \n3.Check Balance \n4.Change PIN \n5.Transaction History  \nEnter your choice:")
#to withdraw money
if choice=="1":
    amount=int(input("Enter your withdraw amount:"))
User_details['Balance']=int(User_details['Balance'])
if amount==0:
    print("Enter valid amount")
elif amount > User_details['Balance']:
    print("Insufficient Balance")
'''
elif choice=="2":
    print("Deposit")
elif choice=="3":
    print("Check Balance")
elif choice=="4":
    print("Change PIN")
else:
    print("Transaction History")
'''
