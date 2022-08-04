# print("Welcome To The Shop")
# while True:
#     p = Product()
#     print("1.Admin\n2.Customer")
#     ch = input("Please Select option:")
#     if ch == "1":
#         print("Welcome Admin")
#         while True:
#             print("-"*20)
#             print("1:Update Quantity\n2:Display Product\n3.Exit")
#             option = input("Enter your choice:")
#             if option == "1":
#                 pname = input("Enter Product name:")
#                 pname = pname.lower()
#                 qnt = int(input("Enter Product Quantity:"))
#                 p.update_quantity(pname, qnt)
#             elif option == "2":
#                 p.display_product()
#             elif option == "3":
#                 print("Thanks You...!")
#                 break
#             else:
#                 print("Please enter valid choice.")
#     # For Customer
#     elif ch == "2":
#         print("Welcome Customer")
#         while True:
#             print("-"*20)
#             print("1:Buy Products\n2:Exit")
#             option = input("Enter your choice:")
#             if option == "1":
#                 cid = int(input("Enter Customer ID:"))
#                 cname = input("Enter Customer Name:")
#                 pname = input("Enter Product Name(laptop,mobile,keyboard):")
#                 qnt = int(input("Enter Quantity:"))
#                 c = Customer(cid, cname, pname, qnt)
#                 c.calculate()
#                 c.display_bill()
#                 p.update_quantity(pname, qnt)
#                 p.display_product()
#             elif option == "2":
#                 print("Thanks for shopping with us.")
#                 break
#             else:
#                 print("Please enter valid choice.")
#     elif ch == "3":
#         sys.exit()
#     else:
#         print("Please Choose Valid Input.")
