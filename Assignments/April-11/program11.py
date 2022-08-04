# WAP to insert ""Mango"", ""Apple"", ""Grapse"" in Vector object and
# print whether ""Grapse"" are their in object or not.


fruits = []

for i in range(3):
    val = input("Enter name:")
    fruits.append(val)
print("List of name:", fruits)


val = input("Enter fruit name to search in list:")
for fruit in fruits:
    if val.lower() == fruit.lower():
        print(val, "is present in fruits list.")
        break
else:
    print(val, "is not present in list.")
