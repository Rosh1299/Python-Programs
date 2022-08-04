# "Check results on entering valid User Id & Password
# Accept username and password from user
# if username is V2STech and password is Thane then print message as ""Valid User"""

username = input("Enter Username:")
password = input("Enter Password:")
file = open("credential.txt", "r")
data = file.readlines()
if username == data[0].strip() and password == data[1]:
    print("Valid User")
else:
    print("Please enter valid username or password.")
file.close()
