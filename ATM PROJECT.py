User_details={"Name":"Neha","Mobile no":" ","ATM PIN":"2255","Balance":10000,"Transaction_history":[]}
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


#withdraw money
if choice=="1":
    amount=int(input("Enter your withdraw amount:"))
    User_details['Balance']=int(User_details['Balance'])
    if amount==0:
        print("Enter valid amount")
    elif amount > User_details['Balance']:
        print("Insufficient Balance")
    else:
        User_details['Balance']-=amount
        User_details['Transaction_history'].append(f"Withdraw: Rs{amount}")
        print(f"Please collect your cash : Rs{amount}")
        print(f"Remaining Balance: Rs{User_details['Balance']}")

#Deposit money
elif choice=="2":
    amount=int(input("Enter amount to Deposit: "))
    if amount==0:
        print("Invalid amount")
    else:
        User_details['Balance']+=amount
        User_details['Transaction_history'].append(f"Desposit: Rs{amount}")
        print(f"{amount} deposited successfully")
        print(f"Updated Balance: Rs{User_details['Balance']}")

#Check Balance
elif choice=="3":
    print(f"Your Balance: Rs{User_details['Balance']}")

#Change PIN
elif choice=="4":
    Old_pin=input("Enter your old pin: ")
    if Old_pin==User_details['ATM PIN']:
        New_pin=input("Enter your new pin:")
        if len(New_pin)==4:
            User_details['ATM PIN']==New_pin
            print("New pin changed successfully")
        else:
            print("Pin must be 4 digits")
    else:
        print("Incorrect old pin")

#Transaction History
else:
    print("Transaction History :")
    if len(User_details['Transaction_history'])==0:
        print("No Transaction yet")
        for g in User_details['Transaction_history']:
            print(t)
    
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
