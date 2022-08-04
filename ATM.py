Balance = 8000
print("""
Select the Options

1. Balance
2. Withdraw
3. Deposit
4. Exit
""")
while True:
    option = int(input("Please select the Option : "))
    Password = int(input("Enter your pin :"))
    if(option == 1 and Password == 1998):
        print("your balance is : ", Balance)
        Anothertransaction = (
            input("Do you want to make another transaction yes/ no"))
        if(Anothertransaction == "yes"):
            continue
        else:
            break
    elif(option == 2 and Password == 1998):
        Withdraw = int(input("Enter withdraw amount: "))
        Balance = Balance - Withdraw
        if(Balance > Withdraw):
            print("plesae collect your money")
            print("your current Balance is :", Balance)
        else:
            print("Unsufficent Balance")
    elif(option == 3 and Password == 1998):
        Deposit = int(input("Enter deposite amount : "))
        Balance = Balance + Deposit
        print("Sucessfully diposited")
        print("Your current Balance is : ", Balance)
    elif(option == 4):
        print("Thank you")
        exit()

    else:
        print("Please select the transaction or enter correct pin")
