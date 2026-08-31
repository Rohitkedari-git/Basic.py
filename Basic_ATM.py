balance = 150

while True:
    print("==============================")
    print("          ATM MACHINE         ")
    print("==============================")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    print("==============================")

    option = int(input("Enter Your Option: "))

    if option == 1:
        print("Your Balance is:", balance)

    elif option == 2:
        withdraw = int(input("Enter Amount to Withdraw: "))

        if withdraw > balance:
            print("Insufficient Balance!")
        else:
            balance -= withdraw
            print("Withdrawal Successful! New Balance:", balance)

    elif option == 3:
        deposit = int(input("Enter Amount to Deposit: "))
        balance += deposit
        print("Deposit Successful! New Balance:", balance)

    elif option == 4:
        print("Thank You for Using the ATM Machine!")
        break

    else:
        print("Invalid Option! Please Try Again.")
