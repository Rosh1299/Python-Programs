# WAP to accept Readers_ID,Readers_Name,Readers_Address and
#  insert in a file called "Readers.txt"


id = int(input("Enter Reader's ID:"))
name = input("Enter Reader's Name:")
address = input("Enter Reader's Address:")

data = f"{id}-{name}-{address}\n"
file = open('Readers.txt', 'a')
file.write(data)
file.close()
print("Data Saved Successfully.")
