import csv


class ATM:
    # method to check balance
    def check_balance(self, acc_no):
        with open("data.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == str(acc_no):
                    print(row)
                    break

    # method to deposit cash
    def deposit(self, acc_no, amount):
        with open("data.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == str(acc_no):
                    print(row)
                    break


while True:
    print("-------Welcome To ATM-------")
    print('1.Check Balance\n2.Deposit\n3.Withdraw\n4.Transfer Funds')
    ch = int(input("Enter your choice:"))
    if ch == 1:
        c = ATM()
        acc_no = int(input("Enter account number:"))
        c.check_balance(acc_no)
    elif ch == 2:
        acc_no = int(input("Enter account number:"))
        amt = int(input("Enter amount:"))
    # elif ch == 3:
    #     pass
    # elif ch == 4:
    #     pass
    elif ch == 5:
        break
    else:
        print("Invalid choice.")
