import json
from pathlib import Path


class ATM:
    def display(self, data):
        print("\t=====Account Detail=====")
        print(
            f"\tAccount No:{data['acc_no']}\n\tUsername:{data['username']}\n\tAccount Type:{data['acc_type'].upper()}\n\tBalance: ₹{data['amount']}")
        # print(
        #     f"Account No.\tUsername\tAccount Type\tBalance\n\t{item['acc_no']}\t{item['username']}\t\t{item['acc_type'].upper()}\t\t ₹{item['amount']}")
        print("--"*20)

    def save_data_to_file(self, data):
        with open("data.json", "w") as write_file:
            json.dump(data, write_file)

    def read_data_from_file(self):
        with open("data.json") as file:
            data = Path("data.json").read_text()
            return(json.loads(data))

    def check_acc_no(self, acc_no):
        data = self.read_data_from_file()
        for item in data:
            if item['acc_no'] == acc_no:
                return acc_no
        else:
            return None

    def check_balance(self, acc_no):
        acc_no = self.check_acc_no(acc_no)
        data = self.read_data_from_file()
        for item in data:
            if item['acc_no'] == acc_no:
                return item

    def deposit(self, acc_no, amount):
        data = self.read_data_from_file()
        for index, item in enumerate(data):
            if item['acc_no'] == acc_no:
                data[index]['amount'] += amount
        self.save_data_to_file(data)
        item = self.check_balance(acc_no)

    def withdraw(self, acc_no, amt):
        with open("data.json") as file:
            data = Path("data.json").read_text()
            data = json.loads(data)
            for index, item in enumerate(data):
                if item['acc_no'] == acc_no:
                    balance = data[index]['amount']
                    if balance <= 1000:
                        print("Account balance is 1000 Rs,can't withdraw amount.")
                    elif (balance-amt) < 1000:
                        print(
                            "you can't withdraw money as minimum 1000 rs required in account.")
                    elif balance < amt:
                        print("'Insufficient Balance !!'")
                    else:
                        data[index]['amount'] -= amt
        self.save_data_to_file(data)

    def transfer(self, sender, receiver, amt):
        sender_info = self.check_balance(sender)
        receiver_info = self.check_balance(receiver)
        if sender_info['acc_type'] == receiver_info['acc_type']:
            self.withdraw(sender, amt)
            self.deposit(receiver, amt)
            print("Amount Transfer Succesfully")
        else:
            print("You can not transfer money.")


while True:
    c = ATM()
    print("-x-x-x-Welcome To ATM-x-x-x-")
    print('1.Check Balance\n2.Deposit\n3.Withdraw\n4.Transfer Funds\n5:Exit')
    try:
        ch = int(input("Please enter your choice:"))
        print("-"*25)
        if ch == 1:
            acc_no = int(input("Enter account number:"))
            item = c.check_balance(acc_no)
            if item == None:
                print("Invalid Account Number")
            else:
                c.display(item)
            # print("="*25)
        elif ch == 2:
            acc_no = int(input("Enter account number:"))
            amt = float(input("Please enter amount to deposit:"))
            c.deposit(acc_no, amt)
            print("Amount Deposited Succesfully...!!!\nCheck your balance.")
        elif ch == 3:
            acc_no = int(input("Enter account number:"))
            amt = float(input("Enter amount:"))
            c.withdraw(acc_no, amt)
        elif ch == 4:
            sender_acc_no = int(input("Enter sender's account number:"))
            receiver_acc_no = int(input("Enter receiver's account number:"))
            amt = int(input("Enter amount:"))
            c.transfer(sender_acc_no, receiver_acc_no, amt)
        elif ch == 5:
            print("Thanks for using our services.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid Input....!")
