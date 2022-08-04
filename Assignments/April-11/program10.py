# WAP to insert 'Sachin", "Rahul", "Saurav", "Virendra", "Rohit" in object of ArrayList and print it,
# now add new value as "Roshan" and print the updated values of ArrayList,update the "Saurav" value
# with "Ritik"

# name_list = ["Sachin", "Rahul", "Saurav", "Virendra", "Rohit"]
name_list = []
for i in range(5):
    val = input("Enter name:")
    name_list.append(val)
print("List of name:", name_list)

# for adding new value
name = input("Enter name to add in list:")
name_list.append(name)
print("After adding new value:", name_list)

# for updating value
choice = input("do you want to update name in list?press y if yes ")
if choice.lower() == 'y':
    new_name = input("Enter new name:")
    old_name = input("Enter old name:")
    for i in name_list:
        if i.lower() == old_name.lower():
            index = name_list.index(old_name)
            name_list.remove(old_name)
            name_list.insert(index, new_name)
            print("Updated list")
            print(name_list)
            break
        else:
            continue
    else:
        print("Old name does not exist in list.")
else:
    print("Thank You!")
