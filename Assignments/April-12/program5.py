# Assignment 5 :
# "Using ""public"" access specifier,
# Declare Customer class inside the package called ""Pack""  and
# declare variables as Cust_ID,Cust_Name,Quantity,Rs, Total_Rs. and
# accept Cust_ID,Cust_Name,Quantity  and accept it from user using constrctor
# and based on following conditions calculate Rs. and Total_Rs.

#  Product_Name = 'MI"" then Rs=9000 and discount will 3% on Rs.
#  Product_Name = 'Oppo"" then Rs=10500 and discount will 5% on Rs.

# 3.print all informtion using  printInfo() from another class called
# ""AccessCustomer"" which will be inside same package called ""Pack"".


class Customer:
    def __init__(self, cust_id, cust_name, quantity, p_name):
        self.custid = cust_id
        self.cust_name = cust_name
        self.quantity = quantity
        self.p_name = p_name
        self.price = 0
        self.total = 0

    def calculate(self, p_name):
        if p_name.lower() == "mi":
            self.price = 9000
            discount = (self.quantity*self.price)*((3*self.quantity)/100)
            self.total = (9000*self.quantity)-discount

        elif p_name.lower() == "oppo":
            self.price = 10500
            discount = (self.quantity*self.price)*((5*self.quantity)/100)
            self.total = (10500*self.quantity)-discount

        else:
            print("Product does not exists.")


class AccessCustomer(Customer):
    def printinfo(self):
        print(
            f"""Customer ID:{self.custid}\nCustomer Name:{self.cust_name}\nProduct Name:{self.p_name}\nQuantity:{self.quantity}\nPrice:{self.price}\nTotal Price:{self.total}""")


cid = int(input("Enter Customer ID:"))
cname = input("Enter Customer Name:")
pname = input("Enter Product Name(Oppo or Mi):")
qnt = int(input("Enter Quantity:"))
c = AccessCustomer(cid, cname, qnt, pname)
c.calculate(pname)
print("-------Details--------")
c.printinfo()
