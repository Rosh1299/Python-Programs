#  Assignment 9
# write  a program  for the scenario: Check whether email id is correct or wrong
# Accept Email id from user and check whether it contains ""@"" and ""."" or not
# if it containd ""@"" an ""."" then it is a valid email id"


email = input("Enter E-mail ID:")
if "@" and "." in email:
    print("It is valid email Id.")
else:
    print("It is invalid email Id.")
