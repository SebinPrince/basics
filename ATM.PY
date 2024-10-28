'''AUTHOR:SEBIN PRINCE
DATE:28/10/24
DESCRIPTION:Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to:

    Check Balance
    Deposit Money
    Withdraw Money
    Exit

The program should run in a loop until the user chooses to exit. For each option, use if, elif, and else to manage each choice. Ensure that the balance doesn’t go below zero during a withdrawal.
balance_amount=1000
while True:
    print("\n1.\tCheck balance")
    print("2.\tDeposite money")
    print("3.\tWithdraw money")
    print("4.\tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    if choice==4:
        break
    elif choice==2:
        deposite_amount=float(input("Enter your amount:"))
        balance_amount=balance_amount + deposite_amount
        print(f"the deposited amount ${deposite_amount} and" f"The current balance ${balance_amount}")
    elif choice==3:
        withdraw_money=float(input("Enter your withdraw money:"))

        if withdraw_money>balance_amount:
            print("Insufficent Balance")
        else:
            balance_amount = balance_amount - withdraw_money

        print(f"The amount withdraw from the account" 
              f"${withdraw_money} The balance amount"
              f"${balance_amount}")

    elif choice == 4:
        break
    else:
        print("Invalid entry")
        '''




