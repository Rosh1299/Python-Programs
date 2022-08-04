
# product_list = [['1', 'laptop', 10, 30000], [
#     '2', 'mobile', 10, 15000], ['3', 'keyboard', 10, 1200]]

import sys


class Product:
    product_list = [[1, 'laptop', 10, 30000], [
        2, 'mobile', 10, 15000], [3, 'keyboard', 10, 1200]]

    def update_quantity(self, pname, qnt):
        for i in range(len(self.product_list)):
            if pname == self.product_list[i][1]:
                self.product_list[i][2] = self.product_list[i][2]-qnt

    def display_product(self):
        print("-"*5, "Products Detail", "-"*5)
        print("ID\tName\tQuantity\tPrice")
        for i in range(len(self.product_list)):
            print(
                f"{self.product_list[i][0]}\t{self.product_list[i][1]}\t{self.product_list[i][2]}\t\t{self.product_list[i][3]}")
        print("-"*20)

    def update_product(self, pname, qnt):
        for i in range(len(self.product_list)):
            if pname == self.product_list[i][1]:
                self.product_list[i][2] = self.product_list[i][2]+qnt
                print("Product Updated Successfully.")
                break
        else:
            print("Product does not exist.")


class Customer(Product):
    def __init__(self, cust_id, cust_name, prod_name, qnt):
        self.custid = cust_id
        self.cust_name = cust_name
        self.qnt = qnt
        self.prod_name = prod_name
        self.total = 0
        super().__init__()

    def calculate(self):
        for i in range(len(self.product_list)):
            if self.prod_name.lower() == self.product_list[i][1]:
                self.total = self.qnt*self.product_list[i][3]

    def display_bill(self):
        print("-"*5, "Your bill", "-"*5)
        print(
            f"Customer ID:{self.custid}\nCustomer Name:{self.cust_name}\nProduct Name:{self.prod_name}\nQuantity:{self.qnt}\nTotal Amount:{self.total}")


def authenticate_admin():
    username = input("Username:")
    password = input("Password:")
    if username == "admin" and password == "admin123":
        print("Authenticated Successfully...!")
    else:
        print("Unauthorized User...!Please enter valid credentials")
        authenticate_admin()


while True:
    print("Welcome To The Shop")
    print("1:Buy Products\n2:Update Quantity\n3:Display Product\n4.Exit")
    ch = input("Please Select option:")
    p = Product()
    if ch == "1":
        cid = int(input("Enter Customer ID:"))
        cname = input("Enter Customer Name:")
        pname = input("Enter Product Name(laptop,mobile,keyboard):")
        qnt = int(input("Enter Quantity:"))
        c = Customer(cid, cname, pname, qnt)
        c.calculate()
        c.display_bill()
        p.update_quantity(pname, qnt)
        p.display_product()
    elif ch == "2":
        authenticate_admin()
        pname = input("Enter Product name:")
        pname = pname.lower()
        qnt = int(input("Enter Product Quantity:"))
        p.update_product(pname, qnt)
    elif ch == "3":
        p.display_product()
    elif ch == "4":
        print("Thanks for shopping with us.")
        break
    else:
        print("Please enter valid choice.")
