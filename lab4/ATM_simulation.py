# Menu driven ATM simulation program.

# Initials
balance = 5000
PIN = 1234
deposit = 0

while True:
    # display menu
    print("------------------------------------")
    print("            ATM MENU")
    print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit")
    print("------------------------------------")

    # taking user input
    choice = int(input("Select the transaction to proceed: "))

    # Error message for incorrect pin
    pin = int(input("Enter ATM PIN: "))
    if( pin != PIN ):
        print("ERROR: Incorrect Pin!")

    # execute if pin is correct
    else:
        # defining menu options
        match choice:
            case 1: 
                print("Account Balance = ", balance)
            case 2:
                deposit = int(input("Enter the amount to deposit: "))
                balance = balance + deposit
                print("Account Balance = ", balance)
            case 3:
                withdraw = int(input("Enter the amount to withdraw: "))
                if( withdraw > balance):
                    print("ERROR: Insufficient Balance")
                else:
                    balance = balance - withdraw 
                    print("Account Balance = ",balance)
            case 4:
                PIN = int(input("Enter NEW ATM PIN: "))
            case 5:
                print("Thank You :)")
                break
            case _:
                print("")
        