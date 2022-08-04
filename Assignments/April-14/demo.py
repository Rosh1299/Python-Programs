def get_credential():
    file = open("credentials.txt", "r")
    data = file.readlines()
    credential_list = []
    print(len(data))
    for i in range(len(data)+1):
        new_data = data[i].strip()
        list1 = new_data.split('-')
        credential_list.append(list1)
    file.close()
    return credential_list


def add_user():
    username = input("Create new username:")
    data = get_credential()
    uname_list = []
    for i in range(len(data)):
        uname_list.append(data[i][0])
    if username in uname_list:
        print("User exists with the same username.Please enter unique username.")
        add_user()
    else:
        password = input("Create new password:")
        credential = f"{username}-{password}"
        file = open("credentials.txt", "a")
        file.write(credential)
        file.write("\n")
        print("New User Created Successfully.")
        file.close()


def check_credential(username, password):
    data = get_credential()
    for credits in data:
        if username == credits[0] and password == credits[1]:
            print("Welcome to the System :)")
            break
    else:
        print("Please enter valid username or password...!:(")


while True:
    print("-"*20)
    print("1:Create New User\n2:Check Credentials\n3:Exit")
    ch = input("Enter your choice:")
    if ch == "1":
        add_user()
    elif ch == "2":
        username = input("Enter username:")
        password = input("Enter password:")
        check_credential(username, password)
    elif ch == "3":
        print("Thanks You!")
        break
    else:
        print("Please enter valid choice.")
